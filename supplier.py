#from cgitb import text
#from msilib.schema import Font
from cgitb import text
from email import message
from email.headerregistry import Address
from operator import ge
from re import search
from tkinter import*
from tkinter import ttk, messagebox
from tkinter import font
from tokenize import Name
from turtle import bgcolor, st, title, width
import sqlite3
#from typing_extensions import Required
from webbrowser import get
#from PIL import Image, ImageTk 
class supplierClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1100x500+220+130")
        #self.root.title("Inventory") #Title
        self.root.focus_force()
        self.root.config(bg="#E0EEEE")
        #**************************************
        #All Variables ****************
        self.var_searchby=StringVar()
        self.var_searchtext=StringVar()

        self.var_sup_invoice=StringVar()
        self.var_name=StringVar()
        self.var_contact=StringVar()
       # self.txt_desc.get('1.0',END),
        
       
#*******Search frame***********************
        SearchFreame=LabelFrame(self.root, text="Search Supplier", font=("goudy old style",12,"bold"), bg="#E0EEEE", relief=RIDGE)
        SearchFreame.place(x=250, y=20, width=600, height=70)

        
        #****options *******
        lbl_search=Label(SearchFreame, text="Search By Invoice No.",bg="white", font=("goudy old style",15))
        lbl_search.place(x=10, y=10)

        txt_search=Entry(SearchFreame, textvariable=self.var_searchtext,font=("goudy old style",15),bg="lightyellow").place(x=200, y=10)
        btn_search=Button(SearchFreame, text="Search", command=self.search, font=("goudy old style",15),bg="green", fg="white", cursor="hand2").place(x=410, y=9, width=150, height=30)

        #********Title**************
        title=Label(self.root, text="Supplier Details",bg="#0f4d7d", font=("goudy old style",15), fg="white",).place(x=50, y=100, width=1000)

        #******** Content**************
        #********Row one****************
        lbl_supplier_invoice=Label(self.root, text="Invoice No: ",bg="White", font=("goudy old style",15)).place(x=50, y=150)
        lbl_supplier_invoice=Entry(self.root, textvariable=self.var_sup_invoice,bg="Light yellow", font=("goudy old style",15)).place(x=150, y=150, width=180)
       
              #***********Row-2*************
        lbl_name=Label(self.root, text="Name: ",bg="White", font=("goudy old style",15)).place(x=50, y=190)
        lbl_name=Entry(self.root, textvariable=self.var_name,bg="Light yellow", font=("goudy old style",15)).place(x=150, y=190, width=180)
               
        
        #***********Row 3*************
        lbl_contact=Label(self.root, text="Contact: ",bg="White", font=("goudy old style",15)).place(x=50, y=230)
        lbl_contact=Entry(self.root, textvariable=self.var_contact,bg="Light yellow", font=("goudy old style",15)).place(x=150, y=230, width=180)
        

        #***********Row 4*************
        lbl_decs=Label(self.root, text="Description: ",bg="White", font=("goudy old style",15)).place(x=50, y=270)
           
        self.txt_desc=Text(self.root, bg="Light yellow", font=("goudy old style",15))
        self.txt_desc.place(x=150, y=270, width=300, height=60)
              

        #*******Button*****************
        btn_add=Button(self.root, text="Save",command=self.add, font=("goudy old style",15),bg="#2196f3", fg="white", cursor="hand2").place(x=500, y=305, width=110, height=28)
        btn_update=Button(self.root, text="Update",command=self.update, font=("goudy old style",15),bg="#4caf50", fg="white", cursor="hand2").place(x=620, y=305, width=110, height=28)
        btn_delete=Button(self.root, text="Delete",command=self.delete, font=("goudy old style",15),bg="#f44336", fg="white", cursor="hand2").place(x=740, y=305, width=110, height=28)
        btn_clear=Button(self.root, text="Clear",command=self.clear, font=("goudy old style",15),bg="#607d8b", fg="white", cursor="hand2").place(x=860, y=305, width=110, height=28)

        #*******Supplier DETAILS*************
        emp_frame=Frame(self.root, bd=3, relief=RIDGE)
        emp_frame.place(x=0, y=350, relwidth=1, height=150)

        scrolly=Scrollbar(emp_frame, orient=VERTICAL)
        scrollx=Scrollbar(emp_frame, orient=HORIZONTAL)

        self.supplier_table=ttk.Treeview(emp_frame, columns=("Invoice", "Name", "Contact", "Desc"),yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=X)
        scrollx.config(command=self.supplier_table.xview)
        scrolly.config(command=self.supplier_table.yview)

        self.supplier_table.heading("Invoice", text="Invoice No")
        self.supplier_table.heading("Name", text="Name")
        self.supplier_table.heading("Contact", text="Contact")
        self.supplier_table.heading("Desc", text="Description")
        
       
        self.supplier_table["show"]="headings"
        self.supplier_table.pack(fill=BOTH, expand=1)

        self.supplier_table.column("Invoice",width=90)
        self.supplier_table.column("Name",width=100 )
        self.supplier_table.column("Contact", width=100)
        self.supplier_table.column("Desc", width=100)
        
        

        self.show()

 #**************************************************************************       
    def add(self):
        con=sqlite3.connect(database="ims1.db")
        cur=con.cursor()
        try:
            if self.var_sup_invoice.get()=="":
                messagebox.showerror("Error", "Invoice must be Required",parent=self.root)
            else:
                cur.execute("Select * from supplier where Invoice =?", (self.var_sup_invoice.get(),))
                row=cur.fetchone()
                print(row)
                if row!= None:
                    messagebox.showerror("This Invoice Number is already assignend ", parent=self.root)
                else:
                    cur.execute("Insert into supplier (Invoice, Name, Contact, Desc) values(?,?,?,?)",(
                                
                                            self.var_sup_invoice.get(),
                                            self.var_name.get(),
                                           
                                            self.var_contact.get(),
                                         
                                            self.txt_desc.get('1.0',END),
                                          
                                        
                        ))
                    con.commit()
                    messagebox.showinfo("Success", "Supplier Addedd Successfully", parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}")
    
    def show(self):
        con=sqlite3.connect(database="ims1.db")
        cur=con.cursor()
        try:
            cur.execute("select * from supplier")
            rows=cur.fetchall()
            self.supplier_table.delete(*self.supplier_table.get_children())
            for row in rows:
                self.supplier_table.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)

    ''' def get_data(self,ev):
        f=self.supplier_table.focus_force()
        content=(self.supplier_table.item(f))
        row=content['value']
        print(row)
        
        self.var_sup_invoice.set(row[0])
        self.var_name.set(row[1])
        self.var_email.set(row[2])
        self.var_gender.set(row[3])
        self.var_contact.set(row[4])
        self.var_dob.set(row[5])
        self.var_pass.set(row[6])
        self.var_utype.set(row[7])
        self.txt_address.get('1.0',END)
        self.txt_address.delete('1.0',END)
        self.txt_address.insert(END,row[8])
        self.var_salary.set(row[9])'''
                                        
