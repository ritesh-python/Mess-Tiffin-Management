
import sqlite3

def connect():
    con=sqlite3.connect("mess.db")
    cur=con.cursor()
    cur.execute("create table user_data(Id integer primary key,name text,address text,mobile_no integer,email_id text,start_date date,password text)")
    con.commit()
    con.close()
connect()