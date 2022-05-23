from tkinter import *
from PIL import ImageTk #pip install pillow
from tkinter import messagebox
import pymysql
class login:
    def __init__(self,root):
        self.root=root

        self.root.title("Login system")
        self.root.geometry("1300x600+100+50")
        #====BG IMage=====
        self.bg=ImageTk.PhotoImage(file=r"C:\Users\DELL\Downloads\Mini project\Mini project\Images\Face-recognition.jpg")
        self.bg_image=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)
        self.root.resizable(False,False)
        #====BG Image====
        Frame_login=Frame(self.root,bg="white")
        Frame_login.place(x=150,y=150,height=340,width=500)




        title=Label(Frame_login,text="Login here",font=("Impact",35,"bold"),fg="#d77337",bg="white").place(x=90,y=10)
        desc=Label(Frame_login,text="Face detection and Face recognition system",font=("Goudy old style",15,"bold"),fg="#d25d17",bg="white").place(x=90,y=70)
         
        lbl_user= Label(Frame_login,text="Student ID",font=("Goudy old style",15,"bold"),fg="gray",bg="white").place(x=90,y=120)
        self.txt_user=Entry(Frame_login,font=("times new roman",15))
        self.txt_user.place(x=90,y=150,width=350,height=35)

        lbl_pass= Label(Frame_login,text="Password",font=("Goudy old style",15,"bold"),fg="gray",bg="white").place(x=90,y=180)
        self.txt_pass=Entry(Frame_login,font=("times new roman",15))
        self.txt_pass.place(x=90,y=210,width=350,height=35)

        forget_btn=Button(Frame_login,text="Forgot password?",bg="white",fg="#d77337",font=("times new roman",12)).place(x=90,y=280)
        Login_btn=Button(self.root,command=self.login_function,text="Login",fg="white",bg="#d77337",font=("times new roman",20)).place(x=300,y=470,width=180,height=40)


    def login_function(self):
        if self.txt_pass.get()=="" or self.txt_user.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        elif self.txt_pass.get()!="123456" or self.txt_user.get()!="aagya":
            messagebox.showerror("Error","Invalid username/password",parent=self.root)
        else:
            messagebox.showinfo("Welcome",parent=self.root)
            




        
        


root=Tk()  #object of tkinter module
obj=login(root) #object of class login
root.mainloop() 