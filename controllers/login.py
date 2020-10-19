#controllers/login.py
import config
from pytz import timezone
from datetime import datetime 
from bottle import route, template, request, response, redirect
from models import userdb

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
  time = datetime.now().astimezone(tz=khtz).strftime('%H:%M')
  return (date, time)

@route('/signup', method="POST")
def signup():
  username = request.forms.get('fusername')
  password = request.forms.get('fpassword')
  rights = request.forms.get('frights')
  email = request.forms.get('femail')

  userdb.insert(username, password, rights, email)

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
    config.kargs['blogTitle'] = "ទំព័រ​គ្រប់គ្រង"
    config.kargs['datetime'] = getTimeZone()
    return template('dashboard/home', data=config.kargs)
  else:
    return template('login', data=config.kargs)