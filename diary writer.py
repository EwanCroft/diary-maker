import datetime
import os
import PySimpleGUI as sg

home_dir = os.path.expanduser("~")
diary_root_folder = os.path.join(home_dir, "Documents", "Diary")

if not os.path.exists(diary_root_folder):
    os.mkdir(diary_root_folder)

def on_submit(values):
    entry_text = values['-ENTRY-']

    today = datetime.date.today()
    now = datetime.datetime.now().time()
    date_directory = os.path.join(diary_root_folder, str(today))
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
    sg.Popup(f"{file_name}\ncreated", title='Diary Entry')

layout = [
    [sg.Text('Diary entry:')],
    [sg.Multiline(key='-ENTRY-', size=(40, 5))],
    [sg.Button('Submit'), sg.Button('Cancel')]
]

window = sg.Window('Diary', layout, background_color='#BEBEBE')

while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Cancel'):
        break
    if event == 'Submit':
        on_submit(values)

window.close()
