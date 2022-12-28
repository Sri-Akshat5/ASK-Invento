from cProfile import label
from cgitb import text
from filecmp import clear_cache
from importlib import import_module
from msilib.schema import Font
from operator import index
from tkinter import *
from tkinter import ttk, messagebox
from tkinter import font
import time
from turtle import left, width
from unittest import result
from employee import employeeClass
from supplier import supplierClass
from pro_Category import categoryClass
from product import productClass
from sales import salesClass
import os
import tempfile
import sqlite3
#from PIL import Image, ImageTk 
class billingClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("ASK Invento") #Title
        self.root.config(bg="#E0EEEE")
        self.chk_print=0
        self.cart_list=[]
        #************Heading************
        self.icon_title=PhotoImage(file="E:\Amity BCA+MCA Notes\Semester 4 2022-2022\Python Programming - CSIT232\Project\IMS\Background8.png")
        title=Label(self.root,text="ASK Invento", image=self.icon_title, compound=LEFT,font=("Goudy old style",40,"bold"),bg="black",fg="white",anchor="w", padx="3" ).place(x=0, y=0, relwidth=1)
        sub_title=Label(self.root,text="Knocking out your inventory needs",  compound=LEFT,font=("Goudy old style",15),bg="black",fg="white").place(x=378, y=25)
        hy_title=Label(self.root,text="-",  compound=LEFT,font=("times new roman",25),bg="black",fg="white").place(x=350, y=15)
        #************Button_LOGOUT*************
       # btn_logout=Button(self.root, text="Logout",font=("times new roman",15, "bold"),bg="yellow",cursor="hand2").place(x=1150, y=20, height=30, width=150)
        #******Clock****************************
        self.lbl_clock_=Label(self.root,text="\t\t\t\t\t\t\tASK Inventory Management System\t\t\t\t \t\t\t\t   ",font=("times new roman",15),bg="gray",fg="black")
        self.lbl_clock_.place(x=0, y=67, relwidth=1,height=30)

#*************Product Frame****************************
        
        productFrame=Frame(self.root, bd=4, relief=RIDGE, bg="white")
        productFrame.place(x=6, y=110, width=410, height=550)

        pTitle=Label(productFrame, text="All product", font=("goudy old style",20,"bold"), bg="#262626", fg="white").pack(side=TOP,fill=X)
#***************************************************************
        self.var_search=StringVar()
        productFrame1=Frame(productFrame, bd=2, relief=RIDGE, bg="white")
        productFrame1.place(x=2, y=42, width=398, height=90)

        
        lbl_search=Label(productFrame1, text="Search product | By Name", font=("Times new roman",15,"bold"), bg="white", fg="green").place(x=2, y=5)

        lbl_search=Label(productFrame1, text="Product name", font=("Times new roman",15,"bold"), bg="white").place(x=5, y=45)
        txt_search=Entry(productFrame1, textvariable=self.var_search, font=("Times new roman",15), bg="lightyellow", fg="green").place(x=128, y=49, width=150, height=22)
        btn_search=Button(productFrame1, text="Search",command=self.search, font=("Goudy old style",15), bg="#2196f3", fg="white", cursor="hand2").place(x=286, y=49, width=100, height=22)
        btn_show_all=Button(productFrame1, text="Show All",command=self.show, font=("Goudy old style",15), bg="#083531", fg="white", cursor="hand2").place(x=286, y=10, width=100, height=22)

        
        #*******Bill DETAILS*************
        productFrame2=Frame(productFrame, bd=3, relief=RIDGE)
        productFrame2.place(x=2, y=140, width=398, height=380)

        scrolly=Scrollbar(productFrame2, orient=VERTICAL)
        scrollx=Scrollbar(productFrame2, orient=HORIZONTAL)

        self.product_table=ttk.Treeview(productFrame2, columns=("pid", "name", "price", "qty", "status"),yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=X)
        scrollx.config(command=self.product_table.xview)
        scrolly.config(command=self.product_table.yview)

        self.product_table.heading("pid", text="Product ID")
        self.product_table.heading("name", text="Name")
        self.product_table.heading("price", text="Price")
        self.product_table.heading("qty", text="Quantity")
        self.product_table.heading("status", text="Status")
        
       
        self.product_table["show"]="headings"
        

        self.product_table.column("pid",width=50)
        self.product_table.column("name", width=100)
        self.product_table.column("price", width=100)
        self.product_table.column("qty",width=100)
        self.product_table.column("status",width=100)
        self.product_table.pack(fill=BOTH, expand=1)

        self.product_table.bind("<ButtonRelease-1>",self.get_data)

        lbl_note=Label(productFrame, text="Note: 'Enter 0 quantity to remove product from the cart'",font=("Goudy old style",10), bg="White", fg="red", anchor="w").pack(side=BOTTOM, fill=X)


        #********Customer Frame******************************
        self.var_name=StringVar()
        self.var_contact=StringVar()
        customerFrame=Frame(self.root, bd=4, relief=RIDGE, bg="white")
        customerFrame.place(x=420, y=110, width=520, height=70)

        cTitle=Label(customerFrame, text="Customer Details", font=("goudy old style",15), bg="light gray").pack(side=TOP,fill=X)

        lbl_name=Label(customerFrame, text="Name", font=("Times new roman",15), bg="white").place(x=7, y=35)
        txt_name=Entry(customerFrame, textvariable=self.var_name, font=("Times new roman",15), bg="lightyellow", fg="green").place(x=60, y=35, width=180)

        lbl_contact=Label(customerFrame, text="Contact No.", font=("Times new roman",15), bg="white").place(x=260, y=35)
        txt_contact=Entry(customerFrame, textvariable=self.var_contact, font=("Times new roman",15), bg="lightyellow", fg="green").place(x=360, y=35, width=150)

   #***************CAL_CART_FRAME******************************     
        Cal_Cart_Frame=Frame(self.root, bd=2, relief=RIDGE, bg="white")
        Cal_Cart_Frame.place(x=420, y=190, width=520, height=360)

