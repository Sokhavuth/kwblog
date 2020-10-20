#controllers/post.py
import config
import datetime
from bottle import route, template, request, redirect, response
from models import postdb

@route('/author/<name:re:[a-z]+>')
def author(name):
  #postdate = datetime.datetime.strptime(postdate, "%d-%m-%Y")
  config.kargs['blogTitle'] = "ទំព័រ​អ្នក​និពន្ធ"
  return template('author', data=config.kargs)