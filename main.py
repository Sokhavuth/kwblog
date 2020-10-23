#main.py
import os, config, lib
from bottle import run, route, template
from controllers import login, post, author
from models import postdb
from public import setup

@route('/')
def main():
  config.kargs['blogTitle'] = "គេហទំព័រ​ខ្មែរ​អង្គរ"
  config.kargs['posts'] = postdb.select(config.kargs['frontPagePostLimit'])
  config.kargs['thumbs'] = lib.getPostThumbs(config.kargs['posts'])
  return template('home', data=config.kargs)

if 'DYNO' in os.environ:
  run(host='0.0.0.0', port=os.environ.get('PORT', 9000))
else: 
  run(host='localhost', port=9000, debug=True, reloader=True)