#****************CAlCULATOR FRAME*********************************
        self.var_cal_input=StringVar()
        Cal_Frame=Frame(Cal_Cart_Frame, bd=8, relief=RIDGE, bg="white")
        Cal_Frame.place(x=5, y=10, width=268, height=340)

        txt_cal_input=Entry(Cal_Frame, textvariable=self.var_cal_input, font=("arial",15, "bold"), width=21, bd=10, relief=GROOVE, state="readonly")
        txt_cal_input.grid(row=0,columnspan=4)

        btn_7=Button(Cal_Frame, text='7',  font=("arial",15, "bold"),command=lambda:self.get.input, bd=3, width=4, pady=13, cursor="hand2").grid(row=1, column=0)
        btn_8=Button(Cal_Frame, text='8',  font=("arial",15, "bold"), bd=3, width=4, pady=13, cursor="hand2").grid(row=1, column=1)
        btn_9=Button(Cal_Frame, text='9',  font=("arial",15, "bold"), bd=3, width=4, pady=13, cursor="hand2").grid(row=1, column=2)
        btn_sum=Button(Cal_Frame, text='+',  font=("arial",15, "bold"), bd=3, width=4, pady=13, cursor="hand2").grid(row=1, column=3)

        btn_4=Button(Cal_Frame, text='4',  font=("arial",15, "bold"), bd=3, width=4, pady=13, cursor="hand2").grid(row=2, column=0)
        btn_5=Button(Cal_Frame, text='5',  font=("arial",15, "bold"), bd=3, width=4, pady=13, cursor="hand2").grid(row=2, column=1)
        btn_6=Button(Cal_Frame, text='6',  font=("arial",15, "bold"), bd=3, width=4, pady=13, cursor="hand2").grid(row=2, column=2)
        btn_sub=Button(Cal_Frame, text='-',  font=("arial",15, "bold"), bd=3, width=4, pady=13, cursor="hand2").grid(row=2, column=3)

        btn_1=Button(Cal_Frame, text='1',  font=("arial",15, "bold"), bd=3, width=4, pady=13, cursor="hand2").grid(row=3, column=0)
        btn_2=Button(Cal_Frame, text='2',  font=("arial",15, "bold"), bd=3, width=4, pady=13, cursor="hand2").grid(row=3, column=1)
        btn_3=Button(Cal_Frame, text='3',  font=("arial",15, "bold"), bd=3, width=4, pady=13, cursor="hand2").grid(row=3, column=2)
        btn_mul=Button(Cal_Frame, text='*',  font=("arial",15, "bold"), bd=3, width=4, pady=13, cursor="hand2").grid(row=3, column=3)

        btn_0=Button(Cal_Frame, text='0',  font=("arial",15, "bold"), bd=3, width=4, pady=13, cursor="hand2").grid(row=4, column=0)
        btn_c=Button(Cal_Frame, text='C',  font=("arial",15, "bold"), bd=3, width=4, pady=13, cursor="hand2").grid(row=4, column=1)
        btn_eq=Button(Cal_Frame, text='=',  font=("arial",15, "bold"), bd=3, width=4, pady=13, cursor="hand2").grid(row=4, column=2)
        btn_div=Button(Cal_Frame, text='/',  font=("arial",15, "bold"), bd=3, width=4, pady=13, cursor="hand2").grid(row=4, column=3)
