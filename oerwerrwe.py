from tkinter import *
import tkinter as tk
import os
from tkinter import filedialog
prog_call = sys.argv[0]
prog_location = os.path.split(prog_call)[0]
class own:
    def osection(self):
        self.top = Toplevel()
        self.top.configure(background="#b8bfd8")
        self.top.geometry("1284x680+312+238")
        self.f1 = tk.Frame(self.top)
        self.f1.place(relx=0.0, rely=0.0, relheight=0.184, relwidth=1.001)
        self.f1.configure(relief='groove')
        self.f1.configure(borderwidth="2")
        self.f1.configure(relief="groove")
        self.f1.configure(background="#7620d8")
        self.f1.configure(highlightbackground="#4a66ef")
        self.f1.configure(highlightcolor="#630930")
        self.f1.configure(width=1285)

        self.m1 = tk.Label(self.f1)
        self.m1.place(relx=0.031, rely=0.08, height=101, width=1217)
        self.m1.configure(background="#54d854")
        self.m1.configure(disabledforeground="#39a380")
        self.m1.configure(font="-family {Wide Latin} -size 22")
        self.m1.configure(foreground="#000000")
        self.m1.configure(highlightcolor="#416352")
        self.m1.configure(text='''Mess and Tifin Service system''')
        self.m1.configure(width=1217)

        self.f2 = tk.Frame(self.top)
        self.f2.place(relx=0.0, rely=0.191, relheight=0.11, relwidth=1.001)
        self.f2.configure(relief='groove')
        self.f2.configure(borderwidth="2")
        self.f2.configure(relief="groove")
        self.f2.configure(background="#ffffff")
        self.f2.configure(width=1285)

        self.seco = tk.Label(self.f2)
        self.seco.place(relx=0.342, rely=0.0, height=71, width=379)
        self.seco.configure(background="#ffffff")
        self.seco.configure(disabledforeground="#a3a3a3")
        self.seco.configure(font="-family {Segoe UI} -size 24")
        self.seco.configure(foreground="#000000")
        self.seco.configure(text='''OWNER SECTION''')

        self.f3 = tk.Frame(self.top)
        self.f3.place(relx=0.117, rely=0.338, relheight=0.625, relwidth=0.775)
        self.f3.configure(relief='groove')
        self.f3.configure(borderwidth="2")
        self.f3.configure(relief="groove")
        self.f3.configure(background="#a6d8d3")
        self.f3.configure(width=995)

        self.add = tk.Button(self.f3)
        self.add.place(relx=0.191, rely=0.071, height=142, width=168)
        self.add.configure(activebackground="#ececec")
        self.add.configure(activeforeground="#000000")
        self.add.configure(background="#3f62d8")
        self.add.configure(command=add_data)
        self.add.configure(disabledforeground="#a3a3a3")
        self.add.configure(foreground="#000000")
        self.add.configure(highlightbackground="#5dd4d8")
        self.add.configure(highlightcolor="black")
        photo_location = os.path.join(prog_location, "cards.png")
        self._img0 = tk.PhotoImage(file=photo_location)
        self.add.configure(image=self._img0)
        self.add.configure(pady="0")
        self.add.configure(text='''Button''')
        self.add.configure(width=168)

        self.menu = tk.Button(self.f3)
        self.menu.place(relx=0.633, rely=0.071, height=142, width=168)
        self.menu.configure(activebackground="#ececec")
        self.menu.configure(activeforeground="#000000")
        self.menu.configure(background="#3f62d8")
        self.menu.configure(command=menudish)
        self.menu.configure(disabledforeground="#a3a3a3")
        self.menu.configure(foreground="#000000")
        self.menu.configure(highlightbackground="#5dd4d8")
        self.menu.configure(highlightcolor="black")
        photo_location = os.path.join(prog_location, "13155119661987559928Restaurant Symbol.svg.thumb.png")
        self._img1 = tk.PhotoImage(file=photo_location)
        self.menu.configure(image=self._img1)
        self.menu.configure(pady="0")
        self.menu.configure(text='''Button''')

        self.logout = tk.Button(self.f3)
        self.logout.place(relx=0.633, rely=0.565, height=142, width=168)
        self.logout.configure(activebackground="#ececec")
        self.logout.configure(activeforeground="#000000")
        self.logout.configure(background="#3f62d8")
        self.logout.configure(command=logout)
        self.logout.configure(disabledforeground="#a3a3a3")
        self.logout.configure(foreground="#000000")
        self.logout.configure(highlightbackground="#5dd4d8")
        self.logout.configure(highlightcolor="black")
        photo_location = os.path.join(prog_location, "222.png")
        self._img2 = tk.PhotoImage(file=photo_location)
        self.logout.configure(image=self._img2)
        self.logout.configure(pady="0")
        self.logout.configure(text='''Button''')

        self.adl = tk.Label(self.f3)
        self.adl.place(relx=0.181, rely=0.447, height=31, width=185)
        self.adl.configure(background="#a6d8d3")
        self.adl.configure(disabledforeground="#a3a3a3")
        self.adl.configure(foreground="#000000")
        self.adl.configure(text='''ADD NEW CUSTOMER''')

        self.sml = tk.Label(self.f3)
        self.sml.place(relx=0.171, rely=0.918, height=31, width=185)
        self.sml.configure(activebackground="#f9f9f9")
        self.sml.configure(activeforeground="black")
        self.sml.configure(background="#a6d8d3")
        self.sml.configure(disabledforeground="#a3a3a3")
        self.sml.configure(foreground="#000000")
        self.sml.configure(highlightbackground="#d9d9d9")
        self.sml.configure(highlightcolor="black")
        self.sml.configure(text='''SHOW DATA''')

        self.eml = tk.Label(self.f3)
        self.eml.place(relx=0.633, rely=0.447, height=31, width=185)
        self.eml.configure(activebackground="#f9f9f9")
        self.eml.configure(activeforeground="black")
        self.eml.configure(background="#a6d8d3")
        self.eml.configure(disabledforeground="#a3a3a3")
        self.eml.configure(foreground="#000000")
        self.eml.configure(highlightbackground="#d9d9d9")
        self.eml.configure(highlightcolor="black")
        self.eml.configure(text='''ENTER TODAY'S MENU''')

        self.show = tk.Button(self.f3)
        self.show.place(relx=0.191, rely=0.565, height=142, width=168)
        self.show.configure(activebackground="#ececec")
        self.show.configure(activeforeground="#000000")
        self.show.configure(background="#3f62d8")
        self.show.configure(command=showdish)
        self.show.configure(disabledforeground="#a3a3a3")
        self.show.configure(foreground="#000000")
        self.show.configure(highlightbackground="#5dd4d8")
        self.show.configure(highlightcolor="black")
        photo_location = os.path.join(prog_location, "11.png")
        self._img3 = tk.PhotoImage(file=photo_location)
        self.show.configure(image=self._img3)
        self.show.configure(pady="0")
        self.show.configure(text='''Button''')

        self.lml = tk.Label(self.f3)
        self.lml.place(relx=0.633, rely=0.894, height=31, width=200)
        self.lml.configure(activebackground="#f9f9f9")
        self.lml.configure(activeforeground="black")
        self.lml.configure(background="#a6d8d3")
        self.lml.configure(disabledforeground="#a3a3a3")
        self.lml.configure(foreground="#000000")
        self.lml.configure(highlightbackground="#d9d9d9")
        self.lml.configure(highlightcolor="black")
        self.lml.configure(text='''Show Response of customer''')

        self.top.mainloop()

def add_data():
    print("addata")
    import adddata
    #adddata
    q=adddata.add()
    q.custdataadd()
def logout():
    print("logout")
    filr=Toplevel()
    eml = tk.Label(filr)
    eml.place(height=100, width=400)
    eml.configure(activebackground="#f9f9f9")
    eml.configure(activeforeground="black")
    eml.configure(background="#a6d8d3")
    eml.configure(disabledforeground="#a3a3a3")
    eml.configure(foreground="#000000")
    eml.configure(highlightbackground="#d9d9d9")
    eml.configure(highlightcolor="black")

    f=open("response.txt",'r')
    x=f.read()
    eml.configure(text=x)

def showdish():
    print("menussss")
    import cusstdata
    c=cusstdata.cwin()
    c.custwindow()
def menudish():
    import todayspec
    t=todayspec.spec()
    t.special()
#o=own()
#o.osection()
