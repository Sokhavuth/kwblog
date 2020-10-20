#controllers/posting.py
import config
import datetime, uuid
from bottle import route, template, request, redirect, response
from models import postdb

@route('/posting', method="POST")
def posting():
  author = request.get_cookie("logged-in", secret=config.kargs['secretKey'])
  if ((author != "Guest") and postdb.check(author)):
    title = request.forms.getunicode('fpost-title')
    if title == "":
      title = "untitled"

    postdate = request.forms.getunicode('fpost-date')
    posttime = request.forms.getunicode('fpost-time')
    category = request.forms.getunicode('fcategory')
    content = request.forms.getunicode('fcontent')
  
    try:
      postdate = datetime.datetime.strptime(postdate, "%d-%m-%Y")
    except ValueError:
      config.kargs['message'] = 'ទំរង់​កាលបរិច្ឆេទ​មិន​ត្រឹមត្រូវ!'
      return template('dashboard/home', data=config.kargs)

    try:
      datetime.datetime.strptime(posttime, "%H:%M:%S")
    except ValueError:
      config.kargs['message'] = 'ទំរង់​ពេល​វេលា​មិន​ត្រឹមត្រូវ!'
      return template('dashboard/home', data=config.kargs)

    postdb.insert(str(uuid.uuid4().int), title, author, postdate, posttime, category, content)
  
  redirect('/login')
