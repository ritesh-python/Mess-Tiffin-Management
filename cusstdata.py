from tkinter import *
import tkinter as tk
import os
from tkinter import  messagebox
prog_call = sys.argv[0]
prog_location = os.path.split(prog_call)[0]
class cwin:
    def custwindow(self):


        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        self.top = Toplevel()
        self.top.geometry("876x602+571+230")
        self.top.title("New Toplevel")
        self.top.configure(background="#34c8d8")
        self.top.configure(highlightbackground="#d9d9d9")
        self.top.configure(highlightcolor="black")

        self.menubar = tk.Menu(self.top, font="TkMenuFont", bg=_bgcolor, fg=_fgcolor)
        self.top.configure(menu=self.menubar)

        self.cdf3 = tk.Frame(self.top)
        self.cdf3.place(relx=0.0, rely=0.0, relheight=1.005, relwidth=0.325)
        self.cdf3.configure(relief='groove')
        self.cdf3.configure(borderwidth="2")
        self.cdf3.configure(relief="groove")
        self.cdf3.configure(background="#7272d8")
        self.cdf3.configure(width=285)

        self.cdf1 = tk.Frame(self.cdf3)
        self.cdf1.place(relx=0.035, rely=0.182, relheight=0.107, relwidth=0.93)
        self.cdf1.configure(relief='groove')
        self.cdf1.configure(borderwidth="2")
        self.cdf1.configure(relief="groove")
        self.cdf1.configure(background="#8cbfd8")
        self.cdf1.configure(width=265)

        self.cdlbl3 = tk.Label(self.cdf1)
        self.cdlbl3.place(relx=0.075, rely=0.0, height=51, width=225)
        self.cdlbl3.configure(activebackground="#f9f9f9")
        self.cdlbl3.configure(activeforeground="black")
        self.cdlbl3.configure(background="#8cbfd8")
        self.cdlbl3.configure(disabledforeground="#a3a3a3")
        self.cdlbl3.configure(font="-family {Segoe UI Semibold} -size 13 -weight bold")
        self.cdlbl3.configure(foreground="#ffffff")
        self.cdlbl3.configure(highlightbackground="#d9d9d9")
        self.cdlbl3.configure(highlightcolor="black")
        self.cdlbl3.configure(text='''Options''')

        self.mail = tk.Button(self.cdf3,command=self.mailcust)
        self.mail.place(relx=0.105, rely=0.347, height=42, width=218)
        self.mail.configure(activebackground="#ececec")
        self.mail.configure(activeforeground="#000000")
        self.mail.configure(background="#d9d9d9")
        self.mail.configure(disabledforeground="#a3a3a3")
        self.mail.configure(foreground="#000000")
        self.mail.configure(highlightbackground="#d9d9d9")
        self.mail.configure(highlightcolor="black")
        self.mail.configure(pady="0")
        self.mail.configure(text='''Send Mail''')
        self.mail.configure(width=218)

        self.deletecust = tk.Button(self.cdf3,command=self.delcust)
        self.deletecust.place(relx=0.105, rely=0.463, height=42, width=218)
        self.deletecust.configure(activebackground="#ececec")
        self.deletecust.configure(activeforeground="#000000")
        self.deletecust.configure(background="#d9d9d9")
        self.deletecust.configure(disabledforeground="#a3a3a3")
        self.deletecust.configure(foreground="#000000")
        self.deletecust.configure(highlightbackground="#d9d9d9")
        self.deletecust.configure(highlightcolor="black")
        self.deletecust.configure(pady="0")
        self.deletecust.configure(text='''Delete customer''')

        self.cdlbl1 = tk.Frame(self.top)
        self.cdlbl1.place(relx=0.0, rely=0.0, relheight=0.174, relwidth=0.999)
        self.cdlbl1.configure(relief='groove')
        self.cdlbl1.configure(borderwidth="2")
        self.cdlbl1.configure(relief="groove")
        self.cdlbl1.configure(background="#2316d8")
        self.cdlbl1.configure(width=875)

        self.cdlbl2 = tk.Label(self.cdlbl1)
        self.cdlbl2.place(relx=0.354, rely=0.286, height=51, width=225)
        self.cdlbl2.configure(background="#2316d8")
        self.cdlbl2.configure(disabledforeground="#a3a3a3")
        self.cdlbl2.configure(font="-family {Segoe UI Semibold} -size 16 -weight bold")
        self.cdlbl2.configure(foreground="#ffffff")
        self.cdlbl2.configure(text='''Customer Data''')

        self.list2 = tk.Listbox(self.top)
        self.list2.place(relx=0.331, rely=0.183, relheight=0.791, relwidth=0.667)
        scrolllbar=Scrollbar(self.top,orient="horizontal")
        scrolllbar.configure(command=self.list2.xview)
        scrolllbar.pack(side="bottom",fill="x")
        self.list2.configure(background="white")
        self.list2.configure(disabledforeground="#a3a3a3")
        self.list2.configure(font="-family {Arial} -size 13")
        self.list2.configure(foreground="#000000")
        self.list2.configure(width=584)
        self.list2.insert(1,"ID NO      NAME    ADDRESS    MOBILE NO    EMAIL ADDRESS   START DATE   PASSWORD")


        import sqlite3
        conn = sqlite3.connect("mess.db")
        cur = conn.cursor()
        cursor=conn.execute("select * from user_data order by Id")
        row=cursor.fetchall()
        self.count=2
        for data in row:
           self.list2.insert(int(self.count),data)
           print(data)
           self.count=self.count+1
        conn.close()


        self.top.mainloop()


    def delcust(self):
            x = self.list2.curselection()
            self.ls=list(x)
            print(self.ls[0])
            if (messagebox.askyesno("Delete data","do you want to delete data")==True):
                print("yes")
                import sqlite3
                con = sqlite3.connect("mess.db")
                cur = con.cursor()
                query = " delete from user_data where id= "+str(self.ls[0])
                print(query)
                cur.execute(query)
                con.commit()
                con.close()
            else:
                print("no")

    def mailcust(self):
        y = self.list2.curselection()
        lsdata = list(y)
        print(lsdata)
        data=str(lsdata[0])
        import sqlite3
        con = sqlite3.connect("mess.db")
        cursor = con.execute("select name,email_id,start_date from user_data where id= "+data)
        for row in cursor:
            nameu=row[0]
            sender=row[1]
            dates=row[2]
        con.close()
        import smtplib
        try:
            idm="harrypotter2ritesh@gmail.com"
            passw="Ritesh@123456"
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.ehlo()
            server.starttls()
            server.login(idm,passw)
            message = "Hellow "+nameu+", \n     This is mess tifin service, your tifin starting date is"+dates+". and your account has been completed this month, please pay of this month"
            server.sendmail(idm,sender, message)
            server.quit()
            messagebox.showinfo("sucess","mail sent to"+nameu)
        except(Exception):
            print(Exception)
            messagebox.showinfo("failed","enter proper mail")
            print("Email failed")
