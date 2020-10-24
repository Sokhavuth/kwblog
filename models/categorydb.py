#models/categorydb.py
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

  SQL = '''CREATE TABLE IF NOT EXISTS CATEGORY(
  ID TEXT,
  TITLE TEXT,
  AUTHOR TEXT,
  POSTDATE DATE,
  POSTTIME TIME,
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

  cursor.execute("INSERT INTO CATEGORY (ID, TITLE, AUTHOR, POSTDATE, POSTTIME, CONTENT) VALUES %s ", (post,))
  
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
    cursor.execute("SELECT * FROM CATEGORY WHERE ID = '" + str(id) +"'")
  elif page:
    SQL = "SELECT * FROM CATEGORY ORDER BY POSTDATE DESC, POSTTIME DESC OFFSET %s ROWS FETCH NEXT %s ROWS ONLY"
    cursor.execute(SQL, (amount*page, amount))
  elif amount == 'all':
    cursor.execute("SELECT * FROM CATEGORY ORDER BY POSTDATE DESC, POSTTIME DESC")
  else:
    cursor.execute("SELECT * FROM CATEGORY ORDER BY POSTDATE DESC, POSTTIME DESC LIMIT " + str(amount))
    
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

  cursor.execute("DELETE FROM CATEGORY WHERE ID = '" + str(id) + "'")

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

  sql = "UPDATE CATEGORY SET TITLE = %s, POSTDATE = %s, POSTTIME = %s, CONTENT = %s WHERE ID = '%s' "
  
  cursor.execute(sql, args)
  
  conn.commit()
  conn.close()