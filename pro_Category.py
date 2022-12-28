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
class categoryClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1100x500+220+130")
        #self.root.title("Inventory") #Title
        self.root.focus_force()
        self.root.config(bg="#E0EEEE")
#***********Variables****************************************
        self.var_cat_id=StringVar()
        self.var_name=StringVar()

        #*****************Title****************
        lbl_title=Label(self.root, text="Manage product Category", font=("goudy old style", 30),bg="#184a45", fg="white", bd=3, relief=RIDGE).pack(side=TOP, fill=X, padx=10, pady=20)
        lbl_name=Label(self.root, text="Enter Category", font=("goudy old style", 30),bg="White").place(x=50,y=100)
        txt_title=Entry(self.root, textvariable=self.var_name, font=("goudy old style", 18),bg="Light yellow").place(x=50,y=170, width=300)
       
        btn_add=Button(self.root, text="ADD", command=self.add, font=("goudy old style", 18),bg="Green", fg="white", cursor="hand2").place(x=360,y=170, width=150, height=30)
        btn_delete=Button(self.root, text="Delete",command=self.delete, font=("goudy old style", 18),bg="Red", fg="white", cursor="hand2").place(x=520,y=170, width=150, height=30)

  #*******Product DETAILS*************
        cat_frame=Frame(self.root, bd=3, relief=RIDGE)
        cat_frame.place(x=700, y=100, width=380, height=300)

        scrolly=Scrollbar(cat_frame, orient=VERTICAL)
        scrollx=Scrollbar(cat_frame, orient=HORIZONTAL)

        self.category_table=ttk.Treeview(cat_frame, columns=("CID", "Name"),yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=X)
        scrollx.config(command=self.category_table.xview)
        scrolly.config(command=self.category_table.yview)

        self.category_table.heading("CID", text="Category ID")
        self.category_table.heading("Name", text="Name")
        
        
       
        self.category_table["show"]="headings"
        self.category_table.pack(fill=BOTH, expand=1)

        self.category_table.column("CID",width=90)
        self.category_table.column("Name",width=100 )

        self.show()
#*********************************************************************************
    def add(self):
        con=sqlite3.connect(database="ims1.db")
        cur=con.cursor()
        try:
            if self.var_name.get()=="":
                messagebox.showerror("Error", "Category name must be Required",parent=self.root)
            else:
                cur.execute("Select * from category where Name =?", (self.var_name.get(),))
                row=cur.fetchone()
                print(row)
                if row!= None:
                    messagebox.showerror("Category already present ", parent=self.root)
                else:
                    cur.execute("Insert into category (Name) values(?)",(
                                
                                            self.var_name.get(),
              
                        ))
                    con.commit()
                    messagebox.showinfo("Success", "Category Addedd Successfully", parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}")
    
    def show(self):
        con=sqlite3.connect(database="ims1.db")
        cur=con.cursor()
        try:
            cur.execute("select * from category")
            rows=cur.fetchall()
            self.category_table.delete(*self.category_table.get_children())
            for row in rows:
                self.category_table.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)

#*******************************************************************
    def delete(self):
        con=sqlite3.connect(database="ims1.db")
        cur=con.cursor()
        try:
            if self.var_name.get()=="":
                messagebox.showerror("Error", "Category Name  must be Required",parent=self.root)
            else:
                cur.execute("Select * from category where Name =?", (self.var_name.get(),))
                row=cur.fetchone()
                print(row)
                if row== None:
                    messagebox.showerror("Invalid Category Name ", parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm","Do you really want to delete?",parent=self.root)
                    if op==True:
                     cur.execute("delete from category where Name=?",(self.var_name.get(),))
                     con.commit()
                     messagebox.showinfo("Delete", "Category Deleted Successfully")
                     self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}")
        
if __name__=="__main__":
    root=Tk()
    obj=categoryClass(root)
    root.mainloop()