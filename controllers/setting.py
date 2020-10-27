#controllers/setting.py
import config, lib
from bottle import route, template, request, redirect, response
from models import settingdb, userdb, postdb

@route('/setting', method="POST")
def posting():
  author = request.get_cookie("logged-in", secret=config.kargs['secretKey'])
  if ((author != "Guest") and userdb.checkAdmin(author)):
    blogTitle = request.forms.getunicode('fblog-title')
    secretKey = request.forms.getunicode('fsecret-key')
    dpostLimit = request.forms.getunicode('fdpost-limit')
    fpostLimit = request.forms.getunicode('ffpost-limit')
    hpostLimit = request.forms.getunicode('fhpost-limit')
    apostLimit = request.forms.getunicode('fapost-limit')
    blogDescription = request.forms.getunicode('fblog-description')

    settingdb.update(blogTitle, secretKey, dpostLimit, fpostLimit, hpostLimit, apostLimit, blogDescription)

  redirect('/login')

@route('/setting')
def edit():
  author = request.get_cookie("logged-in", secret=config.kargs['secretKey'])
  if ((author != "Guest") and userdb.checkAdmin(author)):
    config.kargs['blogTitle'] = "ទំព័រ​កែ​តំរូវ"
    config.kargs['posts'] = postdb.select(config.kargs['dashboardPostLimit'])
    config.kargs['thumbs'] = lib.getPostThumbs(config.kargs['posts'])
    config.kargs['post'] = settingdb.select()
    config.kargs['page'] = 1
    return template('dashboard/setting', data=config.kargs)
  
  redirect('/login')
