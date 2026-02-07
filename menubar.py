import tkinter as tk
from tkinter import Tk
from tkinter import colorchooser
from tkinter import messagebox
from tkinter import filedialog
from tkinter import StringVar
win=tk.Tk()
win.geometry("800x800")
win.title("menu")
textediter = tk.Text(win)
textediter.config(wrap="word",relief=tk.FLAT,height=800,width=300)
textediter.place(x=0,y=0)
mainmenu=tk.Menu(win)
win.config(menu=mainmenu)
file=tk.Menu(mainmenu,tearoff=False,)
edit=tk.Menu(mainmenu,tearoff=False)
view=tk.Menu(mainmenu,tearoff=False)
text_url=StringVar()
def btn2():
    bg_color=colorchooser.askcolor("light blue",title="Select Background Color")
    textediter.config(bg=bg_color[1])
def chooser():
    sel_color=colorchooser.askcolor("blue",title="select color")
    textediter.config(fg=sel_color[1])
def new():
    response=messagebox.askyesno("warning", "do you want make new file")
    if response:
        textediter.delete('1.0',tk.END) 
def cut_text():
    textediter.event_generate("<<Cut>>")
def paste_text():
    textediter.event_generate("<<Paste>>")
def copy_text():
    textediter.event_generate("<<Copy>>")

def save_file():
    global text_url
    if text_url.get():  
        with open(text_url.get(), "w") as f:
            content = textediter.get("1.0", tk.END)
            f.write(content)
            messagebox.showinfo("success", "file save")
    else:
        file_path = filedialog.asksaveasfilename(
            defaultextension=".txt",
            title="select file",
            filetypes=(("Textfiles", ".txt"), ("allfiles", ".*"))
        )
        if file_path:
            try:
                content = textediter.get("1.0", tk.END)
                with open(file_path, "w") as f:
                    f.write(content)
                    messagebox.showinfo("success", "file save")
                    text_url.set(file_path)  
            except Exception as e:
                messagebox.showerror("error", str(e))

def open_file():
    path = filedialog.askopenfilename()
    if path:
        textediter.delete("1.0", tk.END)
        textediter.insert("1.0", open(path).read())
def saveas_file():
    global text_url
    
    file_path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=(("Textfiles", ".txt"), ("allfiles", ".*"))
    )
    confirm = messagebox.askyesno(
        "Confirm",
        "Do you want to replace this file?"
    )
    if not file_path:
        return
    if not confirm:
        return
    try:
        content = textediter.get("1.0", tk.END)
        with open(file_path, "w") as f:
            f.write(content)
            messagebox.showinfo("saved","file saved sucessfully")
            text_url.set(file_path)  
    except Exception as e:
        messagebox.showerror("error", str(e))
file.add_cascade(label="New File",command=new)
file.add_separator()
file.add_cascade(label="Open File",command=open_file)
file.add_cascade(label="Save",command=save_file)
file.add_cascade(label="Save As",command=saveas_file)
file.add_separator()
file.add_cascade(label="exit")

edit.add_cascade(label="cut",command=cut_text)
edit.add_cascade(label="copy",command=copy_text)
edit.add_cascade(label="paste",command=paste_text)
edit.add_separator()
edit.add_cascade(label="find")
edit.add_separator()
edit.add_cascade(label="replace")

view.add_cascade(label="background",command=btn2)
view.add_separator()
view.add_cascade(label="foreground",command=chooser)

mainmenu.add_cascade(label="file",menu=file)
mainmenu.add_cascade(label="edit",menu=edit)
mainmenu.add_cascade(label="view",menu=view)
win.mainloop()