__author__ = 'elifalbayrak'

import sqlite3
import math
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
    return kcal_goal

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
    return bmi

def status(bmi):
    if bmi<18.5:
        return "Underweight"
    if 18.5<=bmi<=22.9:
        return "Normal Weight"
    if 23.0<=bmi<=24.9:
        return "At Risk Overweight"
    if 25.0<=bmi<=29.9:
        return "Moderately Obese"
    if bmi>=30.0:
        return "Severely Obese"
