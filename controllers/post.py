#controllers/post.py
import config
import datetime
from bottle import route, template, request, redirect, response
from models import postdb

@route('/post/<id:int>')
def post(id):
  #postdate = datetime.datetime.strptime(postdate, "%d-%m-%Y")
  config.kargs['blogTitle'] = "ទំព័រ​ការផ្សាយ"
  return template('post', data=config.kargs)