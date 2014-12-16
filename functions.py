__author__ = 'elifalbayrak'

import sqlite3
import math
import time
def calculate_basal_metabolic_rate(gender,weight,height,age):
    if gender==1:
        bmr=66.473+(13.7516*weight)+(5.0033*height)-(6.7550*age)
        return bmr
    if gender==2:
        bmr=655.0955+(9.5634*weight)+(1.8496*height)-(4.6756*age)
        return bmr

def calculate_daily_kcal_intake_need(bmr,exercise):
    if exercise==1:
        kcal_need=bmr*1.2
        return kcal_need
    if exercise==2:
        kcal_need=bmr*1.375
        return kcal_need
    if exercise==3:
        kcal_need=bmr*1.55
        return kcal_need
    if exercise==4:
        kcal_need=bmr*1.725
        return kcal_need
    if exercise==1:
        kcal_need=bmr*1.9
        return kcal_need

def calorie_goal(kcal_need,goal):
    if goal==1:
        kcalgoal=kcal_need-1100
        if kcalgoal<1200:
            goal2=1200
            return goal2
        else:
            goal2=kcalgoal
            return goal2
    if goal==2:
        kcalgoal=kcal_need-880
        if kcalgoal<1200:
            goal2=1200
            return goal2
        else:
            goal2=kcalgoal
            return goal2
    if goal==3:
        kcalgoal=kcal_need-550
        if kcalgoal<1200:
            goal2=1200
            return goal2
        else:
            goal2=kcalgoal
            return goal2
    if goal==4:
        kcalgoal=kcal_need-220
        if kcalgoal<1200:
            goal2=1200
            return goal2
        else:
            goal2=kcalgoal
            return goal2
    if goal==5:
        kcalgoal=kcal_need
        if kcalgoal<1200:
            goal2=1200
            return goal2
        else:
            goal2=kcalgoal
            return goal2
    if goal==6:
        kcalgoal=kcal_need+220
        return kcalgoal
    if goal==7:
        kcalgoal=kcal_need+550
        return kcalgoal
    if goal==8:
        kcalgoal=kcal_need+880
        return kcalgoal
    if goal==9:
        kcalgoal=kcal_need+1100
        return kcalgoal

def user_calorie_goal(lst):
    username=lst[0]
    password=lst[1]
    db=sqlite3.connect("user_data.db")
    im=db.cursor()
    im.execute("""SELECT * FROM user_info where username=? and password=?""",(username,password))
    user_info=im.fetchone()
    age=user_info[2]
    weight=user_info[3]
    height=user_info[4]
    gender=user_info[5]
    exercise=user_info[6]
    goal=user_info[7]
    weight2=user_info[8]
    bmr=calculate_basal_metabolic_rate(gender,weight2,height,age)
    kcal_need=calculate_daily_kcal_intake_need(bmr,exercise)
    kcal_goal=calorie_goal(kcal_need,goal)
    return math.floor(kcal_goal)

def calculate_body_mass_index(lst):
    username=lst[0]
    password=lst[1]
    db=sqlite3.connect("user_data.db")
    im=db.cursor()
    im.execute("""SELECT * FROM user_info where username=? and password=?""",(username,password))
    user_info=im.fetchone()
    height=user_info[4]
    weight2=user_info[8]
    bmi=weight2/(height/100)**2
    return math.floor(bmi)

def status(bmi):
    if bmi<15.0:
        return "Very Severely Underweight"
    if 15.0<=bmi<16.0:
        return "Severely Underweight"
    if 16.0<=bmi<18.5:
        return "Underweight"
    if 18.5<=bmi<25.0:
        return "Healthy Weight"
    if 25.0<=bmi<30.0:
        return "Overweight"
    if 30.0<=bmi<35.0:
        return "Moderately Obese"
    if 35.0<=bmi<40.0:
        return "Severely Obese"
    if bmi>=40.0:
        return "Very Severely Obese"

def database_call_food(searchword):
    food_list=[]
    db=sqlite3.connect("food_database.db")
    db.text_factory=str
    im=db.cursor()
    searchword2=searchword.upper()
    im.execute("""SELECT Food_Name FROM nut_data """)
    data=im.fetchall()
    for food in data:
        for food2 in food:
            if searchword2 in food2:
                food_list.append(food2)
    return food_list

def food_diary(user):
    lst=[]
    db=sqlite3.connect("user_data.db")
    im=db.cursor()

    now = time.localtime(time.time())
    year, month, day, hour, minute, second, weekday, yearday, daylight = now
    im.execute("""SELECT food_name,kcal,amount FROM user_info2 WHERE username=? and year=? and month=? and day=?""",(user,year,month,day))
    data=im.fetchall()
    for food_name,kcal,amount in data:
        a="Food Name: "+food_name+"\nTotal Kcal: "+str(kcal*amount)+"\nTotal Servings: "+str(amount)
        lst.append(a)
    return lst

