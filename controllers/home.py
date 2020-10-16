#controllers/home.py
import config
from bottle import route, template

config.kargs['message'] = "Hello World!"

def index():
  return template('home', data=config.kargs)