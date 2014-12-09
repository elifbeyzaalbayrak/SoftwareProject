# -*- coding: utf-8 -*-
__author__ = 'elifalbayrak'

import csv
import sqlite3
db = sqlite3.connect("food_database.db")
db.text_factory=str

lst=[]

with open('nut_data.csv', 'rb') as f:
    f.readline()
    reader = csv.reader(f)

    for row in reader:
        (NDB_No,Shrt_Desc,Water,Energ_Kcal,Protein,Lipd_Tot,Ash,
        Carbohydrt,Fiber_TD,Sugar_Tot,Calcium,Iron,Magnesium,Phosphorus,
        Potassium,Sodium,Zinc,Copper,Manganese,Selenium,Vit_C,Thiamin,Riboflavin,
        Niacin,Panto_acid,Vit_B6,Folate_Tot,Folic_acid,Food_Folate,Folate_DFE,Vit_B12,
        Vit_A_IU,Vit_A_RAE,Retinol,Vit_E,Vit_K,Alpha_Carot,Beta_Carot,Beta_Crypt,Lycopene,
        Lut_Zea,FA_Sat,FA_Mono,FA_Poly,Cholestrl,GmWt_1,GmWt_Desc1,GmWt_2,GmWt_Desc2,Refuse_Pct)=row
        #print "Name: ",Shrt_Desc,"Calorie: ",float(Energ_Kcal),"Protein: ",float(Protein),"Fat: ",float(Lipd_Tot),"Carbs: ",float(Carbohydrt),"Amount: ",GmWt_Desc1
        a=Shrt_Desc,float(Energ_Kcal),float(Protein),float(Lipd_Tot),float(Carbohydrt),GmWt_Desc1
        lst.append(a)
        #im.execute("""INSERT INTO nut_data VALUES %s"""%(a,))


#db.commit()

#im.execute("""SELECT * FROM nut_data""")
#veriler=im.fetchall()
#for i in veriler:
#    print(i)


im = db.cursor()
im.execute("""CREATE TABLE nut_data (Food_Name,Kcal,Protein,Fat,Carbs,Amount)""")

for i in lst:
    im.execute("""INSERT INTO nut_data VALUES (?,?,?,?,?,?)""" ,i)

db.commit()

im.execute("""SELECT * FROM nut_data""")
veriler=im.fetchall()
for a,b,c,d,e,f in veriler:
    if 'APPLE' in a:
        print a,b,c,d,e,f