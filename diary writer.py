import datetime
import os
from tkinter import Button, Label
import tkinter as tk

home_dir = os.path.expanduser("~")
diary_root_folder = os.path.join(home_dir, "Documents", "Diary")

if not os.path.exists(diary_root_folder):
    os.mkdir(diary_root_folder)
else:
    pass

def on_submit():
    entry_text = entry.get()

    today = datetime.date.today()
    now = datetime.datetime.now().time()
    date_directory = os.path.join(diary_root_folder, today)
    if not os.path.exists(date_directory):
        os.makedirs(date_directory)

    time_str = now.strftime("%H%M%S")
    count = 1
    while True:
        file_name = os.path.join(date_directory, time_str+'.txt')
        if not os.path.exists(file_name):
            break
        count += 1

    with open(file_name, "w") as f:
        f.write(entry_text)

    file_name = time_str+'.txt'
    label.config(text=f"{file_name}\ncreated")

window = tk.Tk()

window.geometry('200x140')
window.configure(background='#BEBEBE')
window.title('Diary')

Button(window, text='Submit', bg='#BEBEBE', font=('arial', 12, 'normal'), command=on_submit).place(x=115, y=90)
label = Label(window, text='', bg='#BEBEBE', font=('arial', 10, 'normal'))
label.place(x=15, y=90)

e = Label(window, text='Diary entry:', bg='#BEBEBE', font=('arial', 12, 'normal')).place(x=15, y=10)

entry=tk.Entry(window)
entry.place(x=15, y=40)

window.mainloop()
