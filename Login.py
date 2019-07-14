from tkinter import *
import tkinter as tk
import os
prog_call = sys.argv[0]
prog_location = os.path.split(prog_call)[0]
class logins:
    def custsection(self):
        self.top = Toplevel()
        self.top.configure(background="#b8bfd8")
        self.top.geometry("653x449+592+276")
        self.top.configure(background="#75d86e")

        self.lf1 = tk.Frame(self.top)
        self.lf1.place(relx=0.0, rely=0.0, relheight=0.256, relwidth=1.003)
        self.lf1.configure(relief='groove')
        self.lf1.configure(borderwidth="2")
        self.lf1.configure(relief="groove")
        self.lf1.configure(background="#24b538")
        self.lf1.configure(width=655)

        self.ll1 = tk.Label(self.lf1)
        self.ll1.place(relx=0.29, rely=0.348, height=44, width=259)
        self.ll1.configure(background="#24b538")
        self.ll1.configure(disabledforeground="#a3a3a3")
        self.ll1.configure(font="-family {Segoe UI Black} -size 14 -weight bold")
        self.ll1.configure(foreground="#000000")
        self.ll1.configure(text='''CUSTOMER LOGIN''')

        self.ll2 = tk.Label(self.top)
        self.ll2.place(relx=0.23, rely=0.379, height=44, width=63)
        self.ll2.configure(background="#75d86e")
        self.ll2.configure(disabledforeground="#a3a3a3")
        self.ll2.configure(font="-family {Segoe UI} -size 14")
        self.ll2.configure(foreground="#000000")
        self.ll2.configure(text='''ID   :''')

        self.textid = tk.Entry(self.top)
        self.textid.place(relx=0.337, rely=0.379, height=46, relwidth=0.466)
        self.textid.configure(background="white")
        self.textid.configure(disabledforeground="#a3a3a3")
        self.textid.configure(font="TkFixedFont")
        self.textid.configure(foreground="#000000")
        self.textid.configure(insertbackground="black")
        self.textid.configure(width=304)

        self.ll3 = tk.Label(self.top)
        self.ll3.place(relx=0.061, rely=0.557, height=44, width=183)
        self.ll3.configure(activebackground="#f9f9f9")
        self.ll3.configure(activeforeground="black")
        self.ll3.configure(background="#75d86e")
        self.ll3.configure(disabledforeground="#a3a3a3")
        self.ll3.configure(font="-family {Segoe UI} -size 14")
        self.ll3.configure(foreground="#000000")
        self.ll3.configure(highlightbackground="#d9d9d9")
        self.ll3.configure(highlightcolor="black")
        self.ll3.configure(text='''PASSWORD :''')
        self.ll3.configure(width=183)

        self.textpass = tk.Entry(self.top)
        self.textpass.place(relx=0.337, rely=0.557, height=46, relwidth=0.466)
        self.textpass.configure(background="white")
        self.textpass.configure(disabledforeground="#a3a3a3")
        self.textpass.configure(font="TkFixedFont")
        self.textpass.configure(foreground="#000000")
        self.textpass.configure(highlightbackground="#d9d9d9")
        self.textpass.configure(highlightcolor="black")
        self.textpass.configure(insertbackground="black")
        self.textpass.configure(selectbackground="#c4c4c4")
        self.textpass.configure(selectforeground="black")

        self.buttlogin = tk.Button(self.top,command=self.userwin)
        self.buttlogin.place(relx=0.352, rely=0.757, height=42, width=168)
        self.buttlogin.configure(activebackground="#ececec")
        self.buttlogin.configure(activeforeground="#000000")
        self.buttlogin.configure(background="#2aa061")
        self.buttlogin.configure(disabledforeground="#a3a3a3")
        self.buttlogin.configure(font="-family {Segoe UI Emoji} -size 14")
        self.buttlogin.configure(foreground="#000000")
        self.buttlogin.configure(highlightbackground="#d9d9d9")
        self.buttlogin.configure(highlightcolor="#000000")
        self.buttlogin.configure(pady="0")
        self.buttlogin.configure(text='''LOGIN''')
        self.buttlogin.configure(width=168)

        self.top.mainloop()
    def userwin(self):
        import sqlite3
        from tkinter import messagebox
        conn = sqlite3.connect("mess.db")
        cur = conn.cursor()
        #------------------------------------------------
        f=open("data.txt",'w')
        f.write(self.textid.get())
        f.close()
        #---------------------------------------------
        try:
            print("select * from user_data where Id=" + self.textid.get() + " and password= '" + self.textpass.get() + "'")
            cursor = conn.execute("select * from user_data where Id="+self.textid.get()+" and password= '"+self.textpass.get()+"'")
            x=cursor.fetchall()
        except(Exception):
            messagebox.showinfo("Error", "Enter proper data")
        print(cursor.fetchall())
        if(len(x)==0):
            messagebox.showinfo("incorrect","Login unsucess")
        else:
            messagebox.showinfo("sucess","hurray..login sucessfull")
            import customerwin
            r=customerwin.cwin()
            r.custwindow()






