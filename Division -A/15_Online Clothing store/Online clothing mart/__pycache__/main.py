from fileinput import filename
import sys
from tkinter import messagebox
import tkinter  as tk 
from tkinter import filedialog
from tkinter.filedialog import askopenfile
from tokenize import Name
from PIL import Image, ImageTk
import io
from turtle import window_width
import PyQt5
import mysql.connector as conn
from PyQt5 import QtWidgets
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import*
from PyQt5.QtWidgets import*
from PyQt5.uic import loadUi
from PySide2 import*
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator
from mysql.connector import Error
import webbrowser
import requests



class Main(QMainWindow):    
        
    def __init__(self):
        super(Main,self).__init__()
        loadUi("Main Page.ui",self)
        
        self.men.clicked.connect(self.Men)
        self.login.clicked.connect(self.log)
        self.women.clicked.connect(self.Women)
        self.admin.clicked.connect(self.Admin)

    def Admin(self):
        lpp.show()
        mp.close()

    def ds(self):
        self.show()


    def log(self):
        lp.show()
        mp.close()

    def Men(self):
        ms.show()
        mp.close()

    def Women(self):
        wp.show()
        mp.close()

class men(QMainWindow):    
        
    def __init__(self):
        super(men,self).__init__()
        loadUi("men section.ui",self)
        self.shirt.clicked.connect(self.shirts)
        self.tshirt.clicked.connect(self.tshirts)
        self.sweatshirt.clicked.connect(self.sweatshirts)
        self.pants.clicked.connect(self.pant)
        self.jeans.clicked.connect(self.jean)
        self.indian_wear.clicked.connect(self.IndianW)
        self.women.clicked.connect(self.Women)
        self.back.clicked.connect(self.Back)
        self.login.clicked.connect(self.log)

    def log(self):
        lp.show()
        ms.close()

        

    def Women(self):
        wp.show()
        ms.close()
        
        self.back.clicked.connect(self.Back)
        self.login.clicked.connect(self.Login)


    
    def Back(self):
        mp.show()
        ms.close()

    def Login(self):
        lp.show()
        ms.close()

    
    def shirts(self):
        ss.show()
        ms.close() 

    def tshirts(self):
        ts.show()
        ms.close()  

    def sweatshirts(self):
        sh.show()
        ms.close()  

    def pant(self):
        tp.show()
        ms.close() 

    def jean(self):
        js.show()
        ms.close()

    def IndianW(self):
        iw.show()
        ms.close()



class Women(QMainWindow):    
    def __init__(self):
        super(Women,self).__init__()
        loadUi("Women's front page.ui",self)
        self.back.clicked.connect(self.Back)
        self.login.clicked.connect(self.Login)
        self.men.clicked.connect(self.Men)
     
    def Back(self):
        mp.show()
        wp.close()

    def Login(self):
        lp.show()
        wp.close()

    def Men(self):
        ms.show()
        wp.close()

class Shirtss(QMainWindow):
    def __init__(self):
        super(Shirtss,self).__init__()
        loadUi("shirts.ui",self)
        self.display = df()
        self.back.clicked.connect(self.Back)
        self.men.clicked.connect(self.Men)
        self.women.clicked.connect(self.Women)
        self.formal1.clicked.connect(self.Formal1)
        self.formal2.clicked.connect(self.Formal2)
        self.formal3.clicked.connect(self.Formal3)
        self.formal4.clicked.connect(self.Formal4)
        db=conn.connect(host="localhost",user="root",password="Ashmina27@",database="trail")
        cursor=db.cursor()  

    def Formal1(self):
        Codef1=self.codef1.text()     
        self.display.code.setText(Codef1)
        self.display.ds()
        ss.close()

    def Formal2(self):
        Codef2=self.codef2.text()     
        self.display.code.setText(Codef2)
        self.display.ds()
        ss.close()

    def Formal3(self):
        Codef3=self.codef3.text()     
        self.display.code.setText(Codef3)
        self.display.ds()
        ss.close()

    def Formal4(self):
        Codef4=self.codef4.text()     
        self.display.code.setText(Codef4)
        self.display.ds()
        ss.close()
                   

    def Men(self):
        ms.show()
        ss.close()

    def Women(self):
        wp.show()
        ss.close()
        
    
    def Back(self):
        mp.show()
        ss.close()    

    def ds(self):
        self.show()

    

