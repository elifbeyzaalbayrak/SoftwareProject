__author__ = 'elifalbayrak'
from Tkinter import *
import tkMessageBox
import sqlite3
import time


def logInWindow():
    root.destroy()
    root2=Tk()
    root2.title("Log In")

    label_username=Label(root2,text="Enter User Name: ")
    label_password=Label(root2,text="Enter Password: ")

    username_entry=Entry(root2,width=30)
    password_entry=Entry(root2,width=30)

    login_button=Button(root2,text="Log In",width=30)

    label_username.grid(row=1,column=1)
    label_password.grid(row=2,column=1)
    username_entry.grid(row=1,column=2)
    password_entry.grid(row=2,column=2)
    login_button.grid(row=3,column=1,columnspan=2)


    root2.mainloop()

def newUserWindow():
    root.destroy()
    root3=Tk()
    root3.title("New User")

    select_username_lbl=Label(root3,text="User Name: ")
    select_password_lbl=Label(root3,text="Password: ")
    height_label=Label(root3,text="Height: ")
    weight_label=Label(root3,text="Weight: ")
    age_label=Label(root3,text="Age: ")
    goal_label=Label(root3,text="Select Goal: ")

    username_entry=Entry(root3,width=30)
    password_entry=Entry(root3,width=30)
    height_entry=Entry(root3,width=30)
    weight_entry=Entry(root3,width=30)
    age_entry=Entry(root3,width=30)

    radiovar=IntVar()

    rb1=Radiobutton(root3,text="Lose 1 kg per week",variable=radiovar,value=1)
    rb2=Radiobutton(root3,text="Lose 0.8 kg per week",variable=radiovar,value=2)
    rb3=Radiobutton(root3,text="Lose 0.5 kg per week",variable=radiovar,value=3)
    rb4=Radiobutton(root3,text="Lose 0.2 kg per week",variable=radiovar,value=4)
    rb5=Radiobutton(root3,text="Maintain your weight",variable=radiovar,value=5)
    rb6=Radiobutton(root3,text="Gain 0.2 kg per week",variable=radiovar,value=6)
    rb7=Radiobutton(root3,text="Gain 0.5 kg per week",variable=radiovar,value=7)
    rb8=Radiobutton(root3,text="Gain 0.8 kg per week",variable=radiovar,value=8)
    rb9=Radiobutton(root3,text="Gain 1 kg per week",variable=radiovar,value=9)



    select_username_lbl.grid(row=1,column=1)
    select_password_lbl.grid(row=2,column=1)
    height_label.grid(row=3,column=1)
    weight_label.grid(row=4,column=1)
    age_label.grid(row=5,column=1)
    goal_label.grid(row=6,column=1)

    username_entry.grid(row=1,column=2)
    password_entry.grid(row=2,column=2)
    height_entry.grid(row=3,column=2)
    weight_entry.grid(row=4,column=2)
    age_entry.grid(row=5,column=2)

    rb1.grid(row=6,column=2)
    rb2.grid(row=7,column=2)
    rb3.grid(row=8,column=2)
    rb4.grid(row=9,column=2)
    rb5.grid(row=10,column=2)
    rb6.grid(row=11,column=2)
    rb7.grid(row=12,column=2)
    rb8.grid(row=13,column=2)
    rb9.grid(row=14,column=2)


    def add_to_database():
        db=sqlite3.connect("user_data.db")
        if username_entry.get()=="" or password_entry.get()=="" or\
            height_entry.get()=="" or weight_entry.get()=="" or \
            age_entry.get()=="": tkMessageBox.showerror("Error","Please fill in the\n required fields")

        im=db.cursor()
        user=username_entry.get()
        password=password_entry.get()
        height=float(height_entry.get())
        weight=float(weight_entry.get())
        age=int(age_entry.get())
        goal=radiovar.get()
        weight2=weight
        data=(user,password,age,weight,height,goal,weight2)
        im.execute("""INSERT INTO user_info VALUES (?,?,?,?,?,?,?)""",data)
        im.close()
        db.commit()
        db.close()
        root3.destroy()
        welcome_window()



    sign_up_button=Button(root3,text="Sign Up",width=30,command=add_to_database)
    sign_up_button.grid(row=15,column=1,columnspan=2)

    root3.mainloop()


def welcome_window():
    root4=Tk()
    root4.mainloop()

root=Tk()
root.title("LogIn")
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