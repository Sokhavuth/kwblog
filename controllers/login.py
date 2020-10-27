#controllers/login.py
import os, config, lib, uuid
from pytz import timezone
from datetime import datetime 
from bottle import route, template, request, response, redirect
from models import userdb, postdb, categorydb, settingdb

def checkLogin(username, password):
  if (username == 'Guest') and (password == 'password'):
    return True
  elif userdb.check(username,password):
    return True
  else:
    return False

def getTimeZone():
  khtz = timezone('Asia/Phnom_Penh')
  date = datetime.now().astimezone(tz=khtz).strftime('%d-%m-%Y')
  time = datetime.now().astimezone(tz=khtz).strftime('%H:%M:%S')
  return (date, time)

@route('/upload')
def upload():
  return template('dashboard/upload', data=config.kargs)

@route('/upload', method='POST')
def saveFile():
  author = request.get_cookie("logged-in", secret=config.kargs['secretKey'])

  upload = request.files.get('fupload')
  name, ext = os.path.splitext(upload.filename)
  if ext not in ('.png','.jpg','.jpeg'):
    return 'File extension not allowed.'

  upload.filename = str(uuid.uuid4().int) + ext
  ROOT_DIR = os.path.dirname(os.path.abspath("config.py"))
  savePath = ROOT_DIR + "/public/images/uploads/"
  config.kargs['uploadUrl'] = "/static/images/uploads/" + upload.filename
  if ((author != "Guest") and postdb.check(author)):
    upload.save(savePath)
    return template('dashboard/uploadurl', data=config.kargs)
  else:
    redirect('/login')

@route('/login', method="POST")
def user():
  username = request.forms.get('fusername')
  password = request.forms.get('fpassword')

  if checkLogin(username, password):
    response.set_cookie("logged-in", username, secret=config.kargs['secretKey'])

  redirect('/login')

@route('/login')
def login():
  user = userdb.createTable()
  username = request.get_cookie("logged-in", secret=config.kargs['secretKey'])
  if not user:
    return template('dashboard/signup', data=config.kargs)
  elif username:
    config.reset(settingdb.select())
    config.kargs['author'] = username
    config.kargs['blogTitle'] = "ទំព័រ​គ្រប់គ្រង"
    config.kargs['datetime'] = getTimeZone()
    config.kargs['posts'] = postdb.select(config.kargs['dashboardPostLimit'])
    config.kargs['categories'] = categorydb.select(amount="all")
    config.kargs['thumbs'] = lib.getPostThumbs(config.kargs['posts'])
    config.kargs['page'] = 1
    return template('dashboard/home', data=config.kargs)
  else:
    return template('login', data=config.kargs)