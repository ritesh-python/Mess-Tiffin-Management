from tkinter import *
import tkinter as tk
import os
from tkinter import messagebox
prog_call = sys.argv[0]
prog_location = os.path.split(prog_call)[0]
class add:
    def custdataadd(self):
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9'  # X11 color: 'gray85'
        _ana1color = '#d9d9d9'  # X11 color: 'gray85'
        _ana2color = '#ececec'  # Closest X11 color: 'gray92'

        self.top = Toplevel()
        self.top.geometry("556x695+571+230")
        self.top.title("New Toplevel")
        self.top.configure(background="#34c8d8")
        self.top.configure(highlightbackground="#d9d9d9")
        self.top.configure(highlightcolor="black")

        self.adf1 = tk.Frame(self.top)
        self.adf1.place(relx=0.0, rely=0.0, relheight=0.137, relwidth=0.998)
        self.adf1.configure(relief='groove')
        self.adf1.configure(borderwidth="2")
        self.adf1.configure(relief="groove")
        self.adf1.configure(background="#2733d8")
        self.adf1.configure(highlightbackground="#d9d9d9")
        self.adf1.configure(highlightcolor="black")
        self.adf1.configure(width=555)

        self.albl1 = tk.Label(self.adf1)
        self.albl1.place(relx=0.36, rely=0.316, height=39, width=146)
        self.albl1.configure(activebackground="#f9f9f9")
        self.albl1.configure(activeforeground="black")
        self.albl1.configure(background="#2733d8")
        self.albl1.configure(disabledforeground="#a3a3a3")
        self.albl1.configure(font="-family {Times New Roman} -size 14")
        self.albl1.configure(foreground="#ffffff")
        self.albl1.configure(highlightbackground="#d9d9d9")
        self.albl1.configure(highlightcolor="black")
        self.albl1.configure(text='''ADD DATA''')

        self.albl2 = tk.Label(self.top)
        self.albl2.place(relx=0.072, rely=0.331, height=39, width=146)
        self.albl2.configure(activebackground="#f9f9f9")
        self.albl2.configure(activeforeground="black")
        self.albl2.configure(background="#675fd8")
        self.albl2.configure(disabledforeground="#a3a3a3")
        self.albl2.configure(font="-family {Times New Roman} -size 12")
        self.albl2.configure(foreground="#ffffff")
        self.albl2.configure(highlightbackground="#d9d9d9")
        self.albl2.configure(highlightcolor="black")
        self.albl2.configure(text='''NAME''')

        self.albl3 = tk.Label(self.top)
        self.albl3.place(relx=0.072, rely=0.403, height=39, width=146)
        self.albl3.configure(activebackground="#f9f9f9")
        self.albl3.configure(activeforeground="black")
        self.albl3.configure(background="#675fd8")
        self.albl3.configure(disabledforeground="#a3a3a3")
        self.albl3.configure(font="-family {Times New Roman} -size 12")
        self.albl3.configure(foreground="#ffffff")
        self.albl3.configure(highlightbackground="#d9d9d9")
        self.albl3.configure(highlightcolor="black")
        self.albl3.configure(text='''MOB NO.''')

        self.albl4 = tk.Label(self.top)
        self.albl4.place(relx=0.072, rely=0.475, height=39, width=146)
        self.albl4.configure(activebackground="#f9f9f9")
        self.albl4.configure(activeforeground="black")
        self.albl4.configure(background="#675fd8")
        self.albl4.configure(disabledforeground="#a3a3a3")
        self.albl4.configure(font="-family {Times New Roman} -size 12")
        self.albl4.configure(foreground="#ffffff")
        self.albl4.configure(highlightbackground="#d9d9d9")
        self.albl4.configure(highlightcolor="black")
        self.albl4.configure(text='''EMAIL .''')

        self.albl5 = tk.Label(self.top)
        self.albl5.place(relx=0.072, rely=0.547, height=39, width=146)
        self.albl5.configure(activebackground="#f9f9f9")
        self.albl5.configure(activeforeground="black")
        self.albl5.configure(background="#675fd8")
        self.albl5.configure(disabledforeground="#a3a3a3")
        self.albl5.configure(font="-family {Times New Roman} -size 12")
        self.albl5.configure(foreground="#ffffff")
        self.albl5.configure(highlightbackground="#d9d9d9")
        self.albl5.configure(highlightcolor="black")
        self.albl5.configure(text='''PASSWORD''')

        self.albl6 = tk.Label(self.top)
        self.albl6.place(relx=0.072, rely=0.691, height=39, width=146)
        self.albl6.configure(activebackground="#f9f9f9")
        self.albl6.configure(activeforeground="black")
        self.albl6.configure(background="#675fd8")
        self.albl6.configure(disabledforeground="#a3a3a3")
        self.albl6.configure(font="-family {Times New Roman} -size 12")
        self.albl6.configure(foreground="#ffffff")
        self.albl6.configure(highlightbackground="#d9d9d9")
        self.albl6.configure(highlightcolor="black")
        self.albl6.configure(text='''ADDRESS''')

        self.txtname = tk.Entry(self.top)
        self.txtname.place(relx=0.396, rely=0.331, height=36, relwidth=0.565)
        self.txtname.configure(background="white")
        self.txtname.configure(disabledforeground="#a3a3a3")
        self.txtname.configure(font="-family {Arial} -size 12")
        self.txtname.configure(foreground="#000000")
        self.txtname.configure(highlightbackground="#d9d9d9")
        self.txtname.configure(highlightcolor="black")
        self.txtname.configure(insertbackground="black")
        self.txtname.configure(selectbackground="#c4c4c4")
        self.txtname.configure(selectforeground="black")

        self.txtmob = tk.Entry(self.top)
        self.txtmob.place(relx=0.396, rely=0.403, height=36, relwidth=0.565)
        self.txtmob.configure(background="white")
        self.txtmob.configure(disabledforeground="#a3a3a3")
        self.txtmob.configure(font="-family {Arial} -size 12")
        self.txtmob.configure(foreground="#000000")
        self.txtmob.configure(highlightbackground="#d9d9d9")
        self.txtmob.configure(highlightcolor="black")
        self.txtmob.configure(insertbackground="black")
        self.txtmob.configure(selectbackground="#c4c4c4")
        self.txtmob.configure(selectforeground="black")

        self.txtemial = tk.Entry(self.top)
        self.txtemial.place(relx=0.396, rely=0.475, height=36, relwidth=0.565)
        self.txtemial.configure(background="white")
        self.txtemial.configure(disabledforeground="#a3a3a3")
        self.txtemial.configure(font="-family {Arial} -size 12")
        self.txtemial.configure(foreground="#000000")
        self.txtemial.configure(highlightbackground="#d9d9d9")
        self.txtemial.configure(highlightcolor="black")
        self.txtemial.configure(insertbackground="black")
        self.txtemial.configure(selectbackground="#c4c4c4")
        self.txtemial.configure(selectforeground="black")

        self.txtpass = tk.Entry(self.top)
        self.txtpass.place(relx=0.396, rely=0.547, height=36, relwidth=0.565)
        self.txtpass.configure(background="white")
        self.txtpass.configure(disabledforeground="#a3a3a3")
        self.txtpass.configure(font="-family {Arial} -size 12")
        self.txtpass.configure(foreground="#000000")
        self.txtpass.configure(highlightbackground="#d9d9d9")
        self.txtpass.configure(highlightcolor="black")
        self.txtpass.configure(insertbackground="black")
        self.txtpass.configure(selectbackground="#c4c4c4")
        self.txtpass.configure(selectforeground="black")

        self.menubar = tk.Menu(self.top, font="TkMenuFont", bg=_bgcolor, fg=_fgcolor)
        self.top.configure(menu=self.menubar)

        self.txtaddr = tk.Entry(self.top)
        self.txtaddr.place(relx=0.396, rely=0.691, height=116, relwidth=0.565)
        self.txtaddr.configure(background="white")
        self.txtaddr.configure(disabledforeground="#a3a3a3")
        self.txtaddr.configure(font="-family {Arial} -size 12")
        self.txtaddr.configure(foreground="#000000")
        self.txtaddr.configure(highlightbackground="#d9d9d9")
        self.txtaddr.configure(highlightcolor="black")
        self.txtaddr.configure(insertbackground="black")
        self.txtaddr.configure(selectbackground="#c4c4c4")
        self.txtaddr.configure(selectforeground="black")

        self.registerbutt = tk.Button(self.top)
        self.registerbutt.place(relx=0.288, rely=0.892, height=42, width=228)
        self.registerbutt.configure(activebackground="#ececec")
        self.registerbutt.configure(activeforeground="#000000")
        self.registerbutt.configure(background="#675fd8")
        self.registerbutt.configure(disabledforeground="#a3a3a3")
        self.registerbutt.configure(font="-family {Segoe UI} -size 12")
        self.registerbutt.configure(foreground="#ffffff")
        self.registerbutt.configure(highlightbackground="#d9d9d9")
        self.registerbutt.configure(highlightcolor="black")
        self.registerbutt.configure(pady="0")
        self.registerbutt.configure(text='''REGISTER''')
        self.registerbutt.configure(command=self.regi)

        self.albl5_3 = tk.Label(self.top)
        self.albl5_3.place(relx=0.072, rely=0.619, height=39, width=146)
        self.albl5_3.configure(activebackground="#f9f9f9")
        self.albl5_3.configure(activeforeground="black")
        self.albl5_3.configure(background="#675fd8")
        self.albl5_3.configure(disabledforeground="#a3a3a3")
        self.albl5_3.configure(font="-family {Times New Roman} -size 12")
        self.albl5_3.configure(foreground="#ffffff")
        self.albl5_3.configure(highlightbackground="#d9d9d9")
        self.albl5_3.configure(highlightcolor="black")
        self.albl5_3.configure(text='''START DATE''')

        self.txtstart = tk.Entry(self.top)
        self.txtstart.place(relx=0.396, rely=0.619, height=36, relwidth=0.565)
        self.txtstart.configure(background="white")
        self.txtstart.configure(disabledforeground="#a3a3a3")
        self.txtstart.configure(font="-family {Arial} -size 12")
        self.txtstart.configure(foreground="#000000")
        self.txtstart.configure(highlightbackground="#d9d9d9")
        self.txtstart.configure(highlightcolor="black")
        self.txtstart.configure(insertbackground="black")
        self.txtstart.configure(selectbackground="#c4c4c4")
        self.txtstart.configure(selectforeground="black")

        self.lblid = tk.Label(self.top)
        self.lblid.place(relx=0.072, rely=0.259, height=39, width=146)
        self.lblid.configure(activebackground="#f9f9f9")
        self.lblid.configure(activeforeground="black")
        self.lblid.configure(background="#675fd8")
        self.lblid.configure(disabledforeground="#a3a3a3")
        self.lblid.configure(font="-family {Times New Roman} -size 12")
        self.lblid.configure(foreground="#ffffff")
        self.lblid.configure(highlightbackground="#d9d9d9")
        self.lblid.configure(highlightcolor="black")
        self.lblid.configure(text='''ID''')

        self.txtid = tk.Entry(self.top)
        self.txtid.place(relx=0.396, rely=0.259, height=36, relwidth=0.565)
        self.txtid.configure(background="white")
        self.txtid.configure(disabledforeground="#a3a3a3")
        self.txtid.configure(font="-family {Arial} -size 12")
        self.txtid.configure(foreground="#000000")
        self.txtid.configure(highlightbackground="#d9d9d9")
        self.txtid.configure(highlightcolor="black")
        self.txtid.configure(insertbackground="black")
        self.txtid.configure(selectbackground="#c4c4c4")
        self.txtid.configure(selectforeground="black")
        self.top.mainloop()
    def getid(self):
        return  self.txtid.get()
    def getname(self):
        name=self.txtname.get()
        return name
    def getaddr(self):
        addr=self.txtaddr.get()
        return addr
    def getmob(self):
        mob=self.txtmob.get()
        return mob
    def getemail(self):
        email=self.txtemial.get()
        return email
    def getsdate(self):
        sdate=self.txtstart.get()
        return sdate
    def getpass(self):
        passw=self.txtpass.get()
        return passw



    def regi(self):
        id=self.getid()
        name=self.getname()
        addr = self.getaddr()
        mob = self.getmob()
        email = self.getemail()
        sdate = self.getsdate()
        passw = self.getpass()
        print("insert into user_data values ("+id+",'"+name+"','"+addr+"',"+mob+",'"+email+"','"+sdate+"','"+passw+"')")
        import sqlite3
        con = sqlite3.connect("mess.db")
        try:
            cur = con.cursor()
            cur.execute("insert into user_data values ("+id+",'"+name+"','"+addr+"',"+mob+",'"+email+"','"+sdate+"','"+passw+"')")
            con.commit()
            messagebox.showinfo("sucess","hurray..! data added sucessfully")

            con.close()
        except(Exception):
            messagebox.showinfo("unsucess","Enter proper data")
