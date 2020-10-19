import os
import psycopg2

cursor = None
conn = None

def connect():
  if 'DYNO' in os.environ:
    DATABASE_URL = os.environ['DATABASE_URL']
    global cursor, conn
    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    cursor = sconn.cursor()
  else: 
    conn = psycopg2.connect(
      database="postgres", 
      user="postgres", 
      password="sokhavuth", 
      host="localhost", 
      port="5432"
    )

    cursor = conn.cursor()

def createTable():
  connect()
  SQL = '''CREATE TABLE IF NOT EXISTS USERS(
  ID SERIAL PRIMARY KEY,
  USERNAME TEXT,
  PASSWORD TEXT,
  RIGHTS TEXT,
  EMAIL TEXT
  )'''

  cursor.execute(SQL)
  cursor.execute("SELECT ID FROM USERS LIMIT 1")
  result = cursor.fetchone()
  conn.commit()
  conn.close()
  return result

def insert(*user):
  connect()
  cursor.execute("INSERT INTO USERS (USERNAME, PASSWORD, RIGHTS, EMAIL) VALUES %s ", (user,))
  
  conn.commit()
  conn.close()

def check(username, password):
  connect()
  cursor.execute("SELECT USERNAME, PASSWORD FROM USERS WHERE USERNAME = '"+ username + "' and PASSWORD = '" + password + "' LIMIT 1")
  result = cursor.fetchone()
  if result:
    return True
  else:
    return False
  