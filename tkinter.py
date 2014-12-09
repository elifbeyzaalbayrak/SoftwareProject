# -*- coding: utf-8 -*-
__author__ = 'elifalbayrak'

import Tkinter
import sqlite3
db=sqlite3.connect("food_database.db")
db.text_factory=str
im=db.cursor()

im.execute("""SELECT * FROM nut_data""")
veriler=im.fetchall()
#print veriler

def program():
    x=raw_input("Enter the food name: ")
    y=x.upper()
    for i in veriler:
        if y in i[0]:
            print "Food Name: ",i[0],"Kcal: ",i[1],"Amount: ",i[5]
program()







