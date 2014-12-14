__author__ = 'elifalbayrak'
from Tkinter import *
import tkMessageBox
import sqlite3
import time
from calculators import *

userlst=[]

def logInWindow():
    root.destroy()
    root2=Tk()
    root2.title("Log In")

    label_username=Label(root2,text="Enter User Name: ")
    label_password=Label(root2,text="Enter Password: ")

    username_entry=Entry(root2,width=30)
    password_entry=Entry(root2,width=30,show="*")

    label_username.grid(row=1,column=1)
    label_password.grid(row=2,column=1)
    username_entry.grid(row=1,column=2)
    password_entry.grid(row=2,column=2)



    def check_user_info():
        username=username_entry.get()
        password=password_entry.get()
        db=sqlite3.connect("user_data.db")
        im=db.cursor()
        im.execute("""SELECT * FROM user_info where username = ? AND password = ?""",(username,password))
        data=im.fetchone()
        if data==None:
            tkMessageBox.showerror("Error!","User Name or Password is wrong!")
        else:
            tkMessageBox.showinfo("Welcome!","Welcome Back!")
            userlst.append(username)
            userlst.append(password)
            root2.destroy()
            welcome_window()


    login_button=Button(root2,text="Log In",width=30,command=check_user_info)
    login_button.grid(row=3,column=1,columnspan=2)


    root2.mainloop()

def newUserWindow():
    root.destroy()
    root3=Tk()
    root3.title("New User")

    select_username_lbl=Label(root3,text="User Name: ")
    select_password_lbl=Label(root3,text="Password: ")
    height_label=Label(root3,text="Height(cm): ")
    weight_label=Label(root3,text="Weight(kg): ")
    age_label=Label(root3,text="Age: ")
    goal_label=Label(root3,text="Select Goal: ")
    gender_label=Label(root3,text="Gender: ")
    exercise_label=Label(root3,text="Exercise Intencity: ")

    username_entry=Entry(root3,width=30)
    password_entry=Entry(root3,width=30,show="*")
    height_entry=Entry(root3,width=30)
    weight_entry=Entry(root3,width=30)
    age_entry=Entry(root3,width=30)

    radiovar=IntVar()
    radiovar2=IntVar()
    radiovar3=IntVar()

    rb1=Radiobutton(root3,text="Lose 1 kg per week",variable=radiovar,value=1)
    rb2=Radiobutton(root3,text="Lose 0.8 kg per week",variable=radiovar,value=2)
    rb3=Radiobutton(root3,text="Lose 0.5 kg per week",variable=radiovar,value=3)
    rb4=Radiobutton(root3,text="Lose 0.2 kg per week",variable=radiovar,value=4)
    rb5=Radiobutton(root3,text="Maintain your weight",variable=radiovar,value=5)
    rb6=Radiobutton(root3,text="Gain 0.2 kg per week",variable=radiovar,value=6)
    rb7=Radiobutton(root3,text="Gain 0.5 kg per week",variable=radiovar,value=7)
    rb8=Radiobutton(root3,text="Gain 0.8 kg per week",variable=radiovar,value=8)
    rb9=Radiobutton(root3,text="Gain 1 kg per week",variable=radiovar,value=9)

    rb10=Radiobutton(root3,text="Male",variable=radiovar2,value=1)
    rb11=Radiobutton(root3,text="Female",variable=radiovar2,value=2)

    rb12=Radiobutton(root3,text="Little to no exercise",variable=radiovar3,value=1)
    rb13=Radiobutton(root3,text="Light exercise (1-3 days per week)",variable=radiovar3,value=2)
    rb14=Radiobutton(root3,text="Moderate exercise (3-5 days per week)",variable=radiovar3,value=3)
    rb15=Radiobutton(root3,text="Heavy exercise (6-7 days per week)", variable=radiovar3,value=4)
    rb16=Radiobutton(root3,text="Very heavy exercise (twice per day, extra heavy workuts)", variable=radiovar3,value=5)

    select_username_lbl.grid(row=1,column=1)
    select_password_lbl.grid(row=2,column=1)
    height_label.grid(row=3,column=1)
    weight_label.grid(row=4,column=1)
    age_label.grid(row=5,column=1)
    gender_label.grid(row=6,column=1)
    exercise_label.grid(row=8,column=1)
    goal_label.grid(row=13,column=1)


    username_entry.grid(row=1,column=2)
    password_entry.grid(row=2,column=2)
    height_entry.grid(row=3,column=2)
    weight_entry.grid(row=4,column=2)
    age_entry.grid(row=5,column=2)

    rb10.grid(row=6,column=2)
    rb11.grid(row=7,column=2)

    rb12.grid(row=8,column=2)
    rb13.grid(row=9,column=2)
    rb14.grid(row=10,column=2)
    rb15.grid(row=11,column=2)
    rb16.grid(row=12,column=2)

    rb1.grid(row=13,column=2)
    rb2.grid(row=14,column=2)
    rb3.grid(row=15,column=2)
    rb4.grid(row=16,column=2)
    rb5.grid(row=17,column=2)
    rb6.grid(row=18,column=2)
    rb7.grid(row=19,column=2)
    rb8.grid(row=20,column=2)
    rb9.grid(row=21,column=2)


    def add_to_database():
        db=sqlite3.connect("user_data.db")
        if username_entry.get()=="" or password_entry.get()=="" or\
            height_entry.get()=="" or weight_entry.get()=="" or \
            age_entry.get()=="" or radiovar.get()==0 or radiovar2.get()==0 or radiovar3.get()==0:
                tkMessageBox.showerror("Error","Please fill in the\n required fields")
        else:
            im=db.cursor()
            user=username_entry.get()
            im.execute("""SELECT * FROM user_info where username=?""",(user,))
            check=im.fetchone()
            if check!=None:
                tkMessageBox.showerror("Error!","Username already exists")
            else:
                password=password_entry.get()
                height=float(height_entry.get())
                weight=float(weight_entry.get())
                age=int(age_entry.get())
                exercise=radiovar3.get()
                goal=radiovar.get()
                weight2=weight
                gender=radiovar2.get()
                userlst.append(user)
                userlst.append(password)
                data=(user,password,age,weight,height,gender,exercise,goal,weight2)
                im.execute("""INSERT INTO user_info VALUES (?,?,?,?,?,?,?,?,?)""",data)
                im.close()
                db.commit()
                db.close()
                root3.destroy()
                welcome_window()



    sign_up_button=Button(root3,text="Sign Up",width=30,command=add_to_database)
    sign_up_button.grid(row=22,column=1,columnspan=2)

    root3.mainloop()