#*******CART DETAILS*************
        Cart_Frame=Frame(Cal_Cart_Frame, bd=3, relief=RIDGE)
        Cart_Frame.place(x=278, y=8, width=235, height=342)

        self.cartTitle=Label(Cart_Frame, text="Cart\t  Total Product:[0]", font=("goudy old style",15), bg="light gray")
        self.cartTitle.pack(side=TOP,fill=X)


        scrolly=Scrollbar(Cart_Frame, orient=VERTICAL)
        scrollx=Scrollbar(Cart_Frame, orient=HORIZONTAL)


        self.cart_table=ttk.Treeview(Cart_Frame, columns=("pid", "name", "price", "qty"),yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=X)
        scrollx.config(command=self.cart_table.xview)
        scrolly.config(command=self.cart_table.yview)

        self.cart_table.heading("pid", text="Product ID")
        self.cart_table.heading("name", text="Name")
        self.cart_table.heading("price", text="Price")
        self.cart_table.heading("qty", text="Quantity")
        
        
       
        self.cart_table["show"]="headings"
        self.cart_table.pack(fill=BOTH, expand=1)

        self.cart_table.column("pid",width=80)
        self.cart_table.column("name", width=100)
        self.cart_table.column("price", width=90)
        self.cart_table.column("qty",width=55)
      
        self.cart_table.bind("<ButtonRelease-1>",self.get_data_cart)


#*******************ADD Cart Frame*************
        self.var_pid=StringVar()
        self.var_pname=StringVar()
        self.var_price=StringVar()
        self.var_qty=StringVar()
        self.var_ststus=StringVar()
        self.var_stock=StringVar()

        Cart_Button_Frames=Frame(self.root, bd=3, relief=RIDGE, bg="white")
        Cart_Button_Frames.place(x=419, y=550, width=521, height=110)

        lbl_p_name=Label(Cart_Button_Frames, text="Product Name",font=("goudy old style",15), bg="White").place(x=5, y=5) 
        txt_p_name=Entry(Cart_Button_Frames, textvariable=self.var_pname,font=("goudy old style",15), bg="light yellow", state='readonly').place(x=5, y=35, width=190, height=22) 

        lbl_p_price=Label(Cart_Button_Frames, text="Price Per Qty",font=("goudy old style",15), bg="White").place(x=230, y=5) 
        txt_p_price=Entry(Cart_Button_Frames, textvariable=self.var_price,font=("goudy old style",15), bg="light yellow", state='readonly').place(x=230, y=35, width=125, height=22) 
       
        lbl_p_qty=Label(Cart_Button_Frames, text="Quantity",font=("goudy old style",15), bg="White").place(x=390, y=5) 
        txt_p_qty=Entry(Cart_Button_Frames, textvariable=self.var_qty,font=("goudy old style",15), bg="light yellow").place(x=390, y=35, width=120, height=22) 

        self.lbl_instock=Label(Cart_Button_Frames, text="In Stock",font=("goudy old style",15), bg="White")
        self.lbl_instock.place(x=5, y=70) 

        btn_clear_cart=Button(Cart_Button_Frames, text="Clear",command=self.clear_cart, font=("goudy old style",15), bg="light gray",cursor="hand2").place(x=180, y=70, width=150, height=30) 
        btn_add_cart=Button(Cart_Button_Frames, text="Add | Update",command=self.add_update, font=("goudy old style",15), bg="orange",cursor="hand2").place(x=340, y=70, width=150, height=30) 

        #********Billing Area******************
        billFrame=Frame(self.root, bd=2,relief=RIDGE, bg="White")
        billFrame.place(x=945, y=110, width=400, height=410)

        bTitle=Label(billFrame, text="Customer Bill",font=("goudy old style",15), bg="#262626", fg="White").pack(side=TOP, fill=X) 
        scrolly=Scrollbar(billFrame, orient=VERTICAL)
        scrolly.pack(side=RIGHT, fill=Y)

        self.txt_billarea=Text(billFrame,yscrollcommand=scrolly.set)
        self.txt_billarea.pack(fill=BOTH, expand=1)
        scrolly.config(command=self.txt_billarea.yview)
        #++++++++Billing Button**************************

        bill_MenuFrame=Frame(self.root, bd=2,relief=RIDGE, bg="White")
        bill_MenuFrame.place(x=945, y=520, width=400, height=140)

        self.lbl_amt=Label(bill_MenuFrame, text="Bill Amount\n [0]", font=("goudy old style",15,"bold"), bg="#3f51b5", fg="white")
        self.lbl_amt.place(x=2, y=5, width=120, height=70)

        self.lbl_disc=Label(bill_MenuFrame, text="Discount\n [5%]", font=("goudy old style",15,"bold"), bg="#3f61b5", fg="white")
        self.lbl_disc.place(x=124, y=5, width=120, height=70)

        self.lbl_npay=Label(bill_MenuFrame, text="Net Pay\n [0]", font=("goudy old style",15,"bold"), bg="#3c51b5", fg="white")
        self.lbl_npay.place(x=246, y=5, width=147, height=70)

        btn_print=Button(bill_MenuFrame, text="Print\n [0]",command=self.print_bill, font=("goudy old style",12,"bold"), bg="#456780", fg="white", cursor="hand2")
        btn_print.place(x=2, y=80, width=120, height=50)

        btn_clear_all=Button(bill_MenuFrame, text="Clear All",command=self.clear_all, font=("goudy old style",12,"bold"), bg="green", fg="white", cursor="hand2")
        btn_clear_all.place(x=124, y=80, width=120, height=50)

        btn_gen=Button(bill_MenuFrame, text="Generate/Save Bill",command=self.generate_bill, font=("goudy old style",12,"bold"), bg="Red", fg="white", cursor="hand2")
        btn_gen.place(x=246, y=80, width=147, height=50)

        

        lbl_foot_=Label(self.root,text="ASK | Developed with ♡ by Akshat & Arushi",font=("times new roman",12),bg="grAy",fg="black").pack(side=BOTTOM, fill=X)

        self.show()
        self.bill_top()
        self.bill_mid()
        #self.bill_bot()
