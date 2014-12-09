__author__ = 'elifalbayrak'
from Tkinter import *

root = Tk()
root.geometry("600x500+10+10")

def PrintIt():
    label=Label(content,text="olmuyo")
    label.grid(column=1,row=3,sticky="we")



content = Frame(root)
ok = Button(content,text="Okay",command=PrintIt,width=15)
#cancel = Button(content,text="Cancel",command=root.destroy(),width=15)

content.grid(column=0,row=0)
ok.grid(column=1,row=2,sticky="we")
#cancel.grid(column=1,row=3,sticky="we")






root.mainloop()