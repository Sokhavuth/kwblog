#models/postdb.py
import os
import psycopg2

def createTable(): 
  if 'DYNO' in os.environ:
    DATABASE_URL = os.environ['DATABASE_URL']
    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    cursor = conn.cursor()
  else: 
    conn = psycopg2.connect(
      database="postgres", 
      user="postgres", 
      password="sokhavuth", 
      host="localhost", 
      port="5432"
    )

    cursor = conn.cursor()

  SQL = '''CREATE TABLE IF NOT EXISTS POST(
  ID TEXT,
  TITLE TEXT,
  AUTHOR TEXT,
  POSTDATE DATE,
  POSTTIME TIME,
  CATEGORY TEXT,
  CONTENT TEXT
  )'''

  cursor.execute(SQL)
  
  conn.commit()
  conn.close()

def insert(*post):
  createTable()
  if 'DYNO' in os.environ:
    DATABASE_URL = os.environ['DATABASE_URL']
    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    cursor = conn.cursor()
  else: 
    conn = psycopg2.connect(
      database="postgres", 
      user="postgres", 
      password="sokhavuth", 
      host="localhost", 
      port="5432"
    )

    cursor = conn.cursor()

  cursor.execute("INSERT INTO POST (ID, TITLE, AUTHOR, POSTDATE, POSTTIME, CATEGORY, CONTENT) VALUES %s ", (post,))
  
  conn.commit()
  conn.close()

def select(amount, id=None, page=0):
  createTable()

  if 'DYNO' in os.environ:
    DATABASE_URL = os.environ['DATABASE_URL']
    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    cursor = conn.cursor()
  else: 
    conn = psycopg2.connect(
      database="postgres", 
      user="postgres", 
      password="sokhavuth", 
      host="localhost", 
      port="5432"
    )

    cursor = conn.cursor()
  if id and (amount == 1):
    cursor.execute("SELECT * FROM POST WHERE ID = '" + str(id) +"'")
  elif page:
    SQL = "SELECT * FROM POST ORDER BY POSTDATE DESC, POSTTIME DESC OFFSET %s ROWS FETCH NEXT %s ROWS ONLY"
    cursor.execute(SQL, (amount*page, amount))
  else:
    cursor.execute("SELECT * FROM POST ORDER BY POSTDATE DESC, POSTTIME DESC LIMIT " + str(amount))
    
  result = cursor.fetchall()
  return result

def check(username):
  if 'DYNO' in os.environ:
    DATABASE_URL = os.environ['DATABASE_URL']
    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    cursor = conn.cursor()
  else: 
    conn = psycopg2.connect(
      database="postgres", 
      user="postgres", 
      password="sokhavuth", 
      host="localhost", 
      port="5432"
    )

    cursor = conn.cursor()

  cursor.execute("SELECT USERNAME FROM USERS WHERE USERNAME = '"+ username + "' LIMIT 1")
  result = cursor.fetchone()
  if result:
    return True
  else:
    return False

def delete(id):
  if 'DYNO' in os.environ:
    DATABASE_URL = os.environ['DATABASE_URL']
    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    cursor = conn.cursor()
  else: 
    conn = psycopg2.connect(
      database="postgres", 
      user="postgres", 
      password="sokhavuth", 
      host="localhost", 
      port="5432"
    )

    cursor = conn.cursor()

  cursor.execute("DELETE FROM POST WHERE ID = '" + str(id) + "'")

  conn.commit()
  conn.close()

def update(*args):
  if 'DYNO' in os.environ:
    DATABASE_URL = os.environ['DATABASE_URL']
    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    cursor = conn.cursor()
  else: 
    conn = psycopg2.connect(
      database="postgres", 
      user="postgres", 
      password="sokhavuth", 
      host="localhost", 
      port="5432"
    )

    cursor = conn.cursor()

  sql = "UPDATE POST SET TITLE = %s, POSTDATE = %s, POSTTIME = %s, CATEGORY = %s, CONTENT = %s WHERE ID = '%s' "
  
  cursor.execute(sql, args)
  
  conn.commit()
  conn.close()