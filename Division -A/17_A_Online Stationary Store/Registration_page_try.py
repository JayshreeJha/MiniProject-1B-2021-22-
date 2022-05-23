from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import re
import pymysql
#pattern=['^[a-z 0-9]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$']
pattern="(0|91)?[7-9][0-9]{9}"
SpecialSym =['$', '@', '#', '%']
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
class Register:
    def __init__(self, root):
        self.root = root
        self.root.title("Create Account")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="purple")

        self.bg = ImageTk.PhotoImage(file="images/image4.png")
        bg = Label(self.root, image=self.bg).place(x=250, y=0, relwidth=1, relheight=1)

        self.left = ImageTk.PhotoImage(file="images/image3.jpg")
        left = Label(self.root, image=self.left).place(x=80, y=100, width=400, height=500)

        frame1 = Frame(self.root, bg="white")
        frame1.place(x=480, y=100, width=700, height=500)

        title = Label(frame1, text="REGISTER YOURSELF", font=("times new roman",20,"bold"), bg="white", fg="black").place(x=50, y=30)
        
        
        f_name = Label(frame1, text="First Name", font=("times new roman",15,"bold"), bg="white", fg="black").place(x=50, y=120)
        self.txt_f_name = Entry(frame1, font=("times new roman", 15), bg="light gray")
        self.txt_f_name.place(x=50,y=160,width=250)
        

        l_name = Label(frame1, text="Last Name", font=("times new roman",15,"bold"), bg="white", fg="black").place(x=370, y=120)
        self.txt_l_name = Entry(frame1, font=("times new roman", 15), bg="light gray")
        self.txt_l_name.place(x=370, y=160, width=250)

        contact = Label(frame1, text="Contact Number", font=("times new roman", 15, "bold"), bg="white", fg="black").place(x=50, y=220)
        self.txt_contact = Entry(frame1, font=("times new roman", 15), bg="light gray")
        self.txt_contact.place(x=50, y=260, width=250)
 

        Email = Label(frame1, text="Email id", font=("times new roman", 15, "bold"), bg="white", fg="black").place(x=370, y=220)
        self.txt_Email = Entry(frame1, font=("times new roman", 15), bg="light gray")
        self.txt_Email.place(x=370, y=260, width=250)

        password = Label(frame1, text="Password", font=("times new roman",15,"bold"), bg="white", fg="black").place(x=50, y=320)
        self.txt_password = Entry(frame1, font=("times new roman", 15), bg="light gray",show="*")
        self.txt_password.place(x=50, y=360, width=250)
 
        c_password = Label(frame1, text="Confirm Password", font=("times new roman",15,"bold"), bg="white", fg="black").place(x=370, y=320)
        self.txt_c_password = Entry(frame1, font=("times new roman", 15), bg="light gray",show="*")
        self.txt_c_password.place(x=370, y=360, width=250)

        self.btn_img = ImageTk.PhotoImage(file="images/image.png")
        btn_register = Button(frame1, image=self.btn_img, bd=0,cursor="hand2", command=self.register_data).place(x=50, y=420)

        btn_login = Button(self.root, text="Sign In",command=self.login_window,font=("times new roman",20), bd=0, cursor="hand2",bg="black",fg="white").place(x=190, y=540, width=180)
    
    def login_window(self):
        self.root.destroy()
        import login
    
    
    
    def clear(self):
        self.txt_f_name.delete(0,END)
        self.txt_l_name.delete(0,END)
        self.txt_contact.delete(0,END)
        self.txt_Email.delete(0,END)
        self.txt_password.delete(0,END)
        self.txt_c_password.delete(0,END)
    
    def register_data(self):
        if self.txt_f_name.get() == "" or self.txt_l_name.get() == "" or self.txt_contact.get() == "" or self.txt_Email.get() == "" or self.txt_password.get() == "" or self.txt_c_password.get() == "" :
            messagebox.showerror("Error", "All Fields are Required", parent = self.root)
        elif len(self.txt_f_name.get()) <= 2 or len(self.txt_l_name.get()) <= 2:
            messagebox.showerror("Error", "Minimum Three Characters are required in First Name and Last Name ", parent = self.root)
        elif len(self.txt_f_name.get()) >= 100 or len(self.txt_l_name.get()) >= 100:
            messagebox.showerror("Error", "Maximum Characters must not exceed 100 characters ", parent = self.root)
        elif any(ch.isdigit() for ch in self.txt_f_name.get()) or any(ch.isdigit() for ch in self.txt_l_name.get()):
            messagebox.showerror("Error", "Please enter Characters in Firstname and Lastname", parent = self.root)
        elif len(self.txt_contact.get()) < 10 or len(self.txt_contact.get()) > 10  or  not re.search(pattern, self.txt_contact.get()):
            messagebox.showerror("Error", "Please enter valid 10 digit Contact Number", parent = self.root)
        elif len(self.txt_Email.get())<6 or not re.fullmatch(regex,self.txt_Email.get()) :
            messagebox.showerror("Error", "Please enter valid Email id example:siddhantdarekar1010@gmail.com", parent = self.root)

        elif not any(char.isupper() for char in self.txt_password.get()) or not any(char.isdigit() for char in self.txt_password.get()) or not any(char.islower() for char in self.txt_password.get()) or not any(char in SpecialSym for char in self.txt_password.get()):
            messagebox.showerror("Error", "Please enter a password containing a minimum of 1 lower case letter [a-z], minimum of 1 upper case letter [A-Z], minimum of 1 numeric character [0-9] and a minimum of 1 special character: '$', '@', '#', '%'", parent=self.root)
        
        elif len(self.txt_password.get())<6 or len(self.txt_password.get())>15:
            messagebox.showerror("Error", "Password should not be greater than 15 characters and should have atleast 6 characters", parent=self.root)

        elif self.txt_password.get() != self.txt_c_password.get() :
            messagebox.showerror("Error", "Password and Confirm Password should be same", parent=self.root)
        
        else:
            try:
                con=pymysql.connect(host="localhost",user="root",password="",database="buyer")
                cur=con.cursor()
                cur.execute("select * from customers where Email=%s",self.txt_Email.get())
                row=cur.fetchone()
                #print(row)
                if row!=None:
                    messagebox.showerror("Error", "User already Exists, Please try with another Email id", parent=self.root)
                else:
                    cur.execute("insert into customers (f_name,l_name,contact,Email,password) values(%s,%s,%s,%s,%s)",
                                  (self.txt_f_name.get(),
                                  self.txt_l_name.get(),
                                  self.txt_contact.get(),
                                  self.txt_Email.get(),
                                  self.txt_password.get()
                                  ))

                    con.commit()
                    con.close()
                    messagebox.showinfo("Success", "Your Account has been Successfully Registered", parent=self.root)
                    self.clear()
            except Exception as es:
                messagebox.showerror("Error", f"Error due to:{str(es)}", parent=self.root)
            
            
            
            
            
        
            
        





root=Tk()
obj=Register(root)
root.mainloop()