from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import time
import json
import requests
# function
#about
def about_prog():
    messagebox.showinfo(title='about prog', message='Created by D1\n')
#quit
def my_quite():
    answer = messagebox.askyesnocancel(title='Vihod', message='zakrit progr?')
    if answer:
        root.quit()
#request time
def tick():
    label1.after(200, tick)
    label1['text'] = time.strftime('%H:%M:%S')
#button create function
def buttns():
    schetchik = 3
    for i in k:
        BASE_SUMM = entry4.get()
        l = k[i]
        valute_name = l['Name']
        valute_nominal = l['Nominal']
        valute_kurs = l['Value']
        entry1 = Entry(f_bottom)
        entry1.insert(0,valute_name)
        entry1.grid(row=schetchik, column=0)
        entry2 = Entry(f_bottom)
        entry2.insert(0,valute_nominal)
        entry2.grid(row=schetchik, column=1)
        entry3 = Entry(f_bottom)
        entry3.insert(0, valute_kurs)
        entry3.grid(row=schetchik, column=2)
        sum = round(float(entry3.get()) * int(BASE_SUMM) / int(entry2.get()),2)
        entry5 = Entry(f_bottom)
        entry5.insert(0, sum)
        entry5.grid(row=schetchik, column=5)
        schetchik += 1
#main menu
root = Tk()
root.title('Расчет валют')
root.iconbitmap('G:\Python\project\gameProject\ValuteCalc\d1.ico')
f_top = LabelFrame(root).grid(sticky=W+E)
f_bottom = LabelFrame(root).grid()
main_menu = Menu(root)
root.config(menu=main_menu)
file_menu = Menu(main_menu, tearoff=0)
file_menu.add_command(label='Exit', command=my_quite)
main_menu.add_cascade(label='File', menu=file_menu)

theme_menu = Menu(main_menu, tearoff=0)
theme_menu.add_command(label='O programme', command= about_prog)
main_menu.add_cascade(label='raznoe', menu=theme_menu)
#api availability
zapros_json = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')
if zapros_json.status_code ==200:
    messagebox.showinfo(message='Api по адресу https://www.cbr-xml-daily.ru/daily_json.js доступен, продолжайте')
else:
    messagebox.showinfo(message= 'Api по адресу https://www.cbr-xml-daily.ru/daily_json.js недоступен, попробуйте позже')
    root.destroy()
#api request result (json) refract
zapros_json = zapros_json.json()
time_zap = zapros_json['Date']
time_zap = time.strftime('%D-%T')
k = zapros_json['Valute']
#default summ for echange
BASE_SUMM = 1000
#current time
label = Label(f_top,font='sans 20', text='Текущее время')
label.grid(row=0, column=0, columnspan=3)
label1 = Label(f_top,font='sans 20')
label1.grid(row=0, column=3, columnspan=2)
label1.after_idle(tick)
#request time
label2 = Label(f_bottom, font='sans 20', text='Время выгрузки курса')
label2.grid(row=1, column=0, columnspan=3)
entry = Entry(f_bottom, font='sans 20')
entry.insert(0, time_zap)
entry.grid(row=1, column=3, columnspan=2)
#the top of the table
zag_lab = Label(f_bottom, text='Valute name', height=2).grid(row=2, column=0)
zag_lab = Label(f_bottom, text='Nominal').grid(row=2, column=1)
zag_lab = Label(f_bottom, text='Kurs').grid(row=2, column=2)
zag_lab = Label(f_bottom, text='Kol-vo dlya obmena').grid(row=2, column=3)
zag_lab = Label(f_bottom, text='najat dlya rascheta').grid(row=2, column=4)
zag_lab = Label(f_bottom, text='itogo  v rublyah').grid(row=2, column=5)
# field to entry summ, differ to base sum
entry4 = Entry(f_bottom)
entry4.insert(0, BASE_SUMM)
entry4.grid(row=3, column=3)
# button for recreation result row
btn5 = Button(f_bottom, text='Push to summ', command=buttns)
btn5.grid(row=3, column=4)


root.mainloop()
# https://www.cbr-xml-daily.ru/daily_json.js json file
