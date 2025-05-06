import sqlite3
def create_db():
    con=sqlite3.connect(database=r'gsps.db')
    cur=con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS employee(eid INTEGER PRIMARY KEY AUTOINCREMENT,name text,email text,gender text,contact text,dob text,doj text,pass text,utype text,city text,salary text)")
    cur.execute("CREATE TABLE IF NOT EXISTS customer(cid INTEGER PRIMARY KEY AUTOINCREMENT,name text,email text,gender text,contact text,area text,city text)")
    cur.execute("CREATE TABLE IF NOT EXISTS category(cid INTEGER PRIMARY KEY AUTOINCREMENT,name text)")
    cur.execute("CREATE TABLE IF NOT EXISTS product(pid INTEGER PRIMARY KEY AUTOINCREMENT,cat text,name text,price text,qty text,status text)")
    cur.execute("CREATE TABLE IF NOT EXISTS vehicl(vehicl_no INTEGER PRIMARY KEY AUTOINCREMENT,vehicl_name text,driver_name text)")


    con.commit()
create_db()    