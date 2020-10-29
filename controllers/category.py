#controllers/category.py
import config, lib, datetime, uuid
from pytz import timezone
from bottle import route, template, request, redirect, response
from models import categorydb, settingdb, postdb

def getTimeZone():
  khtz = timezone('Asia/Phnom_Penh')
  date = datetime.datetime.now().astimezone(tz=khtz).strftime('%d-%m-%Y')
  time = datetime.datetime.now().astimezone(tz=khtz).strftime('%H:%M:%S')
  return (date, time)

@route('/category')
def post():
  config.reset(settingdb.select())
  config.kargs['blogTitle'] = "ទំព័រ​ជំពូក"
  config.kargs['posts'] = categorydb.select(config.kargs['dashboardPostLimit'])
  config.kargs['thumbs'] = lib.getPostThumbs(config.kargs['posts'])
  config.kargs['datetime'] = getTimeZone()
  config.kargs['page'] = 1
  author = request.get_cookie("logged-in", secret=config.kargs['secretKey'])
  if author:
    config.kargs['author'] = author
    config.kargs['showEdit'] = True

  return template('dashboard/category', data=config.kargs)

@route('/category/<id:int>')
def post(id):
  config.reset(settingdb.select())
  config.kargs['blogTitle'] = "ទំព័រ​ការផ្សាយ"
  config.kargs['post'] = categorydb.select(1, id)
  config.kargs['posts'] = categorydb.select(config.kargs['frontPagePostLimit'])
  print(len(config.kargs['posts']))
  config.kargs['thumbs'] = lib.getPostThumbs(config.kargs['posts'])
  config.kargs['page'] = 1
  author = request.get_cookie("logged-in", secret=config.kargs['secretKey'])
  if author:
    config.kargs['showEdit'] = True

  return template('category', data=config.kargs)

@route('/categories/<name>')
def category(name):
  config.reset(settingdb.select())
  config.kargs['blogTitle'] = "ទំព័រ​ជំពូក"
  config.kargs['category'] = name
  config.kargs['posts'] = postdb.select(config.kargs['categoryPostLimit'], category=name)
  config.kargs['thumbs'] = lib.getPostThumbs(config.kargs['posts'])
  config.kargs['page'] = 1
  author = request.get_cookie("logged-in", secret=config.kargs['secretKey'])
  if author:
    config.kargs['showEdit'] = True

  return template('categories', data=config.kargs)

@route('/categorizing', method="POST")
def posting():
  author = request.get_cookie("logged-in", secret=config.kargs['secretKey'])
  if ((author != "Guest") and categorydb.check(author)):
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
      categorydb.update(title, postdate, posttime, content, id)
      del config.kargs['postId']
    else:
      categorydb.insert(str(uuid.uuid4().int), title, author, postdate, posttime, content)
  
  redirect('/category')

@route('/category/delete/<id:int>')
def delete(id):
  author = request.get_cookie("logged-in", secret=config.kargs['secretKey'])
  if ((author != "Guest") and categorydb.check(author)):
    categorydb.delete(id)

  redirect('/category')

@route('/category/edit/<id:int>')
def edit(id):
  author = request.get_cookie("logged-in", secret=config.kargs['secretKey'])
  if ((author != "Guest") and categorydb.check(author)):
    config.reset(settingdb.select())
    config.kargs['blogTitle'] = "ទំព័រ​កែ​តំរូវ"
    config.kargs['posts'] = categorydb.select(config.kargs['dashboardPostLimit'])
    config.kargs['thumbs'] = lib.getPostThumbs(config.kargs['posts'])
    config.kargs['post'] = categorydb.select(1, id)
    config.kargs['edit'] = True
    config.kargs['postId'] = id
    config.kargs['page'] = 1
    return template('dashboard/category', data=config.kargs)
  
  redirect('/category')

@route('/category/paginate/<place>')
def paginate(place):
  if place == "backend":
    postLimit = config.kargs['dashboardPostLimit']
  else:
    postLimit = config.kargs['frontPagePostLimit']

  posts = categorydb.select(postLimit, page=config.kargs['page'])
  
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
  
@route('/categories/paginate/<category>')
def paginate(category):
  posts = postdb.select(config.kargs['categoryPostLimit'], category=category, page=config.kargs['page'])
  
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
  