#models/userdb.py
import os, config
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
  ID TEXT,
  USERNAME TEXT,
  PASSWORD TEXT,
  RIGHTS TEXT,
  EMAIL TEXT,
  PROFILE TEXT,
  GENDER TEXT
  )'''

  cursor.execute(SQL)
  
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

  cursor.execute("INSERT INTO USERS (ID, USERNAME, PASSWORD, RIGHTS, EMAIL, PROFILE, GENDER) VALUES %s ", (user,))
  
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
  
def checkAdmin(username):
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

  cursor.execute("SELECT USERNAME, RIGHTS FROM USERS WHERE USERNAME = '"+ username + "' and RIGHTS = 'Admin' LIMIT 1")

  result = cursor.fetchone()
  if result:
    return True
  else:
    return False

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
    cursor.execute("SELECT * FROM USERS WHERE ID = '" + str(id) +"'")
  elif page:
    SQL = "SELECT * FROM USERS ORDER BY CTID DESC OFFSET %s ROWS FETCH NEXT %s ROWS ONLY"
    cursor.execute(SQL, (amount*page, amount))
  else:
    cursor.execute("SELECT * FROM USERS ORDER BY CTID DESC LIMIT " + str(amount))
    
  result = cursor.fetchall()
  return result

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

  sql = "UPDATE USERS SET USERNAME = %s, PASSWORD = %s, RIGHTS = %s, EMAIL = %s, PROFILE = %s, GENDER = %s WHERE ID = '%s' "
  
  cursor.execute(sql, args)
  
  conn.commit()
  conn.close()

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

  cursor.execute("DELETE FROM USERS WHERE ID = '" + str(id) + "'")

  conn.commit()
  conn.close()