def update_weight():
    root5=Tk()
    update_weight_label=Label(root5,text="Update Weight: ")
    weight_entry=Entry(root5,width=15)
    update_weight_label.grid(row=1,column=1)
    weight_entry.grid(row=1,column=2)

    def update():
        weight=weight_entry.get()
        weight2=float(weight)
        user=userlst[0]
        db=sqlite3.connect("user_data.db")
        im=db.cursor()
        im.execute("""UPDATE user_info SET weight2=? where username=?""",(weight2,user))
        im.close()
        db.commit()
        db.close()
        root5.destroy()
        welcome_window()

    update_button=Button(root5,width=30,command=update,text="Update")
    update_button.grid(row=2,column=1,columnspan=2)

def change():
    master = Tk()
    v = IntVar()

    def readrbutton():
        value=v.get()
        user = userlst[0]
        db=sqlite3.connect("user_data.db")
        im=db.cursor()
        im.execute("""UPDATE user_info SET goal=? where username=?""",(value,user))
        db.commit()
        master.destroy()
        welcome_window()

    a=Radiobutton(master, text="Lose 1 kg per week", variable=v, value=1)
    b=Radiobutton(master, text="Lose 0.8 kg per week", variable=v, value=2)
    c=Radiobutton(master, text="Lose 0.5 kg per week", variable=v, value=3)
    d=Radiobutton(master, text="Lose 0.2 kg per week", variable=v, value=4)
    e=Radiobutton(master, text="Maintain your weight", variable=v, value=5)
    f=Radiobutton(master, text="Gain 0.2 kg per week", variable=v, value=6)
    g=Radiobutton(master, text="Gain 0.5 kg per week", variable=v, value=7)
    h=Radiobutton(master, text="Gain 0.8 kg per week", variable=v, value=8)
    i=Radiobutton(master, text="Gain 1 kg per week", variable=v, value=9)

    a.grid(row=1,column=1)
    b.grid(row=2,column=1)
    c.grid(row=3,column=1)
    d.grid(row=4,column=1)
    e.grid(row=5,column=1)
    f.grid(row=6,column=1)
    g.grid(row=7,column=1)
    h.grid(row=8,column=1)
    i.grid(row=9,column=1)

    update_button=Button(master,text="Update",width=30,command=readrbutton)
    update_button.grid(row=10,column=1,columnspan=2)

    mainloop()

