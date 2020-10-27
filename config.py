#config.py
from models import settingdb

setting = settingdb.createTable()

kargs = {}
kargs['message'] = ''
kargs['page'] = 1

def reset(setting):
  kargs['blogTitle'] = setting[0]
  kargs['secretKey'] = setting[1]
  kargs['dashboardPostLimit'] = setting[2]
  kargs['frontPagePostLimit'] = setting[3]
  kargs['homePagePostLimit'] = setting[4]
  kargs['authorPagePostLimit'] = setting[5]
  kargs['blogDescription'] = setting[6]

if not setting:
  settingdb.insert('គេហទំព័រ​ខ្មែរអង្គរ', 'h4!#au%8tb_9@oe+c0te=g=u%cfxb8t8fy%7+(gx2+51!t*b+s', 5, 8, 12, 16, 'Description' )
  setting = settingdb.select()
  
reset(setting)
