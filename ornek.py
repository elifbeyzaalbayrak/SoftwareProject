__author__ = 'elifalbayrak'
from Tkinter import *

rows = ["A few lines", "of text", "for our example"]
def callback(row):
    print "you picked row # %s which has this data: %s" % (row, rows[row])

rows = ["A few lines", "of text", "for our example"]
root = Tk()
t = Text(root)
t.pack()

t.insert(END, '\n'.join(rows))
for i in range(len(rows)):
    line_num = i + 1 # Tkinter text counts from 1, not zero
    tag_name = "tag_%s" % line_num
    t.tag_add(tag_name, "%s.0" % line_num, "%s.end" % line_num)
    t.tag_bind(tag_name, "<Button-1>", lambda e, row=i: callback(row))

root.mainloop()