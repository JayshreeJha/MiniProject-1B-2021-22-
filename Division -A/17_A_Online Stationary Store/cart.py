from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import re
from designer import show
import pymysql
from tkinter import ttk
import tkinter as tk
from tkhtmlview import HTMLLabel


root=tk.Tk()
class cart_window:
    def __init__(self,root):
        self.root = root
        self.root.title("Cart")
        self.root.configure(width=500,height=300)

        frame1 = Frame(self.root, bg="grey")
        frame1.place(x=50, y=50, width=1400, height=1000)
        product_name= Label(self.root, text="Product Name", font=("times new roman", 15, "bold"), bg="white", fg="black").place(x=370, y=220)
        quantity= Label(self.root, text="Quantity", font=("times new roman", 15, "bold"), bg="white", fg="black").place(x=570, y=220)


        pay= Button(self.root, text = 'Pay',bg='white',fg='black').place(x=650,y=700,width=200,height=50)

        show= Button(self.root, text = 'Buy Now',bg='white',fg='black',command=self.show).place(x=650,y=700,width=200,height=50)
        
    def show(root):
        con=pymysql.connect(host="localhost",user="root",password="",database="cart")
        cur=con.cursor()
        cur.execute("select * from products ")

        #tree=ttk.Treeview(root)

        #tree['columns']=("product_name","quantity","price")

        #tree.column("product_name",width=100,minwidth=100,anchor=tk.CENTER)
        #tree.column("quantity",width=50,minwidth=50,anchor=tk.CENTER)
        #tree.column("price",width=50,minwidth=50,anchor=tk.CENTER)

        #tree.heading("product_name",txt="product_name",anchor=tk.CENTER)
        #tree.heading("quantity",txt="quantity",anchor=tk.CENTER)
        #tree.heading("price",txt="price",anchor=tk.CENTER)

        #i=0
        #for root in cur:
            #tree.insert("",i,text="",values=(root[0],root[1],root[2]))
            #i=i+1
        #tree.pack()
        
        
        rows=cur.fetchall()
        print(rows)
       
        print_rows=""
        for row in rows[0]:
            print_rows  += str(row) + "\n" 
            
            query_label =Label(root,text=print_rows)
            query_label.grid(row=100,column=100,columnspan=2)

       
        con.commit()
        con.close()








obj=cart_window(root)
root.mainloop()
#tree=ttk.Treeview(root)
        #tree['show']='headings'

        #s=ttk.Style(root)
        #s.theme_use("clam")
         #tree["columns"]=("product_name","quantity","price")

        #tree.column("product_name",width=100,minwidth=100,anchor=tk.CENTER)
        #tree.column("quantity",width=50,minwidth=50,anchor=tk.CENTER)
        #tree.column("price",width=50,minwidth=50,anchor=tk.CENTER)

        #tree.heading("product_name",txt="product_name",anchor=tk.CENTER)
        #tree.heading("quantity",txt="quantity",anchor=tk.CENTER)
        #tree.heading("price",txt="price",anchor=tk.CENTER)

        #i=0
         #tree.insert("",i,text="",values=(ro[0],ro[1],ro[2]))
            #i=i+1
        #tree.pack()

        #for i,(product_name,quantity,price) in enumerate(row,start=1):
            #listBox.insert("","end",values=(product_name,quantity,price))

