#controllers/post.py
import config
from bottle import route, template, request, redirect, response
from models.postdb import postdb

@route('/posting', method="POST")
def posting():
  title = request.forms.get('fpost-title')
  content = request.forms.get('fcontent')
  category = request.forms.get('fcategory')
  postdate = request.forms.get('fpost-date')
  posttime = request.forms.get('fpost-time')
  
  redirect('/login')