class df(QMainWindow):
    def __init__(self):
        super(df,self).__init__()
       
        loadUi("displayframe.ui",self)
        self.cart.clicked.connect(self.Cart)
        self.buynow.clicked.connect(self.buy)
        self.back.clicked.connect(self.Back)
        self.men.clicked.connect(self.Men)
        self.women.clicked.connect(self.Women)

    def Men(self):
        ms.show()
        a6.close()

    def Women(self):
        wp.show()
        a6.close()
        
    
    def Back(self):
        ss.show()
        a6.close() 

    def buy(self):
        lp.show()
        a6.close()

    def Cart(self):
        Code=self.code.text()
        db=conn.connect(host="localhost",user="root",password="Ashmina27@",database="trail")
        cursor=db.cursor()       
        cursor.execute("SELECT *FROM productdetails WHERE code='"+Code+"'")
        result = cursor.fetchone()
        self.Caart.code.setText(Code)
        self.Caart.ds()
    
    def ds(self):
        self.show()
        Code =  self.code.text()
        db=conn.connect(host="localhost",user="root",password="Ashmina27@",database="trail")
        cursor=db.cursor()       
        cursor.execute("SELECT *FROM productdetails WHERE code='"+Code+"'")
        result = cursor.fetchone()
        self.name.setText(result[0])
        self.namee.setText(result[0])
        self.dimen.setText(result[1])
        self.depart.setText(result[3])
        self.type.setText(result[4])
        self.colour.setText(result[5])
        self.material.setText(result[6])
        self.sizee.setText(result[7])
        self.discription.setText(result[8])
        
        ImagePath=result[9]
        pixmap = QPixmap(ImagePath)
        pixmap5 = pixmap.scaled(825, 800)
        self.image.setPixmap(QPixmap(pixmap5))
        self.discount.setText(result[10])
        self.price.setText(result[11])
        db.commit()
        


class tshirtss(QMainWindow):
    def __init__(self):
        super(tshirtss,self).__init__()
        loadUi("tshirts.ui",self)
             
    #     self.back.clicked.connect(self.Back) 
    #     self.men.clicked.connect(self.Men)
    #     self.women.clicked.connect(self.Women)

    # def Men(self):
    #     ms.show()
    #     ts.close()

    # def Women(self):
    #     wp.show()
    #     ts.close()

    # def framee(self):        
    #     a6.show()            
    #     ts.close()          

    # def Back(self):
    #     ms.show()
    #     ts.close() 

class hoodies(QMainWindow):
    def __init__(self):
        super(hoodies,self).__init__()
        loadUi("sweatshirts.ui",self)
        self.back.clicked.connect(self.Back)
        self.men.clicked.connect(self.Men)
        self.women.clicked.connect(self.Women)

    def Men(self):
        ms.show()
        sh.close()

    def Women(self):
        wp.show()
        sh.close()

    def Back(self):
        ms.show()
        sh.close() 

class Trousers(QMainWindow):
    def __init__(self):
        super(Trousers,self).__init__()
        loadUi("pants.ui",self) 
        self.back.clicked.connect(self.Back)  
        self.men.clicked.connect(self.Men)
        self.women.clicked.connect(self.Women)

    def Men(self):
        ms.show()
        tp.close()

    def Women(self):
        wp.show()
        tp.close()

    def Back(self):
        ms.show()
        tp.close() 

class Jeans(QMainWindow):
    def __init__(self):
        super(Jeans,self).__init__()
        loadUi("jeans.ui",self)
        self.back.clicked.connect(self.Back)
        self.men.clicked.connect(self.Men)
        self.women.clicked.connect(self.Women)

    def Men(self):
        ms.show()
        js.close()

    def Women(self):
        wp.show()
        js.close()
         
    def Back(self):
        ms.show()
        js.close()