#***********All Funcation***********************************************
    def get_input(self,num):
        xnum=self.var_cal_input.get()+str(num)
        self.var_cal_input.set(xnum)
    def clear_cal(self,num):
        #xnum=self.var_cal_input.get()+str(num)
        self.var_cal_input.set('')
    def perform_cqla(self,num):
        result=self.var_cal_input.get()

        self.var_cal_input.set(eval(result))

    def show(self):
        con=sqlite3.connect(database="ims1.db")
        cur=con.cursor()
        try:
           # self.product_table=ttk.Treeview(productFrame2, columns=("pid", "name", "price", "qty", "status"),yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
            cur.execute("select pid, name, price, qty, status from product")
            rows=cur.fetchall()
            self.product_table.delete(*self.product_table.get_children())
            for row in rows:
                self.product_table.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)
     #***********************************************************************************   
    def search(self):
        con=sqlite3.connect(database="ims1.db")
        cur=con.cursor()
        try:
            if self.var_search.get()=="":
                messagebox.showerror("Error","Search input required")
            
            else:
                cur.execute("select pid, name, price, qty, status from product where name LIKE '%"+self.var_search.get()+"%' ")
                rows=cur.fetchall()
                if len(rows)!=0:

                    self.product_table.delete(*self.product_table.get_children())
                    for row in rows:
                        self.product_table.insert('',END,values=row)
                else:
                    messagebox.showerror("Error","No record found", parents=self.root)

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)

    def get_data(self,ev):
        f=self.product_table.focus()
        content=(self.product_table.item(f))
        row=content['values']
        self.var_pid.set(row[0])
        self.var_pname.set(row[1])
        self.var_price.set(row[2])
        #self.var_qty.set(row[3])
        self.lbl_instock.config(text=f"In Stock [{str(row[3])}]")
        self.var_stock.set(row[3])
        self.var_qty.set('1')


    def get_data_cart(self,ev):
        f=self.cart_table.focus()
        content=(self.cart_table.item(f))
        row=content['values']
        self.var_pid.set(row[0])
        self.var_pname.set(row[1])
        self.var_price.set(row[2])
        self.var_qty.set(row[3])
        self.lbl_instock.config(text=f"In Stock [{str(row[4])}]")
        self.var_stock.set(row[4])
        #self.var_qty.set(row[3])

