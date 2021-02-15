from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from tkinter import ttk
import os
from datetime import datetime



def choose_dir():
    dir_path = filedialog.askdirectory()
    e_path.delete(0, END)
    e_path.insert(0,dir_path)

def f_start():
    cur_path = e_path.get()
    if cur_path:
        for root, dirs, files in os.walk(cur_path):
            for i in files:
                path = os.path.join(root, i)
                mtime = os.path.getmtime(path)
                date = datetime.fromtimestamp(mtime)
                date = date.strftime('%Y-%m-%d') # YYYY-MM-DD
                date_folder = os.path.join(cur_path,date)
                if not os.path.exists(date_folder):
                    os.mkdir(date_folder)
                os.renames(path, os.path.join(date_folder,i))
        messagebox.showinfo('Succes', 'sortirvka vipolnena uspeshno')
        e_path.delete(0, END)
    else:
        messagebox.showwarning('Ykajite papky s photo')

root = Tk()
root.title('Photosort')
root.geometry('500x150+1000+300')

s = ttk.Style()
s.configure('my.TButton', font=('Helvetica',15))



frame = Frame(root, bg='#56ADFF', bd=5)
frame.pack(padx=10, pady=10, fill=X)

e_path = ttk.Entry(frame)
e_path.pack(side=LEFT, ipady=2, expand=1, fill=X)

btn_dialog = ttk.Button(frame, text='Vibrat papky', command=choose_dir)
btn_dialog.pack(side=LEFT, padx=5)

btn_start = ttk.Button(root, text='start', style='my.TButton', command=f_start)
btn_start.pack(fill=X, padx=10)

root.mainloop()