class Indianwear(QMainWindow):
    def __init__(self):
        super(Indianwear,self).__init__()
        loadUi("indianwear.ui",self)
        self.back.clicked.connect(self.Back)
        self.men.clicked.connect(self.Men)
        self.women.clicked.connect(self.Women)

    def Men(self):
        ms.show()
        iw.close()

    def Women(self):
        wp.show()
        iw.close()

    def Back(self):
        ms.show()
        iw.close() 

class Register(QMainWindow):
    def __init__(self):
        super(Register,self).__init__()
        loadUi("Registerpage.ui",self)
        self.save.clicked.connect(self.register)
        validator = QRegExpValidator(QRegExp(r'[0-9]+'))
        self.contact.setValidator(validator)
        self.login.clicked.connect(self.Login)

    def Login(self):
        lp.show()
        rp.close()
    
    def register(self):

        Namee = self.name.text()
        Email = self.email.text()
        Contact = self.contact.text()
        Sques = self.securityq.currentText()
        Securityans = self.securityA.text()
        Pass = self.password.text()
        confpass = self.Cpassword.text()
            
        if Namee == "" or Email == "" or Contact == "" or Sques == "Select" or Securityans == "" or Pass == "" or confpass == "" :
            messagebox.showerror("Error","All fields are required")
        
        elif Pass != confpass:
            messagebox.showerror("Error","Password and confirm password should be same")

        elif self.Conditions.isChecked() == False :
            messagebox.showerror("Error","Please Agree our Terms and Conditions")

        elif len(Contact)!=10:
            messagebox.showerror("Error","Contact number should contain exact 10 digits.")

        elif len(Email)>=12:
            if Email[0].isalpha():
                if ("@" in Email) and (Email.count("@")==1):
                    if (Email[-4]=="."):
                        db=conn.connect(host="localhost",user="root",password="Ashmina27@",database="trail")
                        cursor=db.cursor()
                        cursor.execute("Select * from registerr where Emailid ='"+Email+"'")
                        row=cursor.fetchone()
                        if row!=None:
                            messagebox.showerror("Error","User already exist, Please Login")
                        else:
                            cursor.execute("INSERT into registerr(Name,Emailid,contact,Security_ques,Security_ans,Password) values('"+Namee+"','"+Email+"','"+Contact+"','"+Sques+"',md5('"+Securityans+"'),md5('"+Pass+"'))")
                            db.commit()
                            db.close()
                            messagebox.showinfo("Registration Successfull","Welcome to Pocket Fashion")
                            lp.show()
                            rp.close()
                        
                    else:
                        messagebox.showerror("Error","Enter valid email address with .com")
                else:
                    messagebox.showerror("Error","Enter valid email address with @")
            else:
                messagebox.showerror("Error","First character should be alphabet")
            
        else:
            print("Success")
            

class Login(QMainWindow):
    def __init__(self):
        super(Login,self).__init__()
        loadUi("Loginpage.ui",self)
        self.address=PaymentOption()
        self.back.clicked.connect(self.Back)
        self.login.clicked.connect(self.log)
        self.register_2.clicked.connect(self.registerr)
        self.forgot.clicked.connect(self.Forgot)

    def Forgot(self):
        fp.show()
        

    

        

    def registerr(self):
        rp.show()
        lp.close()    

    def log(self):
        Email=self.email.text()
        Pass = self.password.text()

        if Email =="" or Pass == "":
            messagebox.showerror("Error","Enter Email Id and Password")
        else:
            db=conn.connect(host="localhost",user="root",password="Ashmina27@",database="trail")
            cursor=db.cursor()
            cursor.execute("SELECT * FROM registerr where Emailid ='"+Email+"' and Password = md5('"+Pass+"')")
            row=cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid Username & Password")
                
            else:
                mp.show()
                lp.close()
                self.address.emailid.setText(row[2])
                self.address.contact.setText(row[3])
                self.address.name.setText(row[1])
                self.address.ds()
                
            db.commit()
            
            
    
    def Back(self):
        mp.show()
        lp.close()