#****************************************************************

    def update(self):
        con=sqlite3.connect(database="ims1.db")
        cur=con.cursor()
        try:
            if self.var_sup_invoice.get()=="":
                messagebox.showerror("Error", "Invoice No must be Required",parent=self.root)
            else:
                cur.execute("Select * from supplier where Invoice =?", (self.var_sup_invoice.get(),))
                row=cur.fetchone()
                print(row)
                if row== None:
                    messagebox.showerror("Invalid Invoice No", parent=self.root)
                else:
                    cur.execute("Update supplier set  Name =?, Contact =?, Desc =? where Invoice =?",(
                                
                                           
                                            self.var_name.get(),
                                           
                                            self.var_contact.get(),
                                            
                                           
                                            self.txt_desc.get('1.0',END),
                                            
                                            self.var_sup_invoice.get(),
                                        
                        ))
                    con.commit()
                    messagebox.showinfo("Success", "sUPPLIER Updated Successfully", parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}")
#*******************************************************************
    def delete(self):
        con=sqlite3.connect(database="ims1.db")
        cur=con.cursor()
        try:
            if self.var_sup_invoice.get()=="":
                messagebox.showerror("Error", "Invoice No  must be Required",parent=self.root)
            else:
                cur.execute("Select * from supplier where Invoice =?", (self.var_sup_invoice.get(),))
                row=cur.fetchone()
                print(row)
                if row== None:
                    messagebox.showerror("Invalid Invoice No ", parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm","Do you really want to delete?",parent=self.root)
                    if op==True:
                     cur.execute("delete from supplier where Invoice=?",(self.var_sup_invoice.get(),))
                     con.commit()
                     messagebox.showinfo("Delete", "Supplier Deleted Successfully")
                     self.clear()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}")
#*****************************************************************************
    def clear(self):
        self.var_sup_invoice.set("")
        self.var_name.set("")
       
        self.var_contact.set("")
       
       
        self.txt_desc.delete('1.0',END)
        
      
       
        self.var_searchtext.set("")

        self.show()

        #*************************************************************************
    def search(self):
        con=sqlite3.connect(database="ims1.db")
        cur=con.cursor()
        try:
           
            if self.var_searchtext.get()=="":
                messagebox.showerror("Error","Search invoice no required")
            
            else:

                cur.execute("select * from supplier where invoice=?",(self.var_searchtext.get(),))
                row=cur.fetchone()
                if row!=None:

                    self.supplier_table.delete(*self.supplier_table.get_children())
                  
                    self.supplier_table.insert('',END,values=row)
                else:
                    messagebox.showerror("Error","No record found", parents=self.root)

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)
     

if __name__=="__main__":
    root=Tk()
    obj=supplierClass(root)
    root.mainloop()