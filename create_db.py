import sqlite3
def create_db():
    con=sqlite3.connect(database="ims1.db")
    cur=con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS employee(empid INTEGER PRIMARY KEY AUTOINCREMENT, Name text, Email text, Gender text, Contact text, DOB text, PASS text, Utype text, Address text,Salary text)")
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS supplier(Invoice INTEGER PRIMARY KEY AUTOINCREMENT, Name text, Contact text, Desc text)")
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS category(CID INTEGER PRIMARY KEY AUTOINCREMENT, Name text)")
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS product(pid INTEGER PRIMARY KEY AUTOINCREMENT, cat text, Supplier text, name text, price text, qty text, status text)")
    con.commit()

create_db()