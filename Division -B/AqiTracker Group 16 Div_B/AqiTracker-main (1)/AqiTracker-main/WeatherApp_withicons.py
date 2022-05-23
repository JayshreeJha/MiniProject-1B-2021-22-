from configparser import ConfigParser
from turtle import width
import tkinter as tk
import requests
from tkinter import *
from PIL import Image, ImageTk

app = tk.Tk()
app.geometry("700x700")

img = PhotoImage(file="sky.png")
label = Label(
    app,
    image=img
)
label.place(x=0, y=0,relwidth=1,relheight=1)



def format_response(weather_json):
    try:
        city = weather_json['name']
        conditions = weather_json['weather'][0]['description']
        temp = weather_json['main']['temp']
        temp = (temp-32) * 5/9
        final_str = 'City: %s \nConditions: %s \nTemperature (°C): %s' % (city, conditions, temp)
    except:
        final_str = 'There was a problem retrieving that information'
    #final_str = 'hello'
    return final_str


def get_weather(city):
    weather_key = 'edffd1bf975a74d5d10e58c5ac8be2d3'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': 'edffd1bf975a74d5d10e58c5ac8be2d3', 'q': city, 'units':'imperial'}
    response = requests.get(url, params=params)
    print(response.json())
    weather_json = response.json()

    results['text'] = format_response(response.json())

    icon_name = weather_json['weather'][0]['icon']
    open_image(icon_name)

def open_image(icon):
    size = int(lower_frame.winfo_height()*0.25)
    img = ImageTk.PhotoImage(Image.open('./img/'+icon+'.png').resize((size, size)))
    weather_icon.delete("all")
    weather_icon.create_image(0,0, anchor='nw', image=img)
    weather_icon.image = img

def previouspage():
    app.destroy()
    import Main



frame = tk.Frame(app,  bg='#42c2f4', bd=5)

frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')
#frame_window = C.create_window(100, 40, window=frame)

textbox = tk.Entry(frame,font=('times new roman',20))
textbox.place(relwidth=0.65, relheight=1)

submit = tk.Button(frame, text='Get Weather', font=('times new roman',20), command=lambda: get_weather(textbox.get()))
#submit.config(font=)
submit.place(relx=0.68, relheight=1, relwidth=0.3)

backbutton= tk.Button(app, text='Back', font=40, command=previouspage)
#submit.config(font=)
backbutton.place(x = 450 , y= 600 , width=160 , height=60)

lower_frame = tk.Frame(app, bg='#42c2f4', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

bg_color = 'white'
results = tk.Label(lower_frame, anchor='nw', justify='left', bd=4)
results.config(font=40, bg=bg_color)
results.place(relwidth=1, relheight=1)

weather_icon = tk.Canvas(results, bg=bg_color, bd=0, highlightthickness=0)
weather_icon.place(relx=.75, rely=0, relwidth=1, relheight=0.5)

app.mainloop()