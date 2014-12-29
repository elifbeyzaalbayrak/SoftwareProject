__author__ = 'elifalbayrak'
from Tkinter import *
import tkMessageBox
from functions import *

userlst=[]

def logInWindow():
    root2=Tk()
    root2.geometry("+200+100")
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

    def back():
        root2.destroy()
        first_window()


    login_button=Button(root2,text="Log In",width=30,command=check_user_info)
    login_button.grid(row=3,column=1,columnspan=2)
    back_button=Button(root2,text="<< Back",width=30,command=back)
    back_button.grid(row=4,column=1,columnspan=2)


    root2.mainloop()

def newUserWindow():
    root3=Tk()
    root3.title("New User")
    root3.geometry("+200+100")

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


    def back():
        root3.destroy()
        first_window()

    sign_up_button=Button(root3,text="Sign Up",width=30,command=add_to_database)
    sign_up_button.grid(row=22,column=1,columnspan=2)
    back_button=Button(root3,text="<< Back",width=30,command=back)
    back_button.grid(row=23,column=1,columnspan=2)

    root3.mainloop()

def update_weight():
    root5=Tk()
    root5.geometry("+200+100")
    root5.title("Update Weight")
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

    def back():
        root5.destroy()
        welcome_window()

    update_button=Button(root5,width=30,command=update,text="Update")
    update_button.grid(row=2,column=1,columnspan=2)
    back_button=Button(root5,width=30,command=back,text="<< Back")
    back_button.grid(row=3,column=1,columnspan=2)

def change():
    master = Tk()
    master.geometry("+200+100")
    master.title("Change Goal")
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

    def back():
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
    back_button=Button(master,text="<< Back",width=30,command=back)
    back_button.grid(row=11,column=1,columnspan=2)

    mainloop()

def diary():
    user=userlst[0]
    food_di=food_diary(user)
    func_diary(food_di,welcome_window)

def quick_food_add():

    master=Tk()
    master.title("Quick Add")
    master.geometry("+200+100")
    kcal_label=Label(master,text="Kcal (Required): ")
    food_name_label=Label(master,text="Food Name (Required): ")

    fat_label=Label(master,text="Fat (Optional): ")
    carb_label=Label(master,text="Carbs (Optional): ")
    protein_label=Label(master,text="Protein (Optional): ")
    quantity_label=Label(master,text="Quantity (Required): ")

    kcal_entry=Entry(master,width=30)
    food_name_entry=Entry(master,width=30)
    fat_entry=Entry(master,width=30)
    carb_entry=Entry(master,width=30)
    protein_entry=Entry(master,width=30)
    quantity_entry=Entry(master,width=30)

    kcal_label.grid(row=2,column=1)
    kcal_entry.grid(row=2,column=2)
    food_name_label.grid(row=1,column=1)
    food_name_entry.grid(row=1,column=2)
    fat_label.grid(row=3,column=1)
    fat_entry.grid(row=3,column=2)
    carb_label.grid(row=4,column=1)
    carb_entry.grid(row=4,column=2)
    protein_label.grid(row=5,column=1)
    protein_entry.grid(row=5,column=2)
    quantity_label.grid(row=6,column=1)
    quantity_entry.grid(row=6,column=2)

    def add():
        user=userlst[0]
        now = time.localtime(time.time())
        year, month, day, hour, minute, second, weekday, yearday, daylight = now
        food_name=food_name_entry.get()
        kcal=float(kcal_entry.get())
        if fat_entry.get()=="":
            fat=0
        else:
            fat=float(fat_entry.get())
        if carb_entry.get()=="":
            carbs=0
        else:
            carbs=float(carb_entry.get())
        if protein_entry.get()=="":
            protein=0
        else:
            protein=float(protein_entry.get())
        amount=float(quantity_entry.get())
        weight2=userlst[2]
        data=(user,weight2,year,month,day,food_name.upper(),kcal,carbs,protein,fat,amount)
        db=sqlite3.connect("user_data.db")
        db2=sqlite3.connect("food_database.db")
        im=db.cursor()
        im2=db2.cursor()
        im.execute("""INSERT INTO user_info2 VALUES (?,?,?,?,?,?,?,?,?,?,?)""",data)
        im2.execute("""INSERT INTO nut_data VALUES (?,?,?,?,?,?)""",(food_name.upper(),kcal,protein,fat,carbs,""))
        im2.close()
        im.close()
        db.commit()
        db2.commit()
        db.close()
        db2.close()
        master.destroy()
        welcome_window()

    def back():
        master.destroy()
        welcome_window()


    add_button=Button(master,text="Add",width=60,command=add)
    add_button.grid(row=7,column=1,columnspan=2)
    back_button=Button(master,text="<< Back", width=60,command=back)
    back_button.grid(row=8,column=1,columnspan=2)

    master.mainloop()

