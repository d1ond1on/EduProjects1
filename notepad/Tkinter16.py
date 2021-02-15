from tkinter import *
from tkinter import messagebox
from tkinter import filedialog

root = Tk()
root.geometry('1000x400+800+300')

main_menu = Menu(root)
root.config(menu=main_menu)
#info at menu button
def about_prog():
    messagebox.showinfo(title='about prog', message='notepad ver godnotepad ver godnotepad ver godnotepad '
                                                    'ver godnotepad ver godnotepad ver godnotepad ver godnotepad ver god')
#quit
def my_quite():
    answer = messagebox.askyesnocancel(title='Vihod', message='zakrit progr?')
    if answer:
        root.quit()
#open file in menu action
def open_file():
    file_pass = filedialog.askopenfilename(title='Vibor file', filetypes=(('textovie doci','*.txt'),('vse file','*.*')))

    if file_pass:
        text_area.delete('1.0', END)
        text_area.insert('1.0', open(file_pass, encoding='utf-8').read())
#save as
def save_file():
    file_pass = filedialog.asksaveasfilename(title='save', filetypes=(('textovie doci', '*.txt'), ('vse file', '*.*')))
    f = open(file_pass, 'w', encoding='utf-8')
    text = text_area.get('1.0', END)
    f.write(text)
    f.close()

#change theme( dark and light)
def change_theme(theme):
    text_area['bg'] = theme_colours[theme]['text_bg']
    text_area['fg'] = theme_colours[theme]['text_fg']
    text_area['insertbackground'] = theme_colours[theme]['cursor']
    text_area['selectbackground'] = theme_colours[theme]['select_bg']

#Menu button (open, save, quit action)
file_menu = Menu(main_menu, tearoff=1)
file_menu.add_command(label='Open', command=open_file)
file_menu.add_command(label='Save', command=save_file)
file_menu.add_separator()
file_menu.add_command(label='Exit', command=my_quite)
main_menu.add_cascade(label='File', menu=file_menu)
# Menu button (change theme and info about
theme_menu = Menu(main_menu, tearoff=0)
theme_menu_sub = Menu(theme_menu, tearoff=0)
theme_menu_sub.add_command(label='light', command=lambda :change_theme('light'))
theme_menu_sub.add_command(label='Dark', command=lambda :change_theme('dark'))
theme_menu.add_cascade(label='Oformlenie', menu=theme_menu_sub)
theme_menu.add_command(label='O programme', command=about_prog)
main_menu.add_cascade(label='raznoe', menu=theme_menu)
# Main window
f_text = Frame(root)
f_text.pack(fill=BOTH, expand=1)

# themes parametres
theme_colours = {
    'dark': {
        'text_bg': '#343D46', 'text_fg': '#C6DEC1', 'cursor': '#EDA756', 'select_bg': '#4E5A65'

    },
    'light': {
        'text_bg':'#fff', 'text_fg': '#000', 'cursor': '#8000FF', 'select_bg': '#777'
    }
}

#text field
text_area = Text(f_text, bg=theme_colours['dark']['text_bg'], fg=theme_colours['dark']['text_fg'], padx=10,
                 pady=10, insertbackground=theme_colours['dark']['cursor'],
                 selectbackground=theme_colours['dark']['select_bg'], width=30, wrap=WORD, spacing3=10,
                 font=('Courier New', 20))
text_area.pack(fill=BOTH,expand=1, side=LEFT)
#scroll line, right side
scroll = Scrollbar(f_text, command=text_area.yview)
scroll.pack(fill=Y,side=LEFT)
text_area.configure(yscrollcommand=scroll.set)

root.mainloop()