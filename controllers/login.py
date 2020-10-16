import config
from bottle import route, template, request, response, redirect

def checkLogin(username, password):
  if (username == 'admin') and (password == 'password'):
    return True
  else:
    return False

@route('/login', method="POST")
def user():
  username = request.forms.get('fusername')
  password = request.forms.get('fpassword')

  if checkLogin(username, password):
    response.set_cookie("logged-in", username, secret='some-secret-key')
  
  redirect('/login')


@route('/login')
def login():
  username = request.get_cookie("logged-in", secret='some-secret-key')
  if username:
    return 'dashboard'
  else:
    return template('login', data=config.kargs)