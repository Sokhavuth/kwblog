#controllers/category.py
import config, lib, datetime, uuid
from pytz import timezone
from bottle import route, template, request, redirect, response
from models import pagedb

def getTimeZone():
  khtz = timezone('Asia/Phnom_Penh')
  date = datetime.datetime.now().astimezone(tz=khtz).strftime('%d-%m-%Y')
  time = datetime.datetime.now().astimezone(tz=khtz).strftime('%H:%M:%S')
  return (date, time)

@route('/page')
def post():
  config.kargs['blogTitle'] = "ទំព័រ​ស្តាទិក"
  config.kargs['posts'] = pagedb.select(config.kargs['dashboardPostLimit'])
  config.kargs['thumbs'] = lib.getPostThumbs(config.kargs['posts'])
  config.kargs['datetime'] = getTimeZone()
  config.kargs['page'] = 1
  author = request.get_cookie("logged-in", secret=config.kargs['secretKey'])
  if author:
    config.kargs['author'] = author
    config.kargs['showEdit'] = True

  return template('dashboard/page', data=config.kargs)

@route('/page/<id:int>')
def post(id):
  config.kargs['blogTitle'] = "ទំព័រ​ស្តាទិក"
  config.kargs['post'] = pagedb.select(1, id)
  config.kargs['posts'] = pagedb.select(config.kargs['frontPagePostLimit'])
  config.kargs['thumbs'] = lib.getPostThumbs(config.kargs['posts'])
  config.kargs['page'] = 1
  author = request.get_cookie("logged-in", secret=config.kargs['secretKey'])
  if author:
    config.kargs['showEdit'] = True

  return template('page', data=config.kargs)

@route('/paging', method="POST")
def posting():
  author = request.get_cookie("logged-in", secret=config.kargs['secretKey'])
  if ((author != "Guest") and pagedb.check(author)):
    title = request.forms.getunicode('fpost-title')
    if title == "":
      title = "untitled"

    postdate = request.forms.getunicode('fpost-date')
    posttime = request.forms.getunicode('fpost-time')
    content = request.forms.getunicode('fcontent')

    try:
      postdate = datetime.datetime.strptime(postdate, "%d-%m-%Y")
    except ValueError:
      config.kargs['message'] = 'ទំរង់​កាលបរិច្ឆេទ​មិន​ត្រឹមត្រូវ!'
      return template('dashboard/category', data=config.kargs)

    try:
      posttime = datetime.datetime.strptime(posttime, "%H:%M:%S")
    except ValueError:
      config.kargs['message'] = 'ទំរង់​ពេល​វេលា​មិន​ត្រឹមត្រូវ!'
      return template('dashboard/category', data=config.kargs)

    if 'postId' in config.kargs:
      id = config.kargs['postId']
      pagedb.update(title, postdate, posttime, content, id)
      del config.kargs['postId']
    else:
      pagedb.insert(str(uuid.uuid4().int), title, author, postdate, posttime, content)
  
  redirect('/page')

@route('/page/delete/<id:int>')
def delete(id):
  author = request.get_cookie("logged-in", secret=config.kargs['secretKey'])
  if ((author != "Guest") and pagedb.check(author)):
    pagedb.delete(id)

  redirect('/page')

@route('/page/edit/<id:int>')
def edit(id):
  author = request.get_cookie("logged-in", secret=config.kargs['secretKey'])
  if ((author != "Guest") and pagedb.check(author)):
    config.kargs['blogTitle'] = "ទំព័រ​កែ​តំរូវ"
    config.kargs['posts'] = pagedb.select(config.kargs['dashboardPostLimit'])
    config.kargs['thumbs'] = lib.getPostThumbs(config.kargs['posts'])
    config.kargs['post'] = pagedb.select(1, id)
    config.kargs['edit'] = True
    config.kargs['postId'] = id
    config.kargs['page'] = 1
    return template('dashboard/page', data=config.kargs)
  
  redirect('/page')

@route('/page/paginate/<place>')
def paginate(place):
  if place == 'backend':
    postLimit = config.kargs['dashboardPostLimit']
  else:
    postLimit = config.kargs['frontPagePostLimit']

  posts = pagedb.select(postLimit, page=config.kargs['page'])
  
  def toString(post):
    post[3] = post[3].strftime('%d-%m-%Y')
    post[4] = post[4].strftime('%H:%M:%S')

  if posts:
    config.kargs['page'] += 1
    posts = [list(obj) for obj in posts ]

    [toString(obj) for obj in posts]
    thumbs = lib.getPostThumbs(posts)
    print(posts)
    return {'json':posts, 'thumbs':thumbs}
  else:
    return {'json':0}
  