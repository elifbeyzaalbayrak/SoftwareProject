__author__ = 'elifalbayrak'
import sqlite3
db=sqlite3.connect("user_data.db")
im=db.cursor()
#im.execute("""CREATE TABLE user_info (username,password,age,weight1,height,gender,goal,weight2)""")


im.execute("""SELECT * FROM user_info""")
veriler=im.fetchall()
for i in veriler:
    print i
