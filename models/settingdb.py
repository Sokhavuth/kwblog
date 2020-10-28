#models/settingdb.py
import os
import psycopg2

def connect():
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

  return (cursor, conn)

def createTable(): 
  cursor, conn = connect()

  SQL = '''CREATE TABLE IF NOT EXISTS SETTING(
  BLOGTITLE TEXT,
  SECRETKEY TEXT,
  DASHBOARDPOSTLIMIT INT,
  FRONTPAGEPOSTLIMIT INT,
  HOMEPAGEPOSTLIMIT INT,
  AUTHORPAGEPOSTLIMIT INT,
  CATEGORYPOSTLIMIT INT
  )'''

  cursor.execute(SQL)
  
  cursor.execute("SELECT * FROM SETTING LIMIT 1")
  result = cursor.fetchone()
  conn.commit()
  conn.close()
  return result

def insert(*setting):
  cursor, conn = connect()

  SQL = "INSERT INTO SETTING VALUES %s"
  cursor.execute(SQL, (setting,))
  
  conn.commit()
  conn.close()

def select():
  createTable()
  cursor, conn = connect()

  cursor.execute("SELECT * FROM SETTING LIMIT 1")
  result = cursor.fetchone()

  conn.commit()
  conn.close()
  return result

def update(*args):
  cursor, conn = connect()

  sql = '''UPDATE SETTING SET 
  BLOGTITLE = %s, 
  SECRETKEY = %s, 
  DASHBOARDPOSTLIMIT = %s, 
  FRONTPAGEPOSTLIMIT = %s, 
  HOMEPAGEPOSTLIMIT = %s, 
  AUTHORPAGEPOSTLIMIT = %s,
  SITEDESCRIPTION = %s
   '''
  
  cursor.execute(sql, args)
  
  conn.commit()
  conn.close()
