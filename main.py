#main.py
import os
from bottle import route, run
   
@route('/')
def main():
    return "Hello World!"
   
if 'DYNO' in os.environ:
  run(host='0.0.0.0', port=os.environ.get('PORT', 9000))
else: 
  run(host='localhost', port=9000, debug=True, reloader=True)