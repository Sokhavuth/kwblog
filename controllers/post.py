#controllers/post.py
import config, lib
from bottle import route, template, request, redirect, response
from models import postdb

@route('/post/<id:int>')
def post(id):
  config.kargs['blogTitle'] = "ទំព័រ​ការផ្សាយ"
  config.kargs['post'] = postdb.select(1, id)
  config.kargs['posts'] = postdb.select(config.kargs['frontPagePostLimit'])
  config.kargs['thumbs'] = lib.getPostThumbs(config.kargs['posts'])
  return template('post', data=config.kargs)

@route('/post/delete/<id:int>')
def delete(id):
  author = request.get_cookie("logged-in", secret=config.kargs['secretKey'])
  if ((author != "Guest") and postdb.check(author)):
    postdb.delete(id)

  redirect('/login')

@route('/post/edit/<id:int>')
def edit(id):
  config.kargs['post'] = postdb.select(1, id)
  config.kargs['edit'] = True
  return template('dashboard/home', data=config.kargs)
  