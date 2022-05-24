from email.mime import image
import sys
from turtle import home
from PyQt5.QtGui import QPixmap
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
import Connectionpro as cp 

class login(QDialog):

    def __init__(self):
        super(login,self).__init__()
        loadUi("Login.ui", self)
        self.log_btn.clicked.connect(self.loginfunction)
        self.reg_btn.clicked.connect(self.gotosign)
        

    def loginfunction(self):
        
        un = self.username_txt.text()
        pa = self.pass_txt.text()
        username_login= ""
        password_login = ""
        cp.cursor.execute("select * from register where username ='"+ un +"'")
        result = cp.cursor.fetchall()
        for row in result:
            username_login = row[0] 
            password_login = row[1]
        
        if len(un)==0 or len(pa) == 0:

            err = QMessageBox()
            err.setIcon(QMessageBox.Critical)
            err.setText("ERROR!!Fields cannot be empty...")
            err.setWindowTitle("Warning")
            err.setStandardButtons(QMessageBox.Ok)
            retval = err.exec_()

        elif un == username_login and pa == password_login:
            h1.show()
            m1.close()
        
        else:   
            err = QMessageBox()
            err.setIcon(QMessageBox.Critical)
            err.setText("Invalid login details")
            err.setWindowTitle("Warning")
            err.setStandardButtons(QMessageBox.Ok)
            retval = err.exec_() 
    

    def gotosign(self):
        s1.show()
        m1.close()

class Signup(QDialog):

     def __init__(self):
         super(Signup, self).__init__()
         loadUi("signup.ui",self)
         self.reg_btn.clicked.connect(self.signupfunction)
         self.back_btn.clicked.connect(self.gotologin)


     def signupfunction(self):
        user_name = self.uname_txt.text()
        passw = self.pass_txt.text() 
        cnf_pass = self.cnfpass_txt.text()
        email = self.email_txt.text()
        cp.cursor.execute("Select IF ( EXISTS(Select username from register where username='"+user_name+"'),1,0)")
        result = cp.cursor.fetchone()
        
        if len(user_name) == 0 or len(passw)==0 or len(cnf_pass)==0 or len(email)==0:
            err = QMessageBox()
            err.setIcon(QMessageBox.Critical)
            err.setText("ERROR!!Fields cannot be empty...")
            err.setWindowTitle("Warning")
            err.setStandardButtons(QMessageBox.Ok)
            retval = err.exec_()
        elif result[0] == 1:
            err = QMessageBox()
            err.setIcon(QMessageBox.Critical)
            err.setText("Username already exists !!")
            err.setWindowTitle("Warning")
            err.setStandardButtons(QMessageBox.Ok)
            retval = err.exec_()
        elif passw == cnf_pass:
            sql = "INSERT INTO register (username, password, email) Values(%s,%s,%s)"
            val = (user_name ,passw ,email)
            cp.cursor.execute(sql,val)
            cp.connection.commit()
            err = QMessageBox()
            err.setIcon(QMessageBox.Information)
            err.setText("HURRAH!! Sign Up Successful")
            err.setWindowTitle("Success")
            err.setStandardButtons(QMessageBox.Ok)
            retval = err.exec_()
            m1.show()
            s1.close()
        else:
            err = QMessageBox()
            err.setIcon(QMessageBox.Critical)
            err.setText("Pasword Fields Do Not match..")
            err.setWindowTitle("Warning")
            err.setStandardButtons(QMessageBox.Ok)
            retval = err.exec_()

     def gotologin(self):
        m1.show()
        s1.close()

class Firstpage(QDialog):
    def __init__(self):
         super(Firstpage, self).__init__()
         loadUi("signup.ui",self)

class Homepage(QDialog):
    def __init__(self):
         super(Homepage, self).__init__()
         loadUi("home.ui",self)
         self.readme_btn.clicked.connect(self.gotoreadme)
         self.categories_btn.clicked.connect(self.gotocat)
         self.aboutus_btn.clicked.connect(self.gotoaboutus)
    
    def gotoreadme(self):
        r1.show()
        h1.close()

    def gotocat(self):
        c1.show()
        h1.close()

    def gotoaboutus(self):
        a1.show()
        h1.close()

    

