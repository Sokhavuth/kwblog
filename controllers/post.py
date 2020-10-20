#controllers/post.py
import config
import datetime
from bottle import route, template, request, redirect, response
from models import postdb

@route('/post/<id:int>')
def post(id):
  singlePost = postdb.select(1, id)
  config.kargs['blogTitle'] = "ទំព័រ​ការផ្សាយ"
  config.kargs['post'] = singlePost
  return template('post', data=config.kargs)