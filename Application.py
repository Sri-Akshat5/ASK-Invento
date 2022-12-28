from cgitb import text
from itertools import product
from msilib.schema import Font
from this import d
from time import time
from tkinter import*
from tkinter import ttk, messagebox
from time import strftime
from unicodedata import category
from wsgiref.simple_server import software_version
from tkinter import messagebox
import sqlite3
import os
from billing import billingClass
from employee import employeeClass
from supplier import supplierClass
from pro_Category import categoryClass
from product import productClass
from sales import salesClass
from billing import billingClass
from datetime import datetime
#import pytz

#from PIL import Image, ImageTk 
class IMS:

    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("ASK Invento") #Title
        self.root.config(bg="#E0EEEE")

        #************Heading************
        self.icon_title=PhotoImage(file="E:\Amity BCA+MCA Notes\Semester 4 2022-2022\Python Programming - CSIT232\Project\IMS\Background8.png")
        title=Label(self.root,text="ASK Invento", image=self.icon_title, compound=LEFT,font=("Goudy old style",40,"bold"),bg="black",fg="white",anchor="w", padx="3" ).place(x=0, y=0, relwidth=1)
        sub_title=Label(self.root,text="Knocking out your inventory needs",  compound=LEFT,font=("Goudy old style",15),bg="black",fg="white").place(x=378, y=25)
        hy_title=Label(self.root,text="-",  compound=LEFT,font=("times new roman",25),bg="black",fg="white").place(x=350, y=15)

       


        #************Button_LOGOUT*************
       # btn_logout=Button(self.root, text="Logout",font=("times new roman",15, "bold"),bg="yellow",cursor="hand2").place(x=1150, y=20, height=30, width=150)

        #******Clock****************************
        #IST=pytz.timezone("Asia/kolkata")
        software_version="v1.1"

        self.lbl_clock_=Label(self.root,text="\t\t\t\t\t\t\tASK Inventory Management System\t\t\t\t \t\t\t\t   ",font=("times new roman",15),bg="gray",fg="black")
        self.lbl_clock_.place(x=0, y=67)

        #************Left Menu*******************
        #self.left.menuLogo=Image.open("")
        LeftMenu=Frame(self.root, bd=2, relief=RIDGE,bg="#E0EEEE")
        LeftMenu.place(x=0, y=102, width=200, height=565)

        lbl_menu=Button(LeftMenu, text="Menu",font=("times new roman",20, "bold"),bg="Blue", cursor="hand2").pack(side=TOP, fill=X)
        btn_emp=Button(LeftMenu, text="Employee",command=self.employee,font=("times new roman",20, "bold"),bg="White", bd=3 ,cursor="hand2").pack(side=TOP, fill=X)
        btn_Sup=Button(LeftMenu, text="Supplier",command=self.supplier,font=("times new roman",20, "bold"),bg="White", bd=3 ,cursor="hand2").pack(side=TOP, fill=X)
        btn_Cat=Button(LeftMenu, text="Category",command=self.pro_category,font=("times new roman",20, "bold"),bg="White", bd=3 ,cursor="hand2").pack(side=TOP, fill=X)
        btn_pro=Button(LeftMenu, text="Product",command=self.product, font=("times new roman",20, "bold"),bg="White", bd=3 ,cursor="hand2").pack(side=TOP, fill=X)
        btn_Sale=Button(LeftMenu, text="Sales",command=self.sales, font=("times new roman",20, "bold"),bg="White", bd=3 ,cursor="hand2").pack(side=TOP, fill=X)
        btn_Billing=Button(LeftMenu, text="Billing",command=self.billing, font=("times new roman",20, "bold"),bg="White", bd=3 ,cursor="hand2").pack(side=TOP, fill=X)

         #******Content****************************
        self.lbl_emp=Label(self.root,text="Total Employee",bd=5,relief=RIDGE,font=("times new roman",15),bg="#FFD39B",fg="black")
        self.lbl_emp.place(x=300, y=120, width=300,height=150,)

        self.lbl_sup=Label(self.root,text="Total Supplies",bd=5,relief=RIDGE,font=("times new roman",15),bg="#FF4040",fg="black")
        self.lbl_sup.place(x=650, y=120, width=300,height=150,)

        self.lbl_cat=Label(self.root,text="Category",bd=5,relief=RIDGE,font=("times new roman",15),bg="#66CD00",fg="black")
        self.lbl_cat.place(x=1000, y=120, width=300,height=150,)

        self.lbl_pro=Label(self.root,text="Total Product",bd=5,relief=RIDGE,font=("times new roman",15),bg="#FF1493",fg="black")
        self.lbl_pro.place(x=300, y=300, width=300,height=150,)

        self.lbl_Sale=Label(self.root,text="Total Sales",bd=5,relief=RIDGE,font=("times new roman",15),bg="#76EEC6",fg="black")
        self.lbl_Sale.place(x=650, y=300, width=300,height=150,)

        #******Footer****************************
        lbl_foot_=Label(self.root,text="ASK | Developed with ♡ by Akshat & Arushi",font=("times new roman",12),bg="grAy",fg="black").pack(side=BOTTOM, fill=X)
        #self.lbl_clock_.place(x=0, y=67, relwidth=1,height=30)
        self.update_contant()
############################################################################################################
    def employee(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=employeeClass(self.new_win)

##############################################################################################################
    def supplier(self): 
            self.new_win=Toplevel(self.root)
            self.new_obj=supplierClass(self.new_win)

 ##############################################################################################################
    def pro_category(self): 
            self.new_win=Toplevel(self.root)
            self.new_obj=categoryClass(self.new_win)

##############################################################################################################
    def product(self): 
            self.new_win=Toplevel(self.root)
            self.new_obj=productClass(self.new_win)

#############################################################################################################
    def sales(self): 
            self.new_win=Toplevel(self.root)
            self.new_obj=salesClass(self.new_win)

#############################################################################################################
    def billing(self): 
            self.new_win=Toplevel(self.root)
            self.new_obj=billingClass(self.new_win)

#######################################################################################################################
    def update_date_time(self):
        lbl_clock_=strftime("%H: %M: %S")
        date_=strftime("%d-%b-%Y")
        self.lbl_clock_.config(text=lbl_clock_ )
        self.lbl_clock_.after(1000, self.update_date_time)
#########################################################################################################

    def update_contant(self):
        con=sqlite3.connect(database="ims1.db")
        cur=con.cursor()
        try:
            cur.execute("Select * from product")
            product=cur.fetchall()
            self.lbl_pro.config(text=f'Total product \n[ {str(len(product))}]')

            cur.execute("Select * from supplier")
            supplier=cur.fetchall()
            self.lbl_sup.config(text=f'Total supplier \n[ {str(len(supplier))}]')

            cur.execute("Select * from category")
            category=cur.fetchall()
            self.lbl_cat.config(text=f'Total Category \n[ {str(len(category))}]')

            cur.execute("Select * from employee")
            employee=cur.fetchall()
            self.lbl_emp.config(text=f'Total Employee \n[ {str(len(employee))}]')
            bill=len(os.listdir('Bill'))
            self.lbl_Sale.config(text=f'Total Sales\n[{str(bill)}]')

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}")

if __name__=="__main__":
    root=Tk()
    obj=IMS(root)
    root.mainloop()
