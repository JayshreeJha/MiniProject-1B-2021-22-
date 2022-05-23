from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import pymysql
import re

#root=Tk()
class page1:
    
    
    def __init__(self,root):
        self.root = root
        self.root.title("Home Page")
        self.root.configure(width=500,height=300)
        self.root.configure(bg='lightyellow')

        self.product_name="Cello Ball Pen Blue"
        self.quantity="8"
        self.price="90"

        self.product_name1="Spiral Books 200 Pages"
        self.quantity1="4"
        self.price1="400"

        self.product_name2="Camlin  Watercolor"
        self.quantity2="1"
        self.price2="200"

        self.product_name3="Camlin  Boardmarkers Red,Blue,Black"
        self.quantity3="3"
        self.price3="150"

        self.product_name4="Box File"
        self.quantity4="4"
        self.price4="200"

        self.product_name5="Faber-Castell Glue"
        self.quantity5="3"
        self.price5="75"

        

        frame1 = Frame(self.root, bg="orange")
        frame1.place(x=0, y=150, width=1600, height=1000)

        frame2 = Frame(self.root, bg="orange")
        frame2.place(x=100, y=180, width=250, height=250)
        addtocart = Button(self.root, text = 'Add to Cart',bg='grey',fg='black',command=self.addtocart).place(x=100,y=430,width=250,height=50)

        frame3 = Frame(self.root, bg="orange")
        frame3.place(x=600, y=180, width=250, height=250)
        addtocart1 = Button(self.root, text = 'Add to Cart',bg='grey',fg='black',command=self.addtocart1).place(x=600,y=430,width=250,height=50)

        frame4 = Frame(self.root, bg="orange")
        frame4.place(x=1100, y=180, width=250, height=250)
        addtocart2 = Button(self.root, text = 'Add to Cart',bg='grey',fg='black',command=self.addtocart2).place(x=1100,y=430,width=250,height=50)

        frame5 = Frame(self.root, bg="orange")
        frame5.place(x=100, y=500, width=250, height=250)
        addtocart3 = Button(self.root, text = 'Add to Cart',bg='grey',fg='black',command=self.addtocart3).place(x=100,y=750,width=250,height=50)
        

        frame6 = Frame(self.root, bg="orange")
        frame6.place(x=600, y=500, width=250, height=250)
        addtocart4 = Button(self.root, text = 'Add to Cart',bg='grey',fg='black',command=self.addtocart4).place(x=600,y=750,width=250,height=50)

        frame7 = Frame(self.root, bg="orange")
        frame7.place(x=1100, y=500, width=250, height=250)
        addtocart5 = Button(self.root, text = 'Add to Cart',bg='grey',fg='black',command=self.addtocart5).place(x=1100,y=750,width=250,height=50)

        searchproduct = Button(self.root, text = 'Search Product',bg='grey',fg='black').place(x=100,y=50,width=200,height=50)
        searchproduct_entry = Entry(self.root, font=("times new roman", 15), bg="lightgrey").place(x=320,y=50,width=500,height=50)

#addtocart = Button(root, text = 'Add to Cart',bg='grey',fg='black').place(x=100,y=175,width=200,height=50)

