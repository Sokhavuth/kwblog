#main.py
import os, config, lib
from bottle import run, route, template
from controllers import login, post, category, page, signup, setting
from models import postdb, settingdb
from public import setup

@route('/')
def main():
  config.reset(settingdb.select())
  config.kargs['posts'] = postdb.select(config.kargs['homePagePostLimit'])
  config.kargs['thumbs'] = lib.getPostThumbs(config.kargs['posts'])
  config.kargs['page'] = 1
  return template('home', data=config.kargs)

if 'DYNO' in os.environ:
  run(host='0.0.0.0', port=os.environ.get('PORT', 9000))
else: 
  run(host='localhost', port=9000, debug=True, reloader=True)