import tkinter as tk
from tkinter import *
from tkinter import font
from tkinter import ttk
from tkinter import colorchooser
win = tk.Tk()
win.geometry("1000x800+100+0")
win.title("text editer")
fontnow="Arial"
fontsize=12
def change_font(event):
    global fontnow
    fontnow=fontbox.get()
    textediter.config(font=(fontnow,fontsize))
def change_size(event):
    global sizenow
    sizenow=sizebox.get()
    textediter.config(font=(fontnow,sizenow))
def chooser():
    sel_color=colorchooser.askcolor("blue",title="select color")
    textediter.config(fg=sel_color[1])
def chooser2():
    bg_color=colorchooser.askcolor("light blue",title="Select Background Color")
    textediter.config(bg=bg_color[1])
option=tuple(range(2,100,2))
frame=tk.Frame(win,height=50,width=1000,bg="yellow")
frame.grid(row=0,column=0)
textediter = tk.Text(win)
textediter.config(wrap="word",relief=tk.FLAT,height=200,width=300)
textediter.place(x=0,y=50)
label=tk.Label(frame,text="font",bg="yellow",font=("arial",20,"bold"))
label.place(x=0,y=0)
label=tk.Label(frame,text="size",bg="yellow",font=("arial",20,"bold"))
label.place(x=300,y=0)
fontselect=tk.StringVar()
fonttable=font.families()
fontbox=ttk.Combobox(frame,width=20,textvariable=fontselect,state="readonly",value=fonttable,height=40)
fontbox.place(x=100,y=10)
sizebox=ttk.Combobox(frame,width=20,textvariable=fontsize,state="readonly",value=option,height=40)
sizebox.place(x=400,y=10)
fontbox.current(fontbox.index(0))
sizebox.current(0)
btn=tk.Button(frame,text="choose color",font=("Arial",12),bd=8,command=chooser)
btn.place(x=600,y=0)
btn2=tk.Button(frame,text="Choose screen Color",font=("Arial", 12),bd=8,command=chooser2)
btn2.place(x=800, y=0)
fontbox.bind("<<ComboboxSelected>>",change_font)
sizebox.bind("<<ComboboxSelected>>",change_size)
win.mainloop()