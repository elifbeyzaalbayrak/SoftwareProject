__author__ = 'elifalbayrak'
import sqlite3
import time
db=sqlite3.connect("user_data.db")
im=db.cursor()
#im.execute("""CREATE TABLE user_info (username,password,age,weight1,height,gender,exercise,goal,weight2)""")
now = time.localtime(time.time())
year, month, day, hour, minute, second, weekday, yearday, daylight = now
#im.execute("""CREATE TABLE user_info2 (username,weight2,year,month,day,food_name,kcal,carbs,protein,fat,amount)""")

im.execute("""SELECT * FROM user_info """)
veriler=im.fetchall()
for i in veriler:
    print i