#pay = Button(root, text = 'Make Payment',bg='grey',fg='black').place(x=100,y=50,width=200,height=50)

        logout= Button(self.root, text = 'Log out',bg='grey',fg='black',command=self.lg).place(x=1000,y=50,width=200,height=50)

        cart=Button(self.root,text = 'Cart',bg='grey',fg='black',command=self.cart_window,cursor="hand2").place(x=1250,y=50,width=200,height=50)

   
                       

        self.btn_img = ImageTk.PhotoImage(Image.open("images/pens.jpg"))
        mylabel = Label(frame2, image = self.btn_img)
        mylabel.pack()

        self.btn_img1 = ImageTk.PhotoImage(Image.open("images/notebooks.jpg"))
        mylabel1 = Label(frame3, image = self.btn_img1)
        mylabel1.pack()

        self.btn_img2 = ImageTk.PhotoImage(Image.open("images/watercolours.jpg"))
        mylabel2 = Label(frame4, image = self.btn_img2)
        mylabel2.pack()

        self.btn_img3 = ImageTk.PhotoImage(Image.open("images/boardmarkers.jpg"))
        mylabel3 = Label(frame5, image = self.btn_img3)
        mylabel3.pack()

        self.btn_img4 = ImageTk.PhotoImage(Image.open("images/boxfile.jpg"))
        mylabel4 = Label(frame6, image = self.btn_img4)
        mylabel4.pack()

        self.btn_img5 = ImageTk.PhotoImage(Image.open("images/glue.jpg"))
        mylabel5 = Label(frame7, image = self.btn_img5)
        mylabel5.pack()

        pens = Label(frame1, text="Cello Ball Pen Blue\n Rupees 90.00 \n pack of 8", font=("times new roman",15), bg="lightyellow", fg="black").place(x=360, y=100)
        notebook= Label(frame1, text="Spiral Books 200 Pages\n Rupees 400.00 \n pack of 4", font=("times new roman",15), bg="lightyellow", fg="black").place(x=860, y=100)
        watercolours= Label(frame1, text="Camlin  Watercolor \nTube-5ml\n Rupees 200.00 \n 12 Shades", font=("times new roman",15), bg="lightyellow", fg="black").place(x=1360, y=100)
        boardmarkers= Label(frame1, text="Camlin  Boardmarkers\n Rupees 150.00 \n Black,Blue,Red", font=("times new roman",15), bg="lightyellow", fg="black").place(x=360, y=400)
        boxfile= Label(frame1, text="Box File\n Rupees 200.00 \n Set of 4", font=("times new roman",15), bg="lightyellow", fg="black").place(x=860, y=400)
        glue= Label(frame1, text="Faber-Castell Glue\n Rupees 75.00 \n pack of 3", font=("times new roman",15), bg="lightyellow", fg="black").place(x=1360, y=400)
    

        

    def addtocart(self) :
        con=pymysql.connect(host="localhost",user="root",password="",database="cart")
        cur=con.cursor()
        cur.execute("insert into products (product_name,quantity,price) values(%s,%s,%s)",
                    (self.product_name,
                    self.quantity,
                    self.price,
                    ))

        con.commit()
        con.close()
        messagebox.showinfo("Success", "Your Product has been Successfully Added", parent=self.root)
       

    def addtocart1(self) :
        con=pymysql.connect(host="localhost",user="root",password="",database="cart")
        cur=con.cursor()
        cur.execute("insert into products (product_name,quantity,price) values(%s,%s,%s)",
                    (self.product_name1,
                    self.quantity1,
                    self.price1,
                    ))

        con.commit()
        con.close()
        messagebox.showinfo("Success", "Your Product has been Successfully Added", parent=self.root)
       

    def addtocart2(self) :
        con=pymysql.connect(host="localhost",user="root",password="",database="cart")
        cur=con.cursor()
        cur.execute("insert into products (product_name,quantity,price) values(%s,%s,%s)",
                    (self.product_name2,
                    self.quantity2,
                    self.price2,
                    ))

        con.commit()
        con.close()
        messagebox.showinfo("Success", "Your Product has been Successfully Added", parent=self.root)
       

    def addtocart3(self) :
        con=pymysql.connect(host="localhost",user="root",password="",database="cart")
        cur=con.cursor()
        cur.execute("insert into products (product_name,quantity,price) values(%s,%s,%s)",
                    (self.product_name3,
                    self.quantity3,
                    self.price3,
                    ))

        con.commit()
        con.close()
        messagebox.showinfo("Success", "Your Product has been Successfully Added", parent=self.root)
        
        
    def addtocart4(self) :
        con=pymysql.connect(host="localhost",user="root",password="",database="cart")
        cur=con.cursor()
        cur.execute("insert into products (product_name,quantity,price) values(%s,%s,%s)",
                    (self.product_name4,
                    self.quantity4,
                    self.price4,
                    ))

        con.commit()
        con.close()
        messagebox.showinfo("Success", "Your Product has been Successfully Added", parent=self.root)
        

    def addtocart5(self) :
        con=pymysql.connect(host="localhost",user="root",password="",database="cart")
        cur=con.cursor()
        cur.execute("insert into products (product_name,quantity,price) values(%s,%s,%s)",
                    (self.product_name5,
                    self.quantity5,
                    self.price5,
                    ))

        con.commit()
        con.close()
        messagebox.showinfo("Success", "Your Product has been Successfully Added", parent=self.root)
        

    def cart_window(self):
        self.root.destroy()
        import cart         

    def lg(self):
        self.root.destroy()
        import login
#home.destroy()

root=Tk()
obj=page1(root)
root.mainloop()