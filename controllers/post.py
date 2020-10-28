#controllers/post.py
import config, lib, datetime, uuid
from bottle import route, template, request, redirect, response
from models import postdb, settingdb, categorydb

@route('/post/<id:int>')
def post(id):
  config.reset(settingdb.select())
  config.kargs['blogTitle'] = "ទំព័រ​ការផ្សាយ"
  config.kargs['post'] = postdb.select(1, id)
  config.kargs['posts'] = postdb.select(config.kargs['frontPagePostLimit'])
  config.kargs['thumbs'] = lib.getPostThumbs(config.kargs['posts'])
  config.kargs['page'] = 1
  author = request.get_cookie("logged-in", secret=config.kargs['secretKey'])
  if author:
    config.kargs['showEdit'] = True

  return template('post', data=config.kargs)

@route('/posting', method="POST")
def posting():
  author = request.get_cookie("logged-in", secret=config.kargs['secretKey'])
  if ((author != "Guest") and postdb.check(author)):
    title = request.forms.getunicode('fpost-title')
    if title == "":
      title = "untitled"

    postdate = request.forms.getunicode('fpost-date')
    posttime = request.forms.getunicode('fpost-time')
    category = request.forms.getunicode('fcategory')
    content = request.forms.getunicode('fcontent')

    try:
      postdate = datetime.datetime.strptime(postdate, "%d-%m-%Y")
    except ValueError:
      config.kargs['message'] = 'ទំរង់​កាលបរិច្ឆេទ​មិន​ត្រឹមត្រូវ!'
      return template('dashboard/home', data=config.kargs)

    try:
      posttime = datetime.datetime.strptime(posttime, "%H:%M:%S")
    except ValueError:
      config.kargs['message'] = 'ទំរង់​ពេល​វេលា​មិន​ត្រឹមត្រូវ!'
      return template('dashboard/home', data=config.kargs)

    if 'postId' in config.kargs:
      id = config.kargs['postId']
      postdb.update(title, postdate, posttime, category, content, id)
      del config.kargs['postId']
    else:
      id = str(uuid.uuid4().int)
      postdb.insert(id, title, author, postdate, posttime, category, content)

    redirect('/post/'+str(id))
  
  redirect('/login')

@route('/post/delete/<id:int>')
def delete(id):
  author = request.get_cookie("logged-in", secret=config.kargs['secretKey'])
  if ((author != "Guest") and postdb.check(author)):
    postdb.delete(id)

  redirect('/login')

@route('/post/edit/<id:int>')
def edit(id):
  author = request.get_cookie("logged-in", secret=config.kargs['secretKey'])
  if ((author != "Guest") and postdb.check(author)):
    config.reset(settingdb.select())
    config.kargs['blogTitle'] = "ទំព័រ​កែ​តំរូវ"
    config.kargs['posts'] = postdb.select(config.kargs['dashboardPostLimit'])
    config.kargs['thumbs'] = lib.getPostThumbs(config.kargs['posts'])
    config.kargs['categories'] = categorydb.select(amount="all")
    config.kargs['post'] = postdb.select(1, id)
    config.kargs['edit'] = True
    config.kargs['postId'] = id
    config.kargs['page'] = 1
    return template('dashboard/home', data=config.kargs)
  
  redirect('/login')

@route('/paginate/<place>')
def paginate(place):
  if place == "frontEnd":
    postLimit = config.kargs['frontPagePostLimit']
  elif place == 'home':
    postLimit = config.kargs['homePagePostLimit']
  else:
    postLimit = config.kargs['dashboardPostLimit']

  posts = postdb.select(postLimit, page=config.kargs['page'])
  
  def toString(post):
    post[3] = post[3].strftime('%d-%m-%Y')
    post[4] = post[4].strftime('%H:%M:%S')

  if posts:
    config.kargs['page'] += 1
    posts = [list(obj) for obj in posts ]

    [toString(obj) for obj in posts]
    thumbs = lib.getPostThumbs(posts)
  
    return {'json':posts, 'thumbs':thumbs}
  else:
    return {'json':0}
  
@route('/search/<place>', method="POST")
def search(place):
  config.reset(settingdb.select())
  query = request.forms.getunicode('fquery')
  config.kargs['posts'] = postdb.search(query)
  config.kargs['thumbs'] = lib.getPostThumbs(config.kargs['posts'])
  config.kargs['blogTitle'] = "ទំព័រ​ស្វែង​រក"

  if place == "backend":
    return template('dashboard/search', data=config.kargs)
  else:
    return template('search', data=config.kargs)