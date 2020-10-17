#controllers/post.py
import config
from bottle import route, template, request, redirect, response

@route('/posting', method="POST")
def posting():
  return "Posting"