#controllers/post.py
import config
from bottle import route, template, request, redirect, response
from models import postdb

@route('/post/<id:int>')
def post(id):
  config.kargs['blogTitle'] = "ទំព័រ​ការផ្សាយ"
  config.kargs['post'] = postdb.select(1, id)
  return template('post', data=config.kargs)