def add_food():
    master=Tk()
    master.geometry("+200+100")
    master.title("Add Food")
    search_food_label=Label(master,text="Search Food: ")
    search_food_entry=Entry(master,width=30)

    def back():
        master.destroy()
        welcome_window()

    def search():
        selection_index=[]
        master2=Tk()
        master2.title("Search Food")
        master2.geometry("+200+100")
        frame=Frame(master2)
        frame2=Frame(master2)
        search_word=search_food_entry.get()
        searchresult=database_call_food(search_word)
        sb=Scrollbar(frame,orient=VERTICAL)

        listbox=Listbox(frame,selectmode=SINGLE,yscrollcommand=sb.set,width=100)
        sb.config(command=listbox.yview)

        for item in searchresult:
            listbox.insert(END,item)


        def listbox_click(z):
                value=listbox.curselection()
                selection_index.append(int(value[0]))

        def select():
            master2.destroy()
            master3=Tk()
            master3.geometry("+200+100")
            master3.title("Selection")
            db=sqlite3.connect("food_database.db")
            im=db.cursor()
            selection=selection_index[len(selection_index)-1]
            selection_name=searchresult[selection]
            im.execute("""SELECT * FROM nut_data WHERE Food_Name=?""",(selection_name,))
            data=im.fetchall()



            for i in data:
                name_label=Label(master3,text="Food Name: "+str(i[0]))
                calorie_label=Label(master3,text="Kcal per serving: "+str(i[1]))
                protein_label=Label(master3,text="Protein: "+str(i[2]))
                fat_label=Label(master3,text="Fat: "+str(i[3]))
                carb_label=Label(master3,text="Carbs: "+str(i[4]))
                serving_size_label=Label(master3,text="Serving Size: "+str(i[5]))
                quantity_label=Label(master3,text="Quantity: ")
                quantity_entry=Entry(master3,width=10)


                name_label.grid(row=1,column=1,columnspan=2)
                calorie_label.grid(row=2,column=1,columnspan=2)
                protein_label.grid(row=3,column=1,columnspan=2)
                fat_label.grid(row=4,column=1,columnspan=2)
                carb_label.grid(row=5,column=1,columnspan=2)
                serving_size_label.grid(row=6,column=1,columnspan=2)
                quantity_label.grid(row=7,column=1)
                quantity_entry.grid(row=7,column=2)
            def ate_this():
                db2=sqlite3.connect("user_data.db")
                im2=db2.cursor()
                now = time.localtime(time.time())
                year, month, day, hour, minute, second, weekday, yearday, daylight = now
                user=userlst[0]
                weight2=userlst[2]
                amount=float(quantity_entry.get())
                for a in data:
                    food_name=a[0]
                    kcal=a[1]
                    protein=a[2]
                    fat=a[3]
                    carbs=a[4]
                    im2.execute("""INSERT INTO user_info2 VALUES (?,?,?,?,?,?,?,?,?,?,?) """,(user,weight2,year,month,day,food_name,kcal,carbs,protein,fat,amount))
                    db2.commit()
                    im2.close()
                    db2.close()
                master3.destroy()

            ate_this_button=Button(master3,width=60,text="I Ate this!",command=ate_this)
            ate_this_button.grid(row=8,column=1,columnspan=2)


        listbox.pack(side=LEFT,fill=BOTH,expand=1)
        sb.pack(side=RIGHT,fill=Y)
        listbox.bind("<ButtonRelease-1>",listbox_click)

        select_button=Button(frame2,width=30,text="Select",command=select)
        frame.grid(row=0,column=0)
        frame2.grid(row=0,column=5)
        select_button.grid(row=1,column=1)




    search_food_button=Button(master,width=30,text="Search",command=search)
    back_button=Button(master,text="<< Back",width=30,command=back)
    search_food_label.grid(row=1,column=1)
    search_food_entry.grid(row=1,column=2)
    search_food_button.grid(row=2,column=1,columnspan=2)
    back_button.grid(row=3,column=1,columnspan=2)

