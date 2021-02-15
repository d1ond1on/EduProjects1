from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from tkinter import ttk
import os
from datetime import datetime
# установка параметров главного окна - положение, имя и иконка окна
root = Tk()
# root.geometry('1000x400+800+300')
root.title('D1 refract')
root.iconbitmap('G:\Python\project\gameProject\\notepad\python.ico')
#function for menu
def about_prog():
    messagebox.showinfo(title='about prog', message='Created by D1\n'
                                                    '1 кнопка - указываем путь к рабочей папке\n'
                                                    '2 кнопка - вытаскиваем из подпапок всефайлы в рабочую папку\n'
                                                    '3 кнопка - раскидываем файлы по папкам, с датами последних изменений \n'
                                                    '4 кнопка - перемещаем все файлы размером больше указанного в папку to_large\n'
                                                    'не забываем в поле, рядом с 4 кнопкой, указать размеры в мегабайтах')
def my_quite():
    answer = messagebox.askyesnocancel(title='Vihod', message='zakrit progr?')
    if answer:
        root.quit()
#function for main window
def get_path():
    path = filedialog.askdirectory()
    entry.delete(0, END)
    entry.insert(0, path)

def up_file():
    cur_path = entry.get()
    if cur_path :
        for root, dirs, files in os.walk(cur_path) :
            for i in files :
                path = os.path.join(root, i)
                mtime = os.path.getmtime(path)
                os.renames(path, os.path.join(cur_path, i))
        messagebox.showinfo('Succes', 'sortirvka vipolnena uspeshno')

    else :
        messagebox.showwarning(message='Ykajite papky s photo')

def sort_file():
    cur_path = entry.get()
    if cur_path :
        for root, dirs, files in os.walk(cur_path) :
            for i in files :
                path = os.path.join(root, i)
                mtime = os.path.getmtime(path)
                date = datetime.fromtimestamp(mtime)
                date = date.strftime('%Y-%m-%d')  # YYYY-MM-DD
                date_folder = os.path.join(cur_path, date)
                if not os.path.exists(date_folder) :
                    os.mkdir(date_folder)
                os.renames(path, os.path.join(date_folder, i))
        messagebox.showinfo('Succes', 'sortirvka vipolnena uspeshno')

    else :
        messagebox.showwarning(message='Ykajite papky s photo')

def sort_fsize():
    cur_path = entry.get()
    to_large = entry2.get()
    if cur_path and to_large :
        for root, dirs, files in os.walk(cur_path) :
            for i in files :
                path = os.path.join(root, i)
                size = os.path.getsize(path)
                to_large = int(entry2.get()) * 1000000
                size_path = os.path.join(cur_path, 'to_large')
                if size > to_large:
                    os.renames(path, os.path.join(size_path, i))
                else:
                    pass
        messagebox.showinfo('Succes', 'sortirvka vipolnena uspeshno')
    else :
        messagebox.showinfo(message='Укажите путь к папке и/или размер файла в Мб для сортировки  и перемещения в папку to-large')

# Меню
main_menu = Menu(root)
root.config(menu=main_menu)

file_menu = Menu(main_menu, tearoff=0)
file_menu.add_command(label='Exit', command=my_quite)
main_menu.add_cascade(label='File', menu=file_menu)

theme_menu = Menu(main_menu, tearoff=0)
theme_menu.add_command(label='O programme', command= about_prog)
main_menu.add_cascade(label='raznoe', menu=theme_menu)

# Кнопки

button1 = Button(root, text='Указать путь к рабочей папке', command= get_path)
button2 = Button(root, text='Вытащить все файлы из подпапок в корень', command= up_file)
button3 = Button(root, text='сортировка по дате', command= sort_file)
button4 = Button(root, text='сортировка по размеру', command= sort_fsize)
button1.grid(row=0, column=0)
button2.grid(row=1, column=0)
button3.grid(row=2, column=0)
button4.grid(row=3, column=0)
entry = Entry(root)

entry.grid(row=0,column=1)
entry2 = Entry(root)

entry2.grid(row=3,column=1)


root.mainloop()
