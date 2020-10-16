#main.py
import os
from bottle import run, route, template
from controllers import home
from public import setup

@route('/')
def main():
  return home.index()

if 'DYNO' in os.environ:
  run(host='0.0.0.0', port=os.environ.get('PORT', 9000))
else: 
  run(host='localhost', port=9000, debug=True, reloader=True)