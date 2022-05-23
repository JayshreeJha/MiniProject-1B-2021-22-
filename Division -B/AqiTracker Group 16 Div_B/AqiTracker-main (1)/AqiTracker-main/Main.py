from tkinter import *

from tkinter.ttk import *
import tkinter as tk
import datetime as dt
from tkinter import *
from time import strftime
root = tk.Tk()

x = dt.datetime.now()

print(x.strftime("%A"))

root.title("AQI Tracker")
root.geometry("700x700")
root.configure(bg='light blue') 

img = PhotoImage(file="sky.png")
label = Label(
    root,
    image=img
)
label.place(x=0, y=0,relwidth=1,relheight=1)

def time():

    string = strftime('%H:%M:%S %p')

    lbl.config(text = string)

    lbl.after(1000, time)

def nextPage():
    root.destroy()
    import Aqi

def prevPage():
    root.destroy()
    import WeatherApp_withicons

def ezPage():
    root.destroy()
    import Past


button1 = tk.Button(root,text='AQI',fg='black',font=('times new roman',18),width=8, command=nextPage)
button1.place(x = 100 , y= 250 , width=200 , height=60)

button2 = tk.Button(root,text='WEATHER',fg='black',font=('times new roman',18),width=8, command=prevPage)
button2.place(x = 400 , y= 250 , width=200 , height=60)

button3 = tk.Button(root,text='HISTORY',fg='black',font=('times new roman',18),width=8, command=ezPage)
button3.place(x = 250 , y= 350 , width=200 , height=60)

lbl = Label(root, font = ('times new roman', 30, 'bold'),

             background = 'light blue',

            foreground = 'black')
lbl.pack(anchor = 'center')
time()
        

date = tk.Label(root,text=f"{x:%d : %B : %Y : %A  }"   ,fg = "black",bg="light blue", font=('times new roman',18),width=60)
date.pack(anchor='center')
date.place(x = 0 , y= 660 )


root.mainloop()