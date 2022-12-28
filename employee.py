#from cgitb import text
#from msilib.schema import Font
from ast import Delete
from cgitb import text
from email import message
from email.headerregistry import Address
from importlib.resources import contents
from multiprocessing import parent_process
from operator import ge
from tkinter import*
from tkinter import ttk, messagebox
from tkinter import font
from tokenize import Name
from turtle import bgcolor, title, width
import sqlite3
#from typing_extensions import Required

from webbrowser import get
#from PIL import Image, ImageTk 
class employeeClass:
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

        self.var_emp_id=StringVar()
        self.var_gender=StringVar()
        self.var_contact=StringVar()
        self.var_name=StringVar()
        self.var_dob=StringVar()
        self.var_doj=StringVar()
        self.var_email=StringVar()
        self.var_pass=StringVar()
        self.var_utype=StringVar()
        self.var_salary=StringVar()
        self.var_address=StringVar()
#*******Search frame***********************
        SearchFreame=LabelFrame(self.root, text="Search Employee", font=("goudy old style",12,"bold"), bg="#E0EEEE", relief=RIDGE)
        SearchFreame.place(x=250, y=20, width=600, height=70)

        #****options *******
        cmb_search=ttk.Combobox(SearchFreame,textvariable=self.var_searchby,values=("Select","Email","Name","Contact"),state='readonly',justify=CENTER, font=("goudy old style",15))
        cmb_search.place(x=10,y=10,width=180)
        cmb_search.current(0)

        txt_search=Entry(SearchFreame, textvariable=self.var_searchtext,font=("goudy old style",15),bg="lightyellow").place(x=200, y=10)
        btn_search=Button(SearchFreame, text="Search", command=self.search, font=("goudy old style",15),bg="green", fg="white", cursor="hand2").place(x=410, y=9, width=150, height=30)

        #********Title**************
        title=Label(self.root, text="Employee Details",bg="#0f4d7d", font=("goudy old style",15), fg="white",).place(x=50, y=100, width=1000)

        #******** Content**************
        #********Row one****************
        lbl_empid=Label(self.root, text="Emp ID: ",bg="White", font=("goudy old style",15)).place(x=50, y=150)
        lbl_gender=Label(self.root, text="Gender: ",bg="White", font=("goudy old style",15)).place(x=400, y=150)
        lbl_contact=Label(self.root, text="Contact: ",bg="White", font=("goudy old style",15)).place(x=750, y=150)

        lbl_empid=Entry(self.root, textvariable=self.var_emp_id,bg="Light yellow", font=("goudy old style",15)).place(x=150, y=150, width=180)
        #lbl_gender=Entry(self.root, textvariable=self.var_gender,bg="White", font=("goudy old style",15)).place(x=500, y=150, width=180)
        cmb_gender=ttk.Combobox(self.root,textvariable=self.var_gender,values=("Select","Male","Female","other"),state='readonly',justify=CENTER, font=("goudy old style",15))
        cmb_gender.place(x=500, y=150, width=180)
        cmb_gender.current(0)
        lbl_contact=Entry(self.root, textvariable=self.var_contact,bg="Light yellow", font=("goudy old style",15)).place(x=850, y=150, width=180)
        #***********Row-2*************
        lbl_name=Label(self.root, text="Name: ",bg="White", font=("goudy old style",15)).place(x=50, y=190)
        lbl_dob=Label(self.root, text="D.O.B.: ",bg="White", font=("goudy old style",15)).place(x=400, y=190)
        lbl_doj=Label(self.root, text="D.O.J.: ",bg="White", font=("goudy old style",15)).place(x=750, y=190)

        lbl_name=Entry(self.root, textvariable=self.var_name,bg="Light yellow", font=("goudy old style",15)).place(x=150, y=190, width=180)
        lbl_dob=Entry(self.root, textvariable=self.var_dob,bg="White", font=("goudy old style",15)).place(x=500, y=190, width=180)        
        lbl_doj=Entry(self.root, textvariable=self.var_doj,bg="Light yellow", font=("goudy old style",15)).place(x=850, y=190, width=180)
        
        #***********Row 3*************
        lbl_email=Label(self.root, text="Email: ",bg="White", font=("goudy old style",15)).place(x=50, y=230)
        lbl_pass=Label(self.root, text="Password: ",bg="White", font=("goudy old style",15)).place(x=400, y=230)
        lbl_utype=Label(self.root, text="User type:" ,bg="White", font=("goudy old style",15)).place(x=750, y=230)

        lbl_email=Entry(self.root, textvariable=self.var_email,bg="Light yellow", font=("goudy old style",15)).place(x=150, y=230, width=180)
        lbl_pass=Entry(self.root, textvariable=self.var_pass,bg="Light yellow", font=("goudy old style",15)).place(x=500, y=230, width=180)        
        #lbl_utype=Entry(self.root, textvariable=self.var_utype,bg="Light yellow", font=("goudy old style",15)).place(x=850, y=230, width=180)
        cmb_utype=ttk.Combobox(self.root,textvariable=self.var_utype,values=("Select","Admin","Employee"),state='readonly',justify=CENTER, font=("goudy old style",15))
        cmb_utype.place(x=850, y=230, width=180)
        cmb_utype.current(0)

        #***********Row 4*************
        lbl_address=Label(self.root, text="Address: ",bg="White", font=("goudy old style",15)).place(x=50, y=270)
        lbl_salary=Label(self.root, text="Salary: ",bg="White", font=("goudy old style",15)).place(x=500, y=270)
        

        self.txt_address=Text(self.root, bg="Light yellow", font=("goudy old style",15))
        self.txt_address.place(x=150, y=270, width=300, height=60)
        lbl_salary=Entry(self.root, textvariable=self.var_salary,bg="Light Yellow", font=("goudy old style",15)).place(x=600, y=270, width=180)        

        #*******Button*****************
        btn_add=Button(self.root, text="Save",command=self.add, font=("goudy old style",15),bg="#2196f3", fg="white", cursor="hand2").place(x=500, y=305, width=110, height=28)
        btn_update=Button(self.root, text="Update",command=self.update, font=("goudy old style",15),bg="#4caf50", fg="white", cursor="hand2").place(x=620, y=305, width=110, height=28)
        btn_delete=Button(self.root, text="Delete",command=self.delete, font=("goudy old style",15),bg="#f44336", fg="white", cursor="hand2").place(x=740, y=305, width=110, height=28)
        btn_clear=Button(self.root, text="Clear",command=self.clear, font=("goudy old style",15),bg="#607d8b", fg="white", cursor="hand2").place(x=860, y=305, width=110, height=28)

        #*******EMP DETAILS*************
        emp_frame=Frame(self.root, bd=3, relief=RIDGE)
        emp_frame.place(x=0, y=350, relwidth=1, height=150)

        scrolly=Scrollbar(emp_frame, orient=VERTICAL)
        scrollx=Scrollbar(emp_frame, orient=HORIZONTAL)

        self.Emp_table=ttk.Treeview(emp_frame, columns=("empid", "Name", "Email", "Gender", "Contact", "DOB", "PASS", "Utype", "Address","Salary"),yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=X)
        scrollx.config(command=self.Emp_table.xview)
        scrolly.config(command=self.Emp_table.yview)

        self.Emp_table.heading("empid", text="Employee ID")
        self.Emp_table.heading("Name", text="Name")
        self.Emp_table.heading("Email", text="Email")
        self.Emp_table.heading("Gender", text="Gender")
        self.Emp_table.heading("Contact", text="Contact")
        self.Emp_table.heading("DOB", text="D.O.B.")
        self.Emp_table.heading("PASS", text="Password")
        self.Emp_table.heading("Utype", text="User Type")
        self.Emp_table.heading("Address", text="Address")
        self.Emp_table.heading("Salary", text="Salary")
        self.Emp_table["show"]="headings"
        self.Emp_table.pack(fill=BOTH, expand=1)

        self.Emp_table.column("empid",width=90)
        self.Emp_table.column("Name",width=100 )
        self.Emp_table.column("Email", width=100)
        self.Emp_table.column("Gender", width=100)
        self.Emp_table.column("Contact", width=100)
        self.Emp_table.column("DOB",width=100)
        self.Emp_table.column("PASS",width=100)
        self.Emp_table.column("Utype", width=100)
        self.Emp_table.column("Address",width=100)
        self.Emp_table.column("Salary", width=100)
        self.Emp_table.pack(fill=BOTH, expand=1)

       # self.Emp_table.bind("<ButtonRelease-1>",self.get_data)

        self.show()
 #**************************************************************************       
    def add(self):
        con=sqlite3.connect(database="ims1.db")
        cur=con.cursor()
        try:
            if self.var_emp_id.get()=="":
                messagebox.showerror("Error", "Employee ID must be Required",parent=self.root)
            else:
                cur.execute("Select * from employee where empid =?", (self.var_emp_id.get(),))
                row=cur.fetchone()
                print(row)
                if row!= None:
                    messagebox.showerror("This Employee ID is already assignend ", parent=self.root)
                else:
                    cur.execute("Insert into employee (empid, Name, Email, Gender, Contact, DOB, PASS, Utype, Address,Salary) values(?,?,?,?,?,?,?,?,?,?)",(
                                
                                            self.var_emp_id.get(),
                                            self.var_name.get(),
                                            self.var_email.get(),
                                            self.var_gender.get(),
                                            self.var_contact.get(),
                                            
                                            self.var_dob.get(),
                                                                        
                                            self.var_pass.get(),
                                            self.var_utype.get(),
                                          #  self.var_address.get(),
                                            self.txt_address.get('1.0',END),
                                            self.var_salary.get(),
                                        
                        ))
                    con.commit()
                    messagebox.showinfo("Success", "Employee Addedd Successfully", parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}")
    
    def show(self):
        con=sqlite3.connect(database="ims1.db")
        cur=con.cursor()
        try:
            cur.execute("select * from employee")
            rows=cur.fetchall()
            self.Emp_table.delete(*self.Emp_table.get_children())
            for row in rows:
                self.Emp_table.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)

    ''' def get_data(self,ev):
        f=self.Emp_table.focus_force()
        content=(self.Emp_table.item(f))
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
            if self.var_emp_id.get()=="":
                messagebox.showerror("Error", "Employee ID must be Required",parent=self.root)
            else:
                cur.execute("Select * from employee where empid =?", (self.var_emp_id.get(),))
                row=cur.fetchone()
                print(row)
                if row== None:
                    messagebox.showerror("Invalid Employee id ", parent=self.root)
                else:
                    cur.execute("Update employee set  Name =?, Email =?, Gender =?, Contact =?, DOB =?, PASS =?, Utype =?, Address =?,Salary =? where empid =?",(
                                
                                           
                                            self.var_name.get(),
                                            self.var_email.get(),
                                            self.var_gender.get(),
                                            self.var_contact.get(),
                                            
                                            self.var_dob.get(),
                                                                        
                                            self.var_pass.get(),
                                            self.var_utype.get(),
                                          #  self.var_address.get(),
                                            self.txt_address.get('1.0',END),
                                            self.var_salary.get(),
                                             self.var_emp_id.get(),
                                        
                        ))
                    con.commit()
                    messagebox.showinfo("Success", "Employee Updated Successfully", parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}")
#*******************************************************************
    def delete(self):
        con=sqlite3.connect(database="ims1.db")
        cur=con.cursor()
        try:
            if self.var_emp_id.get()=="":
                messagebox.showerror("Error", "Employee ID must be Required",parent=self.root)
            else:
                cur.execute("Select * from employee where empid =?", (self.var_emp_id.get(),))
                row=cur.fetchone()
                print(row)
                if row== None:
                    messagebox.showerror("Invalid Employee id ", parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm","Do you really want to delete?",parent=self.root)
                    if op==True:
                     cur.execute("delete from employee where empid=?",(self.var_emp_id.get(),))
                     con.commit()
                     messagebox.showinfo("Delete", "Employee Deleted Successfully")
                     self.clear()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}")
#*****************************************************************************
    def clear(self):
        self.var_emp_id.set("")
        self.var_name.set("")
        self.var_email.set("")
        self.var_gender.set("Select")
        self.var_contact.set("")
        self.var_dob.set("")
        self.var_pass.set("")
        self.var_utype.set("Select")
        self.txt_address.get('1.0',END)
        self.txt_address.delete('1.0',END)
        
        self.var_salary.set("")
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

                cur.execute("select * from employee where "+self.var_searchby.get()+" LIKE '%"+self.var_searchtext.get()+"%' ")
                rows=cur.fetchall()
                if len(rows)!=0:

                    self.Emp_table.delete(*self.Emp_table.get_children())
                    for row in rows:
                        self.Emp_table.insert('',END,values=row)
                else:
                    messagebox.showerror("Error","No record found", parents=self.root)

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)
     

if __name__=="__main__":
    root=Tk()
    obj=employeeClass(root)
    root.mainloop()