class forgot(QMainWindow):
    def __init__(self):
        super(forgot,self).__init__()
        loadUi("forgotpasswd.ui",self)
        self.change = Change()
        self.next.clicked.connect(self.Next)

    def Next(self):
        Email=self.email.text()
        Ques=self.ques.currentText()
        Ans=self.ans.text()
        
       
        if Ques=="Select":
            messagebox.showerror("Error","Select the security question")
        elif Ans=="":
            messagebox.showerror("Error","Please enter Answer")
        else:
            db=conn.connect(host="localhost",user="root",password="Ashmina27@",database="trail")
            cursor=db.cursor()
            cursor.execute("SELECT * FROM registerr where Emailid ='"+Email+"' and Security_ques='"+Ques+"' and Security_ans=md5('"+Ans+"')")
            result=cursor.fetchone()
            if result==None:
                messagebox.showerror("Error","Please enter correct Answer")
            else :
                self.change.email.setText(Email)
                self.change.ds()
                fp.close()

class Change(QMainWindow):    
        
    def __init__(self):
        super(Change,self).__init__()
        loadUi("Changepassword.ui",self)
        self.change.clicked.connect(self.Changee)

    def Changee(self):
        Email=self.email.text()
        ChangeP=self.changeP.text()
        Confirm=self.confirm.text()
        if ChangeP != Confirm:
            messagebox.showerror("Error","Password and Confirm password should be same.")
        else :
            db=conn.connect(host="localhost",user="root",password="Ashmina27@",database="trail")
            cursor=db.cursor()
            cursor.execute("UPDATE `trail`.`registerr` SET `Password` = md5('"+ChangeP+"')  WHERE (`Emailid` = '"+Email+"')")
            db.commit()
            cp.close()
            lp.show()


        
    def ds(self):
        self.show()


class PaymentOption(QMainWindow):    
        
    def __init__(self):
        super(PaymentOption,self).__init__()
        loadUi("addresspage.ui",self)
        self.save.clicked.connect(self.ds)
        self.proceed.clicked.connect(self.Proceed)

    def Proceed(self):
        cod = self.cod.isChecked()
        Online = self.online.isChecked()
        Email=self.emailid.text()
        try:
            if cod == 1:
                messagebox.showerror("Error","Order placed successfully")
            elif Online == 1:
                db=conn.connect(host="localhost",user="root",password="Ashmina27@",database="trail")
                cursor=db.cursor()
                cursor.execute("Select *from shipping where email = '"+Email+"'")
                result = cursor.fetchall()
                url = "https://test.cashfree.com/api/v1/order/create"

                payload = {
                    "appId": "161152e57c6b5deb81050e0da0251161",
                    "secretKey": "3f5708722555f72a85267fef97cc48c17f8c2dd1",
                    "orderId": result[7],
                    "orderAmount": "1000",
                    "orderCurrency": "INR",
                    "orderNote": "This is an optional field",
                    "customerName": result[1],
                    "customerEmail": result[0],
                    "customerPhone": result[6],
                    "returnUrl": "https://cashfree.com",
                    "notifyUrl": ""
                }
                response = requests.request("POST",url,data=payload)
                print(response.text[29:94])
                urls = [response.text[29:93]]
                for urll in urls:
                    webbrowser.open_new_tab(urll)
        except Exception as e:
            messagebox.showerror("Error","Check again")
                

    def ds(self):
        self.show()
        Email=self.emailid.text()
        Name=self.name.text()
        Address=self.address.toPlainText()
        Town=self.town.text()
        Statee=self.state.currentText()
        Pincode=self.pincode.text()
        Contact=self.contact.text()
        cod = self.cod.isChecked()
        Online = self.online.isChecked()
        if Email=="" or Name=="" or Address=="" or Town=="" or Statee=="" or Pincode=="" or Contact=="":
            messagebox.showerror("Error","Enter all fields")
        elif cod == Online == 0:
            messagebox.showerror("Error","Select a payment mode.")
        else:
            db=conn.connect(host="localhost",user="root",password="Ashmina27@",database="trail")
            cursor=db.cursor()
            cursor.execute("SELECT * FROM registerr where Emailid ='"+Email+"' and Contact='"+Contact+"'")
            result=cursor.fetchone()
            if result==None:
                messagebox.showerror("Error","Email not found in database.")
            else:
                try:
                    if cod == 1:
                        db=conn.connect(host="localhost",user="root",password="Ashmina27@",database="trail")
                        cursor=db.cursor()
                        cursor.execute("INSERT INTO shipping(email,name,address,town,state,pincode,contact,paymentmode) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", (Email,Name,Address,Town,Statee,Pincode,Contact,cod))
                        db.commit()
                        db.close()
                        messagebox.showinfo("Success !","Shipping Details Successfully inserted")
                        mp.show()
                        po.close()
                    elif Online == 1:
                        db=conn.connect(host="localhost",user="root",password="Ashmina27@",database="trail")
                        cursor=db.cursor()
                        cursor.execute("INSERT INTO shipping(email,name,address,town,state,pincode,contact,paymentmode) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", (Email,Name,Address,Town,Statee,Pincode,Contact,Online))
                        db.commit()
                        db.close()
                        messagebox.showinfo("Success !","Shipping Details Successfully inserted")
                        mp.show()
                        po.close()
                        

                except Exception as e:
                    messagebox.showerror("Error", "Check again")


    



