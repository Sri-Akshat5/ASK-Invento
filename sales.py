from cgitb import text
from email import message
from email.headerregistry import Address
from msilib.schema import Error
from operator import ge, index
from re import search
from select import select
from textwrap import fill
from tkinter import*
from tkinter import ttk, messagebox
from tkinter import font
from tokenize import Name
from turtle import bgcolor, right, st, title, width
import sqlite3
import os
#from typing_extensions import Required
from webbrowser import get
#from PIL import Image, ImageTk 
class salesClass:
    def __init__(self,root):
        self.root=root
        product_Frame=root
        product_Frame.geometry("1100x500+220+130")
        #product_Frame.title("Inventory") #Title
        product_Frame.focus_force()
        product_Frame.config(bg="#E0EEEE")

############################################################################################3
        self.var_searchby=StringVar()
        self.var_searchtext=StringVar()

        self.var_invoice=StringVar()
        self.var_sup=StringVar()
        self.bill_list=[]
 #*****************Title****************
        lbl_title=Label(self.root, text="View Customer Bill", font=("goudy old style", 30),bg="#184a45", fg="white", bd=3, relief=RIDGE).pack(side=TOP, fill=X, padx=10, pady=20)
        lbl_invoice=Label(self.root, text="Invoice No.", font=("goudy old style", 15),bg="White").place(x=50,y=100)
      
        txt_invoice=Entry(self.root, textvariable=self.var_invoice, font=("goudy old style", 18),bg="Light yellow").place(x=160,y=100, width=180, height=28)
       
       # btn_add=Button(self.root, text="ADD", font=("goudy old style", 18),bg="Green", fg="white", cursor="hand2").place(x=360,y=170, width=150, height=30)
        #btn_delete=Button(self.root, text="Delete", font=("goudy old style", 18),bg="Red", fg="white", cursor="hand2").place(x=520,y=170, width=150, height=30)

#**********Button***************
        btn_search=Button(product_Frame, text="Search",command=self.search, font=("goudy old style",15),bg="#2196f3", fg="white", cursor="hand2").place(x=360, y=100, width=120, height=28)
        btn_clear=Button(product_Frame, text="Clear",command=self.clear, font=("goudy old style",15),bg="#4caf50", fg="white", cursor="hand2").place(x=490, y=100, width=120, height=28)

        ''' #*******Search frame***********************
        SaleFreame=LabelFrame(self.root, text="Search Invoice ", font=("goudy old style",12,"bold"), bg="white", relief=RIDGE)
        SaleFreame.place(x=480, y=10, width=600, height=80)

        #****options *******
        cmb_search=ttk.Combobox(SaleFreame,textvariable=self.var_searchby,values=("Select","Category", "Supplier", "Name"),state='readonly',justify=CENTER, font=("goudy old style",15))
        cmb_search.place(x=10,y=10,width=180)
        cmb_search.current(0)'''

#***********BILL LIST******************
        Sale_Freame=Frame(self.root, bd=3, relief=RIDGE)
        Sale_Freame.place(x=50, y=140, width=200, height=330)
        
        scrolly=Scrollbar(Sale_Freame, orient=VERTICAL)
        scrollx=Scrollbar(Sale_Freame, orient=HORIZONTAL)
        self.sale_list=Listbox(Sale_Freame, font=("goudy old style",15),bg="white",yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
        
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.sale_list.xview)
        scrolly.config(command=self.sale_list.yview)
        self.sale_list.pack(fill=BOTH, expand=1)
        self.sale_list.bind("<ButtonRelease-1>",self.get_data)

#**************BILL AREA*****************
        Bill_Freame=Frame(self.root,bg="white", bd=3, relief=RIDGE)
        Bill_Freame.place(x=280, y=140, width=410, height=330)

        lbl_title2=Label(Bill_Freame, text="Customer Bills Area",font=("goudy old style",20), bg="orange").pack(side=TOP, fill=X)
        scrolly2=Scrollbar(Bill_Freame, orient=VERTICAL)
        scrollx2=Scrollbar(Bill_Freame, orient=HORIZONTAL)
        self.Bill_Freame=Text(Bill_Freame,  bg="light yellow", yscrollcommand=scrolly2.set, xscrollcommand=scrollx2.set)
        self.Bill_Freame.pack(fill=BOTH, expand=1)
        scrollx2.pack(side=BOTTOM, fill=X)
        scrolly2.pack(side=RIGHT, fill=Y)
        scrollx2.config(command=self.Bill_Freame.xview)
        scrolly2.config(command=self.Bill_Freame.yview)
        self.show()
#********************************************************************************************************8
    def show(self):
        del self.bill_list[:]
        self.sale_list.delete(0,END)
        for i in os.listdir('Bill'):
        #print(os.listdir('Bill'))
            if i.split('.')[-1]=='txt':
                self.sale_list.insert(END, i)
                self.bill_list.append(i.split('.')[0])

    def get_data(self,ev):
        index_=self.sale_list.curselection()
        file_name=self.sale_list.get(index_)
        print(file_name)
        self.Bill_Freame.delete('1.0',END)
        fp=open(f'Bill/{file_name}','r')
        for i in fp:
                self.Bill_Freame.insert(END,i)
        fp.close

#******************************************************************
    def search(self):
        if self.var_invoice.get()=="":
            messagebox.showerror("Error", "Invoice no.  must be Required",parent=self.root)
        else:
            if self.var_invoice.get() in self.bill_list:
                fp=open(f'Bill/{self.var_invoice.get()}.txt','r')
                self.Bill_Freame.delete('1.0',END)
                for i in fp:
                        self.Bill_Freame.insert(END,i)
                fp.close
            else:
                messagebox.showerror("Error", "Invalid invoice no ",parent=self.root)
#****************************************************************************
    def clear(self):
            self.show()
            self.Bill_Freame.delete('1.0',END)

if __name__=="__main__":
    root=Tk()
    obj=salesClass(root)
    root.mainloop()