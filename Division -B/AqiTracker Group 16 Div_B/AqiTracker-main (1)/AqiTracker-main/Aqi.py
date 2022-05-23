from configparser import ConfigParser
from tkinter import font
from tkinter.font import BOLD
from turtle import width
import requests
import matplotlib.pyplot as plt 
import tkinter as tk
from tkinter import *
from tkinter import messagebox

root = tk.Tk()

root.title("AQI Tracker")
root.geometry("900x700")
root.configure(bg='light blue')
name_var = tk.StringVar()

img = PhotoImage(file="sky.png")
label = Label(
    root,
    image=img
)
label.place(x=0, y=0,relwidth=1,relheight=1)

def piebutton():

        city = textbox1.get()
        level = []
        key='37f96394ffe8b6cca1110af3d8270604c711c688'
        url='http://api.waqi.info/feed/' + city + '/?token='
        main_url = url + key  # Main URL
        r = requests.get(main_url)  # Accessing the URL
        data = r.json()['data']  # Fetching data in variable
        aqi = data['aqi']  # Air quality Index    
        air_label['text'] = aqi
        iaqi = data['iaqi']  # Individual Air Quality Index
        del iaqi['p']  # Deleting unused information

        temperature = iaqi.get('t', 'Not Available')
        humidity = iaqi.get('h', 'Not Available')
        dew = iaqi.get('dew', 'Not Available')
        no2 = iaqi.get('no2', 'Not Available')
        o3 = iaqi.get('o3', 'Not Available')
        so2 = iaqi.get('so2', 'Not Available')
        pm10 = iaqi.get('pm10', 'Not Available')
        pm25 = iaqi.get('pm25', 'Not Available')

        list1.insert(1, f'{city.upper()} AQI :{aqi} µg/m³')
        list1.insert(2, 'Individual Air quality')
        list1.insert(3, f'Dew :{dew}')
        list1.insert(4, f'NO2 :{no2} µg/m³')
        list1.insert(5, f'Ozone :{o3} µg/m³')
        list1.insert(6, f'Sulphur :{so2} µg/m³')
        degree_sign = u"\N{DEGREE SIGN}"
        list1.insert(7, f'Temperature :{temperature} {degree_sign}C ')
        list1.insert(8, f'Humidity :{humidity} g/kg')
        list1.insert(9, f'pm10 :{pm10}g/m³')
        list1.insert(10, f'pm25 :{pm25}g/m³')
        pollutants = [i for i in iaqi]
        values = [i['v'] for i in iaqi.values()]

    # Exploding the first slice
        explode = [0 for i in pollutants]
        mx = values.index(max(values))  # explode 1st slice
        explode[mx] = 0.1

        plt.figure(figsize=(8, 6))  # Size of the figure
        plt.pie(values, labels=pollutants, explode=explode, autopct='%1.1f%%', shadow=True)

        plt.title('Air pollutants and their probable amount in atmosphere of {} and the pollution level is {}'.format(city.upper(), level))  # Title of Pie-Chart
        
        plt.axis('equal')
        plt.show()  # Showing the Pie-Chart
        name_var.set("")


