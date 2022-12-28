from cgitb import text
from email import message
from email.headerregistry import Address
#from nis import cat
from operator import ge
from re import search
from tkinter import*
from tkinter import ttk, messagebox
from tkinter import font
from tokenize import Name
from turtle import bgcolor, right, st, title, width
import sqlite3
#from typing_extensions import Required
from webbrowser import get
#from PIL import Image, ImageTk 
class productClass:
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
        self.cat_list=[]
        self.sup_list=[]
        self.featch_cat_sup()
        self.var_pid=StringVar()
        self.var_cat=StringVar()
        self.var_sup=StringVar()
        self.var_name=StringVar()
        self.var_price=StringVar()
        self.var_qty=StringVar()
        self.var_status=StringVar()


        product_Frame=Frame(product_Frame, bd=2, relief=RIDGE, bg="White")
        product_Frame.place(x=10, y=10, width=450, height=480)
####################title*********************************
        title=Label(product_Frame, text="Manage Product Details",bg="#0f4d7d", font=("goudy old style",18), fg="white",).pack(side=TOP, fill=X)
        
        ###Lable*******************
        lbl_category=Label(product_Frame, text="Category",bg="White", font=("goudy old style",18),).place(x=30, y=60)
        lbl_supplier=Label(product_Frame, text="Supplier",bg="White", font=("goudy old style",18),).place(x=30, y=110)
        lbl_pro_name=Label(product_Frame, text="Name",bg="White", font=("goudy old style",18),).place(x=30, y=160)
        lbl_price=Label(product_Frame, text="Price",bg="White", font=("goudy old style",18),).place(x=30, y=210)
        lbl_quantity=Label(product_Frame, text="Quantity",bg="White", font=("goudy old style",18),).place(x=30, y=260)
        lbl_status=Label(product_Frame, text="Status",bg="White", font=("goudy old style",18),).place(x=30, y=310)

       
        cmb_cat=ttk.Combobox(product_Frame,textvariable=self.var_cat,values=self.cat_list,state='readonly',justify=CENTER, font=("goudy old style",15))
        cmb_cat.place(x=150,y=64,width=200)
        cmb_cat.current(0)

        cmb_sup=ttk.Combobox(product_Frame,textvariable=self.var_sup,values=self.sup_list,state='readonly',justify=CENTER, font=("goudy old style",15))
        cmb_sup.place(x=150,y=114,width=200)
        cmb_sup.current(0)

        txt_name=Entry(product_Frame, textvariable=self.var_name,font=("goudy old style",15),bg="lightyellow").place(x=150, y=164, width=200)
        txt_price=Entry(product_Frame, textvariable=self.var_price,font=("goudy old style",15),bg="lightyellow").place(x=150, y=214, width=200)
        txt_qty=Entry(product_Frame, textvariable=self.var_qty,font=("goudy old style",15),bg="lightyellow").place(x=150, y=264, width=200)

        cmb_status=ttk.Combobox(product_Frame,textvariable=self.var_status,values=("Select", "Active", "Inactive"),state='readonly',justify=CENTER, font=("goudy old style",15))
        cmb_status.place(x=150,y=314,width=200)
        cmb_status.current(0)

        #*******Button*****************
        btn_add=Button(product_Frame, text="Save",command=self.add, font=("goudy old style",15),bg="#2196f3", fg="white", cursor="hand2").place(x=10, y=400, width=100, height=40)
        btn_update=Button(product_Frame, text="Update", command=self.update,font=("goudy old style",15),bg="#4caf50", fg="white", cursor="hand2").place(x=120, y=400, width=100, height=40)
        btn_delete=Button(product_Frame, text="Delete", font=("goudy old style",15),bg="#f44336", fg="white", cursor="hand2").place(x=230, y=400, width=100, height=40)
        btn_clear=Button(product_Frame, text="Clear", font=("goudy old style",15),bg="#607d8b", fg="white", cursor="hand2").place(x=340, y=400, width=100, height=40)

#*******Search frame***********************
        SearchFreame=LabelFrame(self.root, text="Search Product ", font=("goudy old style",12,"bold"), bg="#E0EEEE", relief=RIDGE)
        SearchFreame.place(x=480, y=10, width=600, height=80)

        #****options *******
        cmb_search=ttk.Combobox(SearchFreame,textvariable=self.var_searchby,values=("Select","Category", "Supplier", "Name"),state='readonly',justify=CENTER, font=("goudy old style",15))
        cmb_search.place(x=10,y=10,width=180)
        cmb_search.current(0)

        txt_search=Entry(SearchFreame, textvariable=self.var_searchtext,font=("goudy old style",15),bg="lightyellow").place(x=200, y=10)
        btn_search=Button(SearchFreame, text="Search", font=("goudy old style",15),bg="green", fg="white", cursor="hand2").place(x=410, y=9, width=150, height=30)

#*******PRODUCT DETAILS*************

        p_Frame=Frame(self.root, bd=3, relief=RIDGE)
        p_Frame.place(x=480, y=100, width=600, height=390)

        scrolly=Scrollbar(p_Frame, orient=VERTICAL)
        scrollx=Scrollbar(p_Frame, orient=HORIZONTAL)

        self.product_Table=ttk.Treeview(p_Frame, columns=("pid", "cat", "Supplier", "name", "price", "qty", "status"),yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=X)
        scrollx.config(command=self.product_Table.xview)
        scrolly.config(command=self.product_Table.yview)

        self.product_Table.heading("pid", text="Product ID")
        self.product_Table.heading("cat", text="category")
        self.product_Table.heading("Supplier", text="Supplier")
        self.product_Table.heading("name", text="Name")
        self.product_Table.heading("price", text="Price")
        self.product_Table.heading("qty", text="Quantity")
        self.product_Table.heading("status", text="Status")
       
        self.product_Table["show"]="headings"
        self.product_Table.pack(fill=BOTH, expand=1)

        self.product_Table.column("pid",width=90)
        self.product_Table.column("cat",width=100 )
        self.product_Table.column("Supplier", width=100)
        self.product_Table.column("name", width=100)
        self.product_Table.column("price", width=100)
        self.product_Table.column("qty",width=100)
        self.product_Table.column("status",width=100)

        self.show()
        