class Readme(QDialog):
   def __init__(self):
       super(Readme, self).__init__()
       loadUi("readme.ui",self)
       self.back_btn.clicked.connect(self.gotohome)

   def gotohome(self):
        h1.show()
        r1.close()


class Categories(QDialog):
   def __init__(self):
       super(Categories, self).__init__()
       loadUi("categories.ui",self)
       self.spiri_btn.clicked.connect(self.gotospiri)
       self.mystery_btn.clicked.connect(self.gotomystery)
       self.horror_btn.clicked.connect(self.gotohorror)
       self.scifi_btn.clicked.connect(self.gotoscifi)

   def gotospiri(self):
        sp.show()
        c1.close()

   def gotomystery(self):
        my.show()
        c1.close()

   def gotohorror(self):
        ho.show()
        c1.close()

   def gotoscifi(self):
        sc.show()
        c1.close()

class Spirituality(QDialog):
   def __init__(self):
       super(Spirituality, self).__init__()
       loadUi("spirituality.ui",self)
       self.buy_btn.clicked.connect(self.gotocheckout)
       self.buy_btn_2.clicked.connect(self.gotocheckout)
       self.buy_btn_3.clicked.connect(self.gotocheckout)
       self.buy_btn_4.clicked.connect(self.gotocheckout)

   def gotocheckout(self):
        ck.show()
        sp.close()

class Mystery(QDialog):
   def __init__(self):
       super(Mystery, self).__init__()
       loadUi("mystery.ui",self)
       self.m_buy_btn.clicked.connect(self.gotocheckout)
       self.m_buy_btn_2.clicked.connect(self.gotocheckout)
       self.m_buy_btn_3.clicked.connect(self.gotocheckout)
       self.m_buy_btn_4.clicked.connect(self.gotocheckout)

   def gotocheckout(self):
        ck.show()
        my.close()

class Horror(QDialog):
   def __init__(self):
       super(Horror, self).__init__()
       loadUi("horror.ui",self)
       self.h_buy_btn.clicked.connect(self.gotocheckout)
       self.h_buy_btn_2.clicked.connect(self.gotocheckout)
       self.h_buy_btn_3.clicked.connect(self.gotocheckout)
       self.h_buy_btn_4.clicked.connect(self.gotocheckout)

   def gotocheckout(self):
        ck.show()
        ho.close()

class Scifi(QDialog):
   def __init__(self):
       super(Scifi, self).__init__()
       loadUi("scifi.ui",self)
       self.s_buy_btn.clicked.connect(self.gotocheckout)
       self.s_buy_btn_2.clicked.connect(self.gotocheckout)
       self.s_buy_btn_3.clicked.connect(self.gotocheckout)
       self.s_buy_btn_4.clicked.connect(self.gotocheckout)

   def gotocheckout(self):
        ck.show()
        sc.close()


class Aboutus(QDialog):
   def __init__(self):
       super(Aboutus, self).__init__()
       loadUi("aboutus.ui",self)
       self.back_btn.clicked.connect(self.gotohome)

   def gotohome(self):
        h1.show()
        a1.close()

class Checkout(QDialog):
   def __init__(self):
       super(Checkout, self).__init__()
       loadUi("checkout.ui",self)
       self.next_btn.clicked.connect(self.gotocard)

   def gotocard(self):
        cd.show()
        ck.close()

class Card(QDialog):
   def __init__(self):
       super(Card, self).__init__()
       loadUi("card.ui",self)
       self.pay_btn.clicked.connect(self.gotothankyou)

   def gotothankyou(self):
        ty.show()
        cd.close()

class Thankyou(QDialog):
   def __init__(self):
       super(Thankyou, self).__init__()
       loadUi("thankyou.ui",self)
       self.logout_btn.clicked.connect(self.gotologin)

   def gotologin(self):
        m1.show()
        ty.close()


    
       

app = QApplication(sys.argv)

#Declaring Objects

f1 = Firstpage()
m1 = login()
s1 = Signup()
h1 = Homepage()
c1 = Categories()
r1 = Readme()
a1 = Aboutus()
sp = Spirituality()
my = Mystery()
ho = Horror()
sc = Scifi()
ck = Checkout()
cd = Card()
ty = Thankyou()



m1.show()
app.exec_()