def get_aqi(city):
    try:
        city = textbox1.get()
        key='37f96394ffe8b6cca1110af3d8270604c711c688'
        url='http://api.waqi.info/feed/' + city + '/?token='
        main_url = url + key  # Main URL
        r = requests.get(main_url)  # Accessing the URL
        data = r.json()['data']  # Fetching data in variable
        aqi = data['aqi']  # Air quality Index    
        air_label['text'] = aqi
        iaqi = data['iaqi']  # Individual Air Quality Index
        del iaqi['p']  # Deleting unused information

        temperature = iaqi.get('t', 'Not Available')
        humidity = iaqi.get('h', 'Not Available')
        dew = iaqi.get('dew', 'Not Available')
        no2 = iaqi.get('no2', 'Not Available')
        o3 = iaqi.get('o3', 'Not Available')
        so2 = iaqi.get('so2', 'Not Available')
        pm10 = iaqi.get('pm10', 'Not Available')
        pm25 = iaqi.get('pm25', 'Not Available')

        list1.insert(1, f'{city.upper()} AQI :{aqi} µg/m³')
        list1.insert(2, 'Individual Air quality')
        list1.insert(3, f'Dew :{dew}')
        list1.insert(4, f'NO2 :{no2} µg/m³')
        list1.insert(5, f'Ozone :{o3} µg/m³')
        list1.insert(6, f'Sulphur :{so2} µg/m³')
        degree_sign = u"\N{DEGREE SIGN}"
        list1.insert(7, f'Temperature :{temperature} {degree_sign}C ')
        list1.insert(8, f'Humidity :{humidity} g/kg')
        list1.insert(9, f'pm10 :{pm10}g/m³')
        list1.insert(10, f'pm25 :{pm25}g/m³')
    except:
        messagebox.showerror("AQI", "Data not available sorry")
        #hellow =tk.Label(root,text="Data not available sorry",fg ="black" ,font=('times new roman',18,BOLD),width=500)
        #hellow.place(x = 300 , y= 500 , width=150 , height=50)

    if (aqi < 50):
        condition =tk.Label(root,text="Good",bg = "green" ,font=('times new roman',18,BOLD),width=40)
        condition.place(x = 200 , y= 200 , width=450 , height=50)
        condition1 =tk.Label(root,text="Good place to visit",bg = "green" ,font=('times new roman',18,BOLD),width=40)
        condition1.place(x = 200 , y= 300 , width=450 , height=50)


    elif(aqi > 50 and aqi < 100):
       
        condition =tk.Label(root,text="Moderate",bg = "yellow" ,font=('times new roman',18,BOLD),width=40)
        condition.place(x = 200 , y= 200 , width=450 , height=50)
        condition1 =tk.Label(root,text="Can be visited",bg = "yellow" ,font=('times new roman',18,BOLD),width=40)
        condition1.place(x = 200 , y= 300 , width=450 , height=50)
    elif(aqi > 100 and aqi < 150):
        
        condition =tk.Label(root,text="Unhealthy for Sensitive Groups",bg = "orange" ,font=('times new roman',18,BOLD),width=40)
        condition.place(x = 200 , y= 200 , width=450 , height=50)
        condition1 =tk.Label(root,text="Can be Harmful for small kids and old people",bg = "orange" ,font=('times new roman',18,BOLD),width=40)
        condition1.place(x = 200 , y= 300 , width=450 , height=50)
    elif(aqi > 150 and aqi < 200):
        
        condition =tk.Label(root,text="Unhealthy",bg = "red" ,font=('times new roman',18,BOLD),width=40)
        condition.place(x = 200 , y= 200 , width=450 , height=50)
        condition1 =tk.Label(root,text="Can be Harmful for small kids and old people",bg = "red" ,font=('times new roman',18,BOLD),width=40)
        condition1.place(x = 200 , y= 300 , width=450 , height=50)    
    elif(aqi > 200 and aqi < 300):
        
        condition =tk.Label(root,text="Very Unhealthy",bg = "purple" ,font=('times new roman',18,BOLD),width=40)
        condition.place(x = 200 , y= 200 , width=450 , height=50)
        condition1 =tk.Label(root,text="Harmful for all to visit",bg = "purple" ,font=('times new roman',18,BOLD),width=40)
        condition1.place(x = 200 , y= 300 , width=450 , height=50)
    else:
        condition =tk.Label(root,text="Hazardous",bg = "crimson" ,font=('times new roman',18,BOLD),width=40)
        condition.place(x = 200 , y= 200 , width=150 , height=50)
        condition1 =tk.Label(root,text="Shouldn't visit",bg = "crimson" ,font=('times new roman',18,BOLD),width=40)
        condition1.place(x = 200 , y= 300 , width=450 , height=50)

def previouspage1():
    root.destroy()
    import Main

cond =tk.Label(root,text="Enter a Place" ,bg = 'light blue',font=('times new roman',18,BOLD),width = 10)
cond.place(x = 0 , y= 50 , height= 50 )

textbox1 = tk.Entry(root,font=('times new roman',20),width=40)
textbox1.place(x = 200 , y=50 , width=300 , height=50)

air_label=tk.Label(root,text="",font=('times new roman',20,BOLD),width=40)
air_label.place(x = 200 , y= 130 , width=150 , height=50)

air_label1=tk.Label(root,text="AQI",bg = 'light blue',font=('times new roman',18,BOLD),width=40)
air_label1.place(x = 0 , y= 130 , width=150 , height=50)

air_label11=tk.Label(root,text="Condition",bg = 'light blue',font=('times new roman',18,BOLD),width=40)
air_label11.place(x = 0 , y= 200 , width=150 , height=50)

button1 = tk.Button(root,text='Get AQI',fg='blue',font=('times new roman',18,BOLD),width=8,command=lambda: get_aqi(textbox1.get()))
button1.place(x = 450 , y= 130, width=200 , height=50)

info = tk.Label(root,text="  Air Info ",bg = 'light blue',font=('times new roman',18,BOLD),width=100)
info.place(x = 0 , y= 400 , width=150 , height=50)

list1 = tk.Listbox(root,font=('times new roman',15), width=60, height=12)  # Details about the city
list1.place(x= 200, y= 400)

prediction=tk.Label(root,text="Prediction",bg = 'light blue',font=('times new roman',18,BOLD),width=40)
prediction.place(x = 0 , y= 300 , width=150 , height=50)

piebutton = tk.Button(root,text='Generate Pie chart',fg='blue',font=('times new roman',18,BOLD),width=8,command = piebutton)
piebutton.place(x = 200 , y= 700 , width=200 , height=50)

backbutton1= tk.Button(root, text='Back', font=('times new roman',18,BOLD), command=previouspage1)
backbutton1.place(x = 600 , y= 700, width=160 , height=50)
root.mainloop()