#**************************************************************************      
    def featch_cat_sup(self):
        con=sqlite3.connect(database="ims1.db")
        cur=con.cursor()
        try:
            cur.execute("Select name from category")
            cat=cur.fetchall()
            self.cat_list.append("Empty")
            if len(cat)>0:
                del self.cat_list[:]
                self.cat_list.append("Select")
                for i in cat:
                    self.cat_list.append(i[0])
            

            cur.execute("Select name from supplier")
            sup=cur.fetchall()
            self.sup_list.append("Empty")
            if len(sup)>0:
                del self.sup_list[:]
                self.sup_list.append("Select")
                for i in sup:
                    self.sup_list.append(i[0])
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}")
#*************************************************************************************************
    def add(self):
        con=sqlite3.connect(database="ims1.db")
        cur=con.cursor()
        try:
            if self.var_cat.get()=="Selcet" or self.var_cat.get()=="Empty" or self.var_sup.get()=="Select" or self.var_name.get()=="":
                messagebox.showerror("Error", "All fields must be Required",parent=self.root)
            else:
                cur.execute("Select * from product where name=? ", (self.var_name.get(),))
                row=cur.fetchone()
                
                if row!= None:
                    messagebox.showerror("This Product is already assignend ", parent=self.root)
                else:
                    cur.execute("Insert into product (cat, Supplier, name, price, qty, status) values(?,?,?,?,?,?)",(
                                
                                                    self.var_cat.get(),
                                                    
                                                    self.var_sup.get(),
                                                                                
                                                    self.var_name.get(),
                                                    self.var_price.get(),
                                                    self.var_qty.get(),
                                                    
                                                    self.var_status.get(),
                                        
                        ))
                    con.commit()
                    messagebox.showinfo("Success", "Product Addedd Successfully", parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}")
 #******************************************************************   
    def show(self):
        con=sqlite3.connect(database="ims1.db")
        cur=con.cursor()
        try:
            cur.execute("select * from product")
            rows=cur.fetchall()
            self.product_Table.delete(*self.product_Table.get_children())
            for row in rows:
                self.product_Table.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)

    '''def get_data(self,ev):
        f=self.product_Table.focus_force()
        content=(self.product_Table.item(f))
        row=content['value']
        print(row)
        
        self.var_emp_id.set(row[0])
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
            if self.var_name.get()=="":
                messagebox.showerror("Error", "Product  ID must be Required",parent=self.root)
            else:
                cur.execute("Select * from product where pid =?", (self.var_pid.get(),))
                row=cur.fetchone()
                print(row)
                if row== None:
                    messagebox.showerror("Invalid product id ", parent=self.root)
                else:
                    cur.execute("Update product set  cat =?, Supplier  =?, name =?, price =?, qty =?, status =? where pid =?",(
                                
                                           
                                         #  self.var_name.get(),
                                            
                                            self.var_sup.get(),
                                                                        
                                            self.var_name.get(),
                                            self.var_price.get(),
                                            self.var_qty.get(),
                                            
                                            self.var_status.get(),
                                            self.var_pid.get(),
                                        
                        ))
                    con.commit()
                    messagebox.showinfo("Success", "Product Updated Successfully", parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}")
#*******************************************************************
    def delete(self):
        con=sqlite3.connect(database="ims1.db")
        cur=con.cursor()
        try:
            if self.var_pid.get()=="":
                messagebox.showerror("Error", "Product must be Required",parent=self.root)
            else:
                cur.execute("Select * from product where pid =?", (self.var_pid.get(),))
                row=cur.fetchone()
                print(row)
                if row== None:
                    messagebox.showerror("Invalid product id ", parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm","Do you really want to delete?",parent=self.root)
                    if op==True:
                     cur.execute("delete from product where pid=?",(self.var_pid.get(),))
                     con.commit()
                     messagebox.showinfo("Delete", "Product Deleted Successfully")
                     self.clear()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}")
#*****************************************************************************
    def clear(self):
        self.var_name.set(""),
                                            
        self.var_sup.set(""),
        self.var_name.set(""),
        self.var_price.set(""),
        self.var_qty.set(""),
        self.var_status.set(""),
        self.var_pid.set(""),
        self.var_searchby.set("Select")
        self.var_searchtext.set("")

        self.show()

        #*************************************************************************
    def search(self):
        con=sqlite3.connect(database="ims1.db")
        cur=con.cursor()
        try:
            if self.var_searchby.get()=="Select":
                messagebox.showerror("Error","Select Search By Option")

            elif self.var_searchtext.get()=="":
                messagebox.showerror("Error","Search input required")
            
            else:

                cur.execute("select * from product where "+self.var_searchby.get()+" LIKE '%"+self.var_searchtext.get()+"%' ")
                rows=cur.fetchall()
                if len(rows)!=0:

                    self.product_Table.delete(*self.product_Table.get_children())
                    for row in rows:
                        self.product_Table.insert('',END,values=row)
                else:
                    messagebox.showerror("Error","No record found", parents=self.root)

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)
     

if __name__=="__main__":
    root=Tk()
    obj=productClass(root)
    root.mainloop()