#*******************************************
    def add_update(self):
        if self.var_pid.get()=="":
             messagebox.showerror('Error',"Product is required", parent=self.root)   
        elif self.var_qty.get()=='':
             messagebox.showerror('Error',"Quanity is required", parent=self.root)
        elif int(self.var_qty.get())>int(self.var_stock.get()):
             messagebox.showerror('Error',"Invalid Quanity ", parent=self.root)
        else:
             #price_cal=float(int(self.var_qty.get())*float(self.var_price.get()))
             #pid, name, price, qty, status
             
             price_cal=self.var_price.get()
             cart_data=[self.var_pid.get(),self.var_pname.get(),price_cal,self.var_qty.get(), self.var_stock.get()]
             
             #print(self.cart_list)
             #*********************UPDATE CART********************
             present="no"
             index_=0
             for row in self.cart_list:
                if self.var_pid.get()==row[0]:
                        present='yes'
                        break
                index_+=1

             if present =="yes":
                     op=messagebox.askyesno("Confirm","Product already present \n Do you want to Update or remove from cart")
                     if op==True:
                             if self.var_qty.get()=="0":
                                     self.cart_list.pop(index_)
                             else:
                                     #self.cart_list[index_][2]=price_cal
                                     self.cart_list[index_][3]=self.var_qty.get()
             else:
                          self.cart_list.append(cart_data)   

        self.show_cart()
        self.bill_update()
        #self.generate_bill()
#****BILL UPDATE*******************
    def bill_update(self):
        self.bill_amt=0
        self.net_pay=0
        self.desc=0
        for row in self.cart_list:
            self.bill_amt=self.bill_amt+(float(row[2])*int(row[3]))
        self.desc=(self.bill_amt*5)/100
        self.net_pay=self.bill_amt-self.bill_amt-self.desc

        self.lbl_amt.config(text=f"Bill Amount\n{str(self.bill_amt)} ")
        self.lbl_npay.config(text=f"Net Pay\n{str(self.net_pay)} ")
        self.cartTitle.config( text=f"Cart\t  Total Product:[{str(len(self.cart_list))}]")

    #********************************************
    def show_cart(self):
        try:
            self.cart_table.delete(*self.cart_table.get_children())
            for row in self.cart_list:
                self.cart_table.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)
#********************************************************************
    def generate_bill(self):
        if self.var_name.get()=="" or self.var_contact.get()=="":
            messagebox.showerror("Error", f"customer details required")
        elif len(self.cart_list)==0:
            messagebox.showerror("Error", f"Add product required")
        else:
            #*******BILL TOP **************
            self.bill_top()
            #*******BILL MID****************
            self.bill_mid()
            #********BILL BOTTOM****************
            self.bill_bot()
            #pass
            fp=open(f'Bill/{str(self.invoice)}.txt','w')
            fp.write(self.txt_billarea.get('1.0',END))
            fp.close()
            messagebox.showinfo("Saved", "Bill has been generated and saved")
            self.chk_print=1

    def bill_top(self):
        self.invoice=int(time.strftime("%H%M%S"))+int(time.strftime("%d%m%Y"))
        bill_top_temp = f'''
\t\t ASK Invento
\t Phone no. 8181******, Noida-20313
{str("-"*46)}
 Customer Name: {self.var_name.get()}
 ph no.: {self.var_contact.get()}
 Bill No.: {str(self.invoice)}\t\t Date: {str(time.strftime("%d/%m/%y"))}
{str("-"*46)}
 Product Name\t\t Quantity\t Price
{str("-"*46)}
        '''
        self.txt_billarea.delete('1.0',END)
        self.txt_billarea.insert('1.0',bill_top_temp)

    def bill_bot(self):
        bill_bot_temp=f'''
{str("-"*46)}
 Bill Amount \t\t\tRs.{self.bill_amt}
 Discount\t\t\tRs.{self.desc}
 Net Pay\t\t\tRs.{self.net_pay}
{str("-"*46)}\n
        '''
        self.txt_billarea.insert(END,bill_bot_temp)

    def bill_mid(self):
        
             
             for row in self.cart_list:
                
                 pid=row[0]
                 name=row[1]
                 qty=row[3]
                 
                 
                 price=float(row[2]*int(row[3]))
                 price=str(price)
                 self.txt_billarea.insert(END,"\n"+name+"\t\t\t"+qty+"\tRs:"+price)

                 
                 

    def clear_cart(self):
        self.var_pid.set('')
        self.var_pname.set('')
        self.var_price.set('')
        self.var_qty.set('')
        self.lbl_instock.config(text=f"In Stock ")
        self.var_stock.set('')

    def clear_all(self):
        del self.cart_list[:]
        self.var_name.set('')
        self.var_contact.set('')
        self.txt_billarea.delete('1.0', END)
        self.cartTitle.config(text=f"Cart \t Total Product: [0]")
        self.var_search.set('')
        self.clear_cart()
        self.show()
        self.show_cart()

    def print_bill(self):
        if self.chk_print==1:
            messagebox.showinfo("print", "Please wait while printing")
        else:
            messagebox.showinfo("print", "Please generate bill for printing")


if __name__=="__main__":
    root=Tk()
    obj=billingClass(root)
    root.mainloop()
