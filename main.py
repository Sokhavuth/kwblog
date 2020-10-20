#main.py
import os, config
from bottle import run, route, template
from controllers import login, posting, post, author
from public import setup

@route('/')
def main():
  config.kargs['blogTitle'] = "គេហទំព័រ​ខ្មែរ​អង្គរ"
  return template('home', data=config.kargs)

if 'DYNO' in os.environ:
  run(host='0.0.0.0', port=os.environ.get('PORT', 9000))
else: 
  run(host='localhost', port=9000, debug=True, reloader=True)