def welcome_window():
    db=sqlite3.connect("user_data.db")
    im=db.cursor()
    im2=db.cursor()

    user=userlst[0]
    calorie_consumed=[]
    fat_consumed=[]
    protein_consumed=[]
    carbs_consumed=[]
    im.execute("""SELECT * FROM  user_info WHERE username=?""",(user,))
    now = time.localtime(time.time())
    year, month, day, hour, minute, second, weekday, yearday, daylight = now
    im2.execute("""SELECT kcal,carbs,protein,fat,amount FROM user_info2 WHERE username=? and year=? and month=? and day=? """,(user,year,month,day))
    data=im.fetchone()
    data2=im2.fetchall()
    for i in data2:
        total_kcal=i[0]*i[4]
        total_carbs=i[1]*i[4]
        total_protein=i[2]*i[4]
        total_fat=i[3]*i[4]
        calorie_consumed.append(total_kcal)
        fat_consumed.append(total_fat)
        protein_consumed.append(total_protein)
        carbs_consumed.append(total_carbs)

    userlst.append(data[8])
    weight_lost=data[3]-data[8]

    root4=Tk()
    root4.title("Calorie Counter")
    root4.geometry("+200+100")

    kcal_goal=user_calorie_goal(userlst)
    bmi=calculate_body_mass_index(userlst)
    user_state=status(bmi)
    kcal_consumed=sum(calorie_consumed)
    kcal_left=kcal_goal-sum(calorie_consumed)

    def update_w():
        root4.destroy()
        update_weight()

    def change_goal():
        root4.destroy()
        change()

    def quick_add():
        root4.destroy()
        quick_food_add()

    def add_food_command():
        root4.destroy()
        add_food()

    def diary_command():
        root4.destroy()
        diary()

    kcal_goal_label=Label(root4,text="Recommended daily kcal intake: ")
    kcal_goal_label2=Label(root4,text=str(kcal_goal)+" kcal")
    user_state_label=Label(root4,text="BMI: ")
    user_state_label2=Label(root4,text=str(bmi)+" ("+user_state+")")
    calorie_consumed_label=Label(root4,text="Calorie Consumed: ")
    calorie_consumed_label2=Label(root4,text=str(kcal_consumed)+" kcal")
    calorie_left_label=Label(root4,text="Calorie Left: ")
    calorie_left_label2=Label(root4,text=str(kcal_left)+" kcal")
    weight_lost_label=Label(root4,text="Weight Lost: ")
    weight_lost_label2=Label(root4,text=str(weight_lost)+" kg")
    current_weight_label=Label(root4,text="Current Weight: ")
    current_weight_label2=Label(root4,text=str(data[8])+" kg")
    fat_label=Label(root4,text="Fat Consumed: ")
    fat_label2=Label(root4,text=str((math.floor(sum(fat_consumed))))+" g")
    carb_label=Label(root4,text="Carbs Consumed: ")
    carb_label2=Label(root4,text=str((math.floor(sum(carbs_consumed))))+" g")
    protein_label=Label(root4,text="Protein Consumed: ")
    protein_label2=Label(root4,text=str((math.floor(sum(protein_consumed))))+" g")

    update_weight_button=Button(root4,text="Update Weight",width=40,command=update_w)
    change_goal_button=Button(root4,text="Change Goal",width=40,command=change_goal)
    add_food_button=Button(root4,text="Add Food",width=40,command=add_food_command)
    quick_add_button=Button(root4,text="Quick Food",width=40,command=quick_add)
    diary_button=Button(root4,text="Diary",width=40,command=diary_command)
    exit_button=Button(root4,text="Exit",command=root4.destroy,width=40)
    blank=Label(root4)

    kcal_goal_label.grid(row=1,column=1)
    kcal_goal_label2.grid(row=1,column=2)
    user_state_label.grid(row=2,column=1)
    user_state_label2.grid(row=2,column=2)
    calorie_consumed_label.grid(row=5,column=1)
    calorie_consumed_label2.grid(row=5,column=2)
    calorie_left_label.grid(row=6,column=1)
    calorie_left_label2.grid(row=6,column=2)
    weight_lost_label2.grid(row=4,column=2)
    weight_lost_label.grid(row=4,column=1)
    current_weight_label.grid(row=3,column=1)
    current_weight_label2.grid(row=3,column=2)
    carb_label.grid(row=8,column=1)
    carb_label2.grid(row=8,column=2)
    fat_label.grid(row=9,column=1)
    fat_label2.grid(row=9,column=2)
    protein_label.grid(row=10,column=1)
    protein_label2.grid(row=10,column=2)
    blank.grid(row=11,column=1)
    update_weight_button.grid(row=12,column=1,columnspan=2)
    change_goal_button.grid(row=13,column=1,columnspan=2)
    add_food_button.grid(row=14,column=1,columnspan=2)
    quick_add_button.grid(row=15,column=1,columnspan=2)
    diary_button.grid(row=16,column=1,columnspan=2)
    exit_button.grid(row=17,column=1,columnspan=2)

    root4.mainloop()

def first_window():
    root=Tk()
    root.geometry("+200+100")
    root.title("Log In or Register")
    content=Frame(root)

    def log_in():
        root.destroy()
        logInWindow()

    def new_user():
        root.destroy()
        newUserWindow()

    login=Button(content,text="Log In",command=log_in,width=15)
    newuser=Button(content,text="New User",command=new_user,width=15)
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

first_window()
