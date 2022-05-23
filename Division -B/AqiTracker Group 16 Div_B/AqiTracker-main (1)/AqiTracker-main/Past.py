from configparser import ConfigParser
from tkinter.font import BOLD
from turtle import width
import requests
import tkinter as tk
from tkinter import *
from tkinter import messagebox

root = tk.Tk()

root.title("AQI Tracker")
root.geometry("700x700")
root.configure(bg='light blue')

img = PhotoImage(file="sky.png")
label = Label(
    root,
    image=img
)
label.place(x=0, y=0,relwidth=1,relheight=1)


def nextPage1():
    root.destroy()
    import Mum5

def nextPage2():
    root.destroy()
    import Mum15

def nextPage3():
    root.destroy()
    import Mum30

def nextPage4():
    root.destroy()
    import Del5

def nextPage5():
    root.destroy()
    import Del15

def nextPage6():
    root.destroy()
    import Del30

def nextPage7():
    root.destroy()
    import Ahem5

def nextPage8():
    root.destroy()
    import Ahem15

def nextPage9():
    root.destroy()
    import Ahem30

cond =tk.Label(root,text="MUMBAI" ,font=('times new roman',20,BOLD),width = 180)
cond.place(x = -1300 , y= 50 , height= 120 )

cond1 =tk.Label(root,text="DELHI" ,font=('times new roman',20,BOLD),width = 180)
cond1.place(x = -1300 , y= 250 , height= 120 )

cond2 =tk.Label(root,text="AHMEDABAD" ,font=('times new roman',20,BOLD),width = 180)
cond2.place(x = -1300 , y= 450 , height= 120 )

backbutton= tk.Button(root, text='5', font=('times new roman',25,BOLD), bg='yellow',command=nextPage1 )
#submit.config(font=)
backbutton.place(x = 300 , y= 80 , width=100 , height=60)

backbutton= tk.Button(root, text='15', font=('times new roman',25,BOLD), bg='blue',command=nextPage2 )
#submit.config(font=)
backbutton.place(x = 440 , y= 80 , width=100 , height=60)

backbutton= tk.Button(root, text='30',font=('times new roman',25,BOLD), bg='red',command=nextPage3 )
#submit.config(font=)
backbutton.place(x = 580 , y= 80 , width=100 , height=60)

#delhi

backbutton= tk.Button(root, text='5', font=('times new roman',25,BOLD), bg='yellow',command=nextPage4 )
#submit.config(font=)
backbutton.place(x = 300 , y= 280 , width=100 , height=60)

backbutton= tk.Button(root, text='15', font=('times new roman',25,BOLD), bg='blue',command=nextPage5 )
#submit.config(font=)
backbutton.place(x = 440 , y= 280 , width=100 , height=60)

backbutton= tk.Button(root, text='30', font=('times new roman',25,BOLD), bg='red',command=nextPage6 )
#submit.config(font=)
backbutton.place(x = 580 , y= 280 , width=100 , height=60)

#ahemdabad

backbutton= tk.Button(root, text='5', font=('times new roman',25,BOLD),bg='yellow',command=nextPage7 )
#submit.config(font=)
backbutton.place(x = 300 , y= 480 , width=100 , height=60)

backbutton= tk.Button(root, text='15', font=('times new roman',25,BOLD),bg='blue' ,command=nextPage8)
#submit.config(font=)
backbutton.place(x = 440 , y= 480 , width=100 , height=60)

backbutton= tk.Button(root, text='30', font=('times new roman',25,BOLD), bg='red',command=nextPage9 )
#submit.config(font=)
backbutton.place(x = 580 , y= 480 , width=100 , height=60)

root.mainloop()