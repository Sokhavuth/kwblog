import os
import psycopg2

class Postdb():
  def __init__(self):
    if 'DYNO' in os.environ:
      DATABASE_URL = os.environ['DATABASE_URL']
      self.conn = psycopg2.connect(DATABASE_URL, sslmode='require')
      self.cursor = self.conn.cursor()
    else: 
      self.conn = psycopg2.connect(
        database="postgres", 
        user="postgres", 
        password="sokhavuth", 
        host="localhost", 
        port="5432"
      )

      self.cursor = self.conn.cursor()

  def createTable(self):
    SQL = '''CREATE TABLE IF NOT EXISTS POST(
      ID INT PRIMARY KEY NOT NULL,
      TITLE TEXT,
      POSTDATE DATE,
      POSTTIME TIME,
      AUTHOR TEXT,
      CONTENT TEXT,
      CATEGORY TEXT
    )'''

    self.cursor.execute(SQL)
    self.cursor.execute("select version()")
    data = self.cursor.fetchone()
    print("Connection established to: ", data)

    self.conn.commit()
    self.conn.close()


postdb = Postdb()