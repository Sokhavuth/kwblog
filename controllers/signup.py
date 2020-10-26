#controllers/signup.py
import config, lib, uuid
from bottle import route, template, request, redirect
from models import userdb

@route('/signup')
def signup():
  config.kargs['blogTitle'] = "ទំព័រសមាជិក​"
  config.kargs['posts'] = userdb.select(config.kargs['dashboardPostLimit'])
  config.kargs['thumbs'] = lib.getPostThumbs(config.kargs['posts'], type="user")
  config.kargs['page'] = 1
  return template('dashboard/signup', data=config.kargs)

@route('/user/<id:int>')
def post(id):
  config.kargs['blogTitle'] = "ទំព័រសមាជិក"
  config.kargs['frontPagePostLimit'] = 16
  config.kargs['post'] = userdb.select(1, id)
  config.kargs['posts'] = userdb.select(config.kargs['frontPagePostLimit'])
  config.kargs['thumbs'] = lib.getPostThumbs(config.kargs['posts'], "user")
  config.kargs['page'] = 1
  author = request.get_cookie("logged-in", secret=config.kargs['secretKey'])
  if author:
    config.kargs['showEdit'] = True

  return template('user', data=config.kargs)

@route('/signup', method="POST")
def signupPost():
  author = request.get_cookie("logged-in", secret=config.kargs['secretKey'])
  user = userdb.createTable()

  username = request.forms.getunicode('fusername')
  password = request.forms.getunicode('fpassword')
  rights = request.forms.getunicode('frights')
  email = request.forms.getunicode('femail')
  profile = request.forms.getunicode('fprofile')
  gender = request.forms.getunicode('fgender')
  
  if not user:
    userdb.insert(str(uuid.uuid4().int), username, password, "Admin", email, profile, gender)
  else:
    if ((author != "Guest") and userdb.checkAdmin(author)):
      if 'postId' in config.kargs:
        id = config.kargs['postId']
        userdb.update(username, password, rights, email, profile, gender, id)
        del config.kargs['postId']
      else:
        userdb.insert(str(uuid.uuid4().int), username, password, rights, email, profile, gender)

      redirect('/signup')
    
  redirect('/login')

@route('/user/edit/<id:int>')
def edit(id):
  author = request.get_cookie("logged-in", secret=config.kargs['secretKey'])
  if ((author != "Guest") and userdb.checkAdmin(author)):
    config.kargs['blogTitle'] = "ទំព័រ​កែ​តំរូវ"
    config.kargs['posts'] = userdb.select(config.kargs['dashboardPostLimit'])
    config.kargs['thumbs'] = lib.getPostThumbs(config.kargs['posts'], type="user")
    config.kargs['post'] = userdb.select(1, id)
    config.kargs['edit'] = True
    config.kargs['postId'] = id
    config.kargs['page'] = 1
    return template('dashboard/signup', data=config.kargs)
  
  redirect('/signup')

@route('/user/delete/<id:int>')
def delete(id):
  author = request.get_cookie("logged-in", secret=config.kargs['secretKey'])
  if ((author != "Guest") and userdb.checkAdmin(author)):
    userdb.delete(id)
    
  redirect('/signup')

@route('/user/paginate/<place>')
def paginate(place):
  if place == "frontEnd":
    postLimit = config.kargs['frontPagePostLimit']
  else:
    postLimit = config.kargs['dashboardPostLimit']

  posts = userdb.select(postLimit, page=config.kargs['page'])

  if posts:
    config.kargs['page'] += 1
    thumbs = lib.getPostThumbs(posts, type='user')
    return {'json':posts, 'thumbs':thumbs}
  else:
    return {'json':0}