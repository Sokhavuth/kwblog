#models/userdb.py
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

  SQL = '''CREATE TABLE IF NOT EXISTS USERS(
  ID SERIAL PRIMARY KEY,
  USERNAME TEXT,
  PASSWORD TEXT,
  RIGHTS TEXT,
  EMAIL TEXT,
  PROFILE TEXT
  )'''

  cursor.execute(SQL)

  cursor.execute("ALTER TABLE USERS ADD COLUMN IF NOT EXISTS PROFILE TEXT")

  cursor.execute("SELECT ID FROM USERS LIMIT 1")
  result = cursor.fetchone()
  conn.commit()
  conn.close()
  return result

def insert(*user):
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

  cursor.execute("INSERT INTO USERS (USERNAME, PASSWORD, RIGHTS, EMAIL) VALUES %s ", (user,))
  
  conn.commit()
  conn.close()

def check(username, password):
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

  cursor.execute("SELECT USERNAME, PASSWORD FROM USERS WHERE USERNAME = '"+ username + "' and PASSWORD = '" + password + "' LIMIT 1")
  result = cursor.fetchone()
  if result:
    return True
  else:
    return False
  