from tkinter import *
import tkinter as tk
import os
from tkinter import messagebox
prog_call = sys.argv[0]
prog_location = os.path.split(prog_call)[0]
class spec:
    def special(self):
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9'  # X11 color: 'gray85'
        _ana1color = '#d9d9d9'  # X11 color: 'gray85'
        _ana2color = '#ececec'  # Closest X11 color: 'gray92'

        self.top = Toplevel()
        self.top.geometry("548x357+571+230")
        self.top.title("New Toplevel")
        self.top.configure(background="#34c8d8")

        self.spf1 = tk.Frame(self.top)
        self.spf1.place(relx=0.0, rely=0.0, relheight=0.266, relwidth=1.013)
        self.spf1.configure(relief='groove')
        self.spf1.configure(borderwidth="2")
        self.spf1.configure(relief="groove")
        self.spf1.configure(background="#2733d8")
        self.spf1.configure(width=555)

        self.slbl1 = tk.Label(self.spf1)
        self.slbl1.place(relx=0.306, rely=0.316, height=42, width=219)
        self.slbl1.configure(background="#2733d8")
        self.slbl1.configure(disabledforeground="#a3a3a3")
        self.slbl1.configure(font="-family {Arial} -size 16")
        self.slbl1.configure(foreground="#ffffff")
        self.slbl1.configure(text='''Today's special''')

        self.slbl2 = tk.Label(self.top)
        self.slbl2.place(relx=0.073, rely=0.42, height=39, width=146)
        self.slbl2.configure(activebackground="#f9f9f9")
        self.slbl2.configure(activeforeground="black")
        self.slbl2.configure(background="#675fd8")
        self.slbl2.configure(disabledforeground="#a3a3a3")
        self.slbl2.configure(font="-family {Times New Roman} -size 12")
        self.slbl2.configure(foreground="#ffffff")
        self.slbl2.configure(highlightbackground="#d9d9d9")
        self.slbl2.configure(highlightcolor="black")
        self.slbl2.configure(text='''First dish''')

        self.slbl3 = tk.Label(self.top)
        self.slbl3.place(relx=0.073, rely=0.616, height=39, width=146)
        self.slbl3.configure(activebackground="#f9f9f9")
        self.slbl3.configure(activeforeground="black")
        self.slbl3.configure(background="#675fd8")
        self.slbl3.configure(disabledforeground="#a3a3a3")
        self.slbl3.configure(font="-family {Times New Roman} -size 12")
        self.slbl3.configure(foreground="#ffffff")
        self.slbl3.configure(highlightbackground="#d9d9d9")
        self.slbl3.configure(highlightcolor="black")
        self.slbl3.configure(text='''Second dish''')

        self.txtdish1 = tk.Entry(self.top)
        self.txtdish1.place(relx=0.365, rely=0.42, height=36, relwidth=0.573)
        self.txtdish1.configure(background="white")
        self.txtdish1.configure(disabledforeground="#a3a3a3")
        self.txtdish1.configure(font="-family {Arial} -size 12")
        self.txtdish1.configure(foreground="#000000")
        self.txtdish1.configure(highlightbackground="#d9d9d9")
        self.txtdish1.configure(highlightcolor="black")
        self.txtdish1.configure(insertbackground="black")
        self.txtdish1.configure(selectbackground="#c4c4c4")
        self.txtdish1.configure(selectforeground="black")

        self.txtdish2 = tk.Entry(self.top)
        self.txtdish2.place(relx=0.365, rely=0.616, height=36, relwidth=0.573)
        self.txtdish2.configure(background="white")
        self.txtdish2.configure(disabledforeground="#a3a3a3")
        self.txtdish2.configure(font="-family {Arial} -size 12")
        self.txtdish2.configure(foreground="#000000")
        self.txtdish2.configure(highlightbackground="#d9d9d9")
        self.txtdish2.configure(highlightcolor="black")
        self.txtdish2.configure(insertbackground="black")
        self.txtdish2.configure(selectbackground="#c4c4c4")
        self.txtdish2.configure(selectforeground="black")

        self.menubar = tk.Menu(self.top, font="TkMenuFont", bg=_bgcolor, fg=_fgcolor)
        self.top.configure(menu=self.menubar)

        self.textenter = tk.Button(self.top,command=self.enter)
        self.textenter.place(relx=0.274, rely=0.84, height=42, width=228)
        self.textenter.configure(activebackground="#ececec")
        self.textenter.configure(activeforeground="#000000")
        self.textenter.configure(background="#675fd8")
        self.textenter.configure(disabledforeground="#a3a3a3")
        self.textenter.configure(font="-family {Segoe UI} -size 12")
        self.textenter.configure(foreground="#ffffff")
        self.textenter.configure(highlightbackground="#d9d9d9")
        self.textenter.configure(highlightcolor="black")
        self.textenter.configure(pady="0")
        self.textenter.configure(text='''Enter''')
        self.textenter.configure(width=228)
        self.top.mainloop()
    def enter(self):
        r=open("response.txt","w")
        r.write(" ")
        r.close()
        if (self.txtdish1.get()==" " and self.txtdish2.get()==" " ):
            messagebox.showinfo("Error","dish is not blanck")
        else:
            f=open("dish1.txt",'w')
            f.write(self.txtdish1.get())
            f.close()
            d=open("dish2.txt","w")
            d.write(self.txtdish2.get())
            d.close()
            messagebox.showinfo("Message","special menu added")