def quick_add_calorie():

    master=Tk()
    kcal_label=Label(master,text="Kcal: ")
    food_name=Label(master,text="Food Name: ")

    kcal_entry=Entry(master,width=30)
    food_name_entry=Entry(master,width=30)

    kcal_label.grid(row=2,column=1)
    kcal_entry.grid(row=2,column=2)
    food_name.grid(row=1,column=1)
    food_name_entry.grid(row=1,column=2)

    def add():
        user=userlst[0]
        now = time.localtime(time.time())
        year, month, day, hour, minute, second, weekday, yearday, daylight = now
        kcal=float(kcal_entry.get())
        carbs=0
        protein=0
        fat=0
        amount=1
        weight2=userlst[2]
        data=(user,weight2,year,month,day,kcal,carbs,protein,fat,amount)
        db=sqlite3.connect("user_data.db")
        im=db.cursor()
        im.execute("""INSERT INTO user_info2 VALUES (?,?,?,?,?,?,?,?,?,?)""",data)
        im.close()
        db.commit()
        db.close()
        master.destroy()
        welcome_window()


    add_button=Button(master,text="Add",width=60,command=add)
    add_button.grid(row=3,column=1,columnspan=2)
    master.mainloop()

def welcome_window():
    db=sqlite3.connect("user_data.db")
    im=db.cursor()
    user=userlst[0]
    im.execute("""SELECT * FROM  user_info WHERE username=?""",(user,))
    data=im.fetchone()
    userlst.append(data[8])
    weight_lost=data[3]-data[8]
    root4=Tk()
    root4.title("Calorie Counter")

    kcal_goal=user_calorie_goal(userlst)
    bmi=calculate_body_mass_index(userlst)
    user_state=status(bmi)

    def update_w():
        root4.destroy()
        update_weight()

    def change_goal():
        root4.destroy()
        change()

    def quick_add():
        root4.destroy()
        quick_add_calorie()

    kcal_goal_label=Label(root4,text="Recommended daily kcal intake: ")
    kcal_goal_label2=Label(root4,text=str(kcal_goal)+"kcal")
    user_state_label=Label(root4,text="BMI: "+str(bmi)+" ("+user_state+")")
    calorie_left_label=Label(root4,text="Calorie Left: ")
    calorie_left_label2=Label(root4,text=str(kcal_goal)+"kcal")

    weight_lost_label=Label(root4,text="Weight Lost: ")
    weight_lost_label2=Label(root4,text=str(weight_lost))
    update_weight_button=Button(root4,text="Update Weight",width=30,command=update_w)
    change_goal_button=Button(root4,text="Change Goal",width=30,command=change_goal)
    add_food_button=Button(root4,text="Add Food",width=30)
    quick_add_button=Button(root4,text="Quick-Add Calories",width=30,command=quick_add)
    exit_button=Button(root4,text="Exit",command=root4.destroy,width=30)

    kcal_goal_label.grid(row=1,column=1)
    kcal_goal_label2.grid(row=1,column=2)
    user_state_label.grid(row=2,column=1,columnspan=2)
    calorie_left_label.grid(row=3,column=1)
    calorie_left_label2.grid(row=3,column=2)
    weight_lost_label2.grid(row=4,column=2)
    weight_lost_label.grid(row=4,column=1)
    update_weight_button.grid(row=1,column=3)
    change_goal_button.grid(row=2,column=3)
    add_food_button.grid(row=3,column=3)
    quick_add_button.grid(row=4,column=3)
    exit_button.grid(row=5,column=1,columnspan=3)

    root4.mainloop()

root=Tk()
root.title("Log In or Register")

content=Frame(root)
login=Button(content,text="Log In",command=logInWindow,width=15)
newuser=Button(content,text="New User",command=newUserWindow,width=15)
loginlbl=Label(content,text="Select")
orlbl=Label(content,text="Or")
exit_button=Button(content,text="Exit",command=root.destroy,width=15)
content.grid(row=0,column=0)
loginlbl.grid(row=1,column=1,columnspan=2)
login.grid(row=2,column=1)
newuser.grid(row=2,column=2)
orlbl.grid(row=3,column=1,columnspan=2)
exit_button.grid(row=4,column=1,columnspan=2)
root.mainloop()

