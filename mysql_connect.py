#  Author: Anton Nedilko
#   Email: arcs3567@gmail.com
#  Source: https://github.com/techeditorsrc
#    Info: Some functions for MySql
# License: GPL v3


import mysql.connector
db=None
cr=None

def init_db(host_,user_,password_):
  global db,cr
  r=True
  try:
    db = mysql.connector.connect(
      host=host_,
      user=user_,
      password=password_
    )
    cr = db.cursor(buffered=True)
  except mysql.connector.Error as error:
    print("Failed: {}".format(error))
    r=False
  return r

def connect_db(host_,user_,password_,database_):
  global db,cr
  r=True
  try:
    db = mysql.connector.connect(
      host=host_,
      user=user_,
      password=password_,
      database=database_
    )
    cr = db.cursor(buffered=True)
  except mysql.connector.Error as error:
    print("Failed: {}".format(error))
    r=False
  return r

def exec_db(param):
  global db,cr
  r=True
  if db and cr:
    try:
      cr.execute(param)
    except mysql.connector.Error as error:
      print("Failed: {}".format(error))
      r=False
  return r

def use_db(database_name):
  return exec_db("USE "+database_name) 

def exists_db(database_name):
  global db,cr
  r=False
  if db and cr:
    if exec_db("SHOW DATABASES"):
      for i in cr:
        if i[0]==database_name:
          r=True
          break
  return r

def exists_table(table_name):
  global db,cr
  r=False
  if db and cr:
    if exec_db("SHOW TABLES"):
      for i in cr:
        if i[0]==table_name:
          r=True
          break
  return r

def create_db(database_name):
  return exec_db("CREATE DATABASE IF NOT EXISTS "+database_name)

def create_table(param):
  return exec_db(param)

def append_table(table_name,param):
  return exec_db("INSERT INTO "+table_name+" VALUES\n"+param)

def close_db():