class Loginn(QMainWindow):
    def __init__(self):
        super(Loginn,self).__init__()
        loadUi("Adminlogin.ui",self)
        self.login.clicked.connect(self.Alogin)

    def Alogin(self):
        Username=self.username.text()
        Password=self.password.text()
        if Username == "Ashmina" and Password == "20104052":
            messagebox.showinfo("Success","Login successful")
            mpp.show()
            lpp.close()

        elif Username == "Kritika" and Password == "20104102":
            messagebox.showinfo("Success","Login successful")
            mpp.show()
            lpp.close()

        elif Username == "Sakshi" and Password == "20104106":
            messagebox.showinfo("Success","Login successful")
            mpp.show()
            lpp.close()

        elif Username == "Neha" and Password == "20104134":
            messagebox.showinfo("Success","Login successful")
            mpp.show()
            lpp.close()

        else :
            messagebox.showerror("Error","Check username or password.")

class Mainn(QMainWindow):
    def __init__(self):
        super(Mainn,self).__init__()
        loadUi("Upload.ui",self)
        self.browse.clicked.connect(self.Browse)
        self.add.clicked.connect(self.addDetails)
        self.updatee.clicked.connect(self.Update)
        self.display.clicked.connect(self.Display)
        self.logout.clicked.connect(self.Logout)

    def Logout(self):
        lpp.show()
        mpp.close()
        
        
    def Update(self):
        ud.show()
        mpp.close()

    def Display(self):
        up.show()
        mpp.close()

    def Browse(self):
        file_name = QFileDialog.getOpenFileName(self, 'Open File', 'c:\\', 'Image Files (*.png *.jpg *gif *.jpeg)')
        image_path = file_name[0]          
        pixmap = QPixmap(image_path)
        pixmap5 = pixmap.scaled(300, 250)
        self.image.setPixmap(QPixmap(pixmap5))
        self.path.setText(image_path)

    def addDetails(self):
        Name = self.Pname.text()
        dimen=self.dimensions.text()
        Pcode = self.code.text()
        depart = self.gender.currentText()
        Type = self.type.currentText()
        Colour = self.colour.text()
        Material = self.material.text()
        Size = self.sizee.currentText()
        Discription = self.discription.toPlainText()
        Path = self.path.text()
        Discount = self.discount.currentText()
        Price = self.price.text()
        if Name == "" or dimen == "" or Pcode == "" or depart=="" or Type=="" or Colour=="" or Material=="" or Size=="" or Discription=="" or Path=="" or Price=="":
            messagebox.showerror("Error","All fields are required")
        
        else:
            try:
                db=conn.connect(host="localhost",user="root",password="Ashmina27@",database="trail")
                cursor=db.cursor()
                cursor.execute("INSERT INTO productdetails(name,dimension,code,department,type,colour,material,size,description,path,discount,price) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (Name,dimen,Pcode,depart,Type,Colour,Material,Size,Discription,Path,Discount,Price ))
                db.commit()
                db.close()
                messagebox.showinfo("Success !","Product Details Successfully inserted")

            except Exception as e:
                messagebox.showinfo("Error!","Product code already exists!")

class Display(QMainWindow):    
        
    def __init__(self):
        super(Display,self).__init__()
        loadUi("Display.ui",self)
        self.Update = Update()
        self.Updatee.clicked.connect(self.updatee)
        self.remove.clicked.connect(self.Remove)
        self.Updat.clicked.connect(self.updat)
        self.upload.clicked.connect(self.Upload)
        self.pdetails.clicked.connect(self.Pdetails)
        db=conn.connect(host="localhost",user="root",password="Ashmina27@",database="trail")
        cursor=db.cursor()       
        cursor.execute("SELECT *FROM productdetails ")
        self.display.setRowCount(20)       
        tablerow= 0      
        for row in cursor:
            self.display.setItem(tablerow, 0, PyQt5.QtWidgets.QTableWidgetItem(row[0]))
            self.display.setItem(tablerow, 1, PyQt5.QtWidgets.QTableWidgetItem(row[1]))
            self.display.setItem(tablerow, 2, PyQt5.QtWidgets.QTableWidgetItem(row[2]))
            self.display.setItem(tablerow, 3, PyQt5.QtWidgets.QTableWidgetItem(row[3]))
            self.display.setItem(tablerow, 4, PyQt5.QtWidgets.QTableWidgetItem(row[4]))
            self.display.setItem(tablerow, 5, PyQt5.QtWidgets.QTableWidgetItem(row[5]))
            self.display.setItem(tablerow, 6, PyQt5.QtWidgets.QTableWidgetItem(row[6]))
            self.display.setItem(tablerow, 7, PyQt5.QtWidgets.QTableWidgetItem(row[7]))
            self.display.setItem(tablerow, 8, PyQt5.QtWidgets.QTableWidgetItem(row[8]))
            self.display.setItem(tablerow, 9, PyQt5.QtWidgets.QTableWidgetItem(row[9]))
            self.display.setItem(tablerow, 10, PyQt5.QtWidgets.QTableWidgetItem(row[10]))
            self.display.setItem(tablerow, 11, PyQt5.QtWidgets.QTableWidgetItem(row[11]))           
            tablerow+=1
        self.logout.clicked.connect(self.Logout)

    def Logout(self):
        lpp.show()
        up.close()

    def Pdetails(self):
        db=conn.connect(host="localhost",user="root",password="Ashmina27@",database="trail")
        cursor=db.cursor()       
        cursor.execute("SELECT *FROM productdetails ")
        self.display.setRowCount(20)       
        tablerow= 0      
        for row in cursor:
            self.display.setItem(tablerow, 0, PyQt5.QtWidgets.QTableWidgetItem(row[0]))
            self.display.setItem(tablerow, 1, PyQt5.QtWidgets.QTableWidgetItem(row[1]))
            self.display.setItem(tablerow, 2, PyQt5.QtWidgets.QTableWidgetItem(row[2]))
            self.display.setItem(tablerow, 3, PyQt5.QtWidgets.QTableWidgetItem(row[3]))
            self.display.setItem(tablerow, 4, PyQt5.QtWidgets.QTableWidgetItem(row[4]))
            self.display.setItem(tablerow, 5, PyQt5.QtWidgets.QTableWidgetItem(row[5]))
            self.display.setItem(tablerow, 6, PyQt5.QtWidgets.QTableWidgetItem(row[6]))
            self.display.setItem(tablerow, 7, PyQt5.QtWidgets.QTableWidgetItem(row[7]))
            self.display.setItem(tablerow, 8, PyQt5.QtWidgets.QTableWidgetItem(row[8]))
            self.display.setItem(tablerow, 9, PyQt5.QtWidgets.QTableWidgetItem(row[9]))
            self.display.setItem(tablerow, 10, PyQt5.QtWidgets.QTableWidgetItem(row[10]))
            self.display.setItem(tablerow, 11, PyQt5.QtWidgets.QTableWidgetItem(row[11]))           
            tablerow+=1

    def updat(self):
        ud.show()
        up.close()

    def Upload(self):
        mpp.show()
        up.close()


    def updatee(self):
        row = self.display.currentRow() # Index of Row
        Tcode = self.display.item(row, 2)
        Code = Tcode.text()
        self.Update.code.setText(Code)
        self.Update.ds()
        up.close()
    
    def Remove(self):
        row = self.display.currentRow() # Index of Row
        Tcode = self.display.item(row, 2)
        Code = Tcode.text()
        db=conn.connect(host="localhost",user="root",password="Ashmina27@",database="trail")
        cursor=db.cursor()       
        cursor.execute("DELETE FROM productdetails WHERE code='"+Code+"'")
        db.commit()
        messagebox.showinfo("Success!","Product details successfully deleted from database.")


class Update(QMainWindow):    
        
    def __init__(self):
        super(Update,self).__init__()
        loadUi("Update.ui",self)
        self.search.clicked.connect(self.Search)
        self.add.clicked.connect(self.Update)
        self.browse.clicked.connect(self.Browse)
        self.upload.clicked.connect(self.Upload)
        self.display.clicked.connect(self.Dplay)
        self.logout.clicked.connect(self.Logout)

    def Logout(self):
        lpp.show()
        ud.close()

    def Upload(self):
        mpp.show()
        ud.close()    

    def Dplay(self):
        up.show()
        ud.close()

    def Search(self):
        try:
            Code = self.code.text()
            db=conn.connect(host="localhost",user="root",password="Ashmina27@",database="trail")
            cursor=db.cursor()       
            cursor.execute("SELECT *FROM productdetails WHERE code='"+Code+"'")
            result = cursor.fetchone()
            self.Pname.setText(result[0])
            self.dimensions.setText(result[1])
            self.gender.setCurrentText(result[3])
            self.type.setCurrentText(result[4])
            self.colour.setText(result[5])
            self.material.setText(result[6])
            self.sizee.setCurrentText(result[7])
            self.discription.setPlainText(result[8])
            self.path.setText(result[9])
            ImagePath = self.path.text()
            pixmap = QPixmap(ImagePath)
            pixmap5 = pixmap.scaled(400, 250)
            self.image.setPixmap(QPixmap(pixmap5))
            self.discount.setCurrentText(result[10])
            self.price.setText(result[11])
            db.commit()
        except Exception as e :
            messagebox.showerror("Error", "Enter Product code to search!")
        
    
    def Update(self):
        Name = self.Pname.text()
        dimen=self.dimensions.text()
        Pcode = self.code.text()
        depart = self.gender.currentText()
        Type = self.type.currentText()
        Colour = self.colour.text()
        Material = self.material.text()
        Size = self.sizee.currentText()
        Discription = self.discription.toPlainText()
        Path = self.path.text()
        Discount = self.discount.currentText()
        Price = self.price.text()
        db=conn.connect(host="localhost",user="root",password="Ashmina27@",database="trail")
        cursor=db.cursor()
        cursor.execute("UPDATE `trail`.`productdetails` SET `name` = '"+Name+"', `dimension` = '"+dimen+"', `department` = '"+depart+"', `type` = '"+Type+"', `colour` = '"+Colour+"', `material` = '"+Material+"', `size` = '"+Size+"', `description` = '"+Discription+"', `path` = '"+Path+"', `discount` = '"+Discount+"', `price` = '"+Price+"' WHERE (`code` = '"+Pcode+"')")
        db.commit()
        messagebox.showinfo("Success !","Product Details Successfully Updated")

    def Browse(self):
        file_name = QFileDialog.getOpenFileName(self, 'Open File', 'c:\\', 'Image Files (*.png *.jpg *gif *.jpeg)')
        image_path = file_name[0]          
        pixmap = QPixmap(image_path)
        pixmap5 = pixmap.scaled(400, 250)
        self.image.setPixmap(QPixmap(pixmap5))
        self.path.setText(image_path)    
            
    def ds(self):
        self.show()

App=QApplication(sys.argv)
mp=Main()
lp=Login()
rp=Register()
#Men
ms=men()
ss=Shirtss()
ts=tshirtss()
sh=hoodies()
tp=Trousers()
js=Jeans()
iw=Indianwear()
#Women
wp=Women()
#Display page
a6=df()

po=PaymentOption()

fp=forgot()
cp=Change()
lpp=Loginn()
mpp=Mainn()
up=Display()
ud=Update()

mp.show()
App.exec()       