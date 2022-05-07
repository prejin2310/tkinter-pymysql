import imp
from tkinter import *
import tkinter.messagebox
import tkinter
import pymysql
from PIL import ImageTk,Image
from subprocess import call
x=pymysql.connect(host='localhost',user='root',password='prejin2310',database='sample')

t=tkinter.Tk()
t.title('Registreation form') #rename the title of tkinter 
t.geometry('500x500') #adjust the width & height of tkinter GUI
#display text on tkinter

#setting background image
p=Image.open("E:\\Dev\\Python\\pymysql\\bg.png")
p=p.resize((500,500))
p=ImageTk.PhotoImage(p)
pic=tkinter.Label(image=p)
pic.place(x=0,y=0)



a=tkinter.Label(text="Profile Creation",font=('times new roman',27,'bold'))
a.place(x=110,y=0) 

b=tkinter.Label(text="Name :")
b.place(x=50,y=50)

c=tkinter.Entry(width=40)
c.place(x=130,y=50)

d=tkinter.Label(text="Place :")
d.place(x=50,y=100)

e=tkinter.Entry(width=40)
e.place(x=130,y=100)

def abcd():
    name=c.get() #get data from c entry field 
    place=e.get() #get data from e entry field 
    if(name=="" or place==""):
        tkinter.messagebox.showerror('error','Please fill all fields')
    else:
        cr=x.cursor()
        cr.execute('insert into profile values(%s,%s)',(name,place))
        x.commit() 
        x.close
        tkinter.messagebox.showinfo('tile of box','Data Submitted') #showerror,showwarning
        t.destroy()
         
        call(['python','next.py'])

f=tkinter.Button(text="Submit",width=30,command=abcd).place(x=150,y=150)
t.mainloop()
