from tkinter.font import BOLD
from turtle import width
import requests
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from database import *

class Table:
    
    def __init__(self,root):
        
        # code for creating table
        for i in range(total_rows):
            for j in range(total_columns):                 
                self.e = Entry(root, width=20, fg='black',font=('Times new Roman',18,'bold'))
                if(row < 150):
                    self.e = Entry(root, width=20, fg='red',font=('Times new Roman',18,'bold'))           
                self.e.grid(row=i, column=j)
                self.e.insert(END, lst[i][j])
 
# take the data

cursor.execute("SELECT `City`, `Date`, `AQI`, `Weather` FROM `aqi_data` WHERE City = 'Mumbai'")
record = cursor.fetchmany(5)
print("Total number of rows in table:", cursor.rowcount)
lst = [] 

for row in record:
    lst.append((row[0],row[1],row[2],row[3]))
    total_rows = len(lst)
    total_columns = len(lst[0])
    row = int(row[2])
    
  
# create root window
root = Tk()
t = Table(root)
root.title("5 days Data")
root.mainloop()