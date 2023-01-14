import json
import os
import codecs
import datetime
import time

home_dir = os.path.expanduser("~")
Diary_root_folder = os.path.join(home_dir, "Documents", "Diary")

if not os.path.exists(Diary_root_folder):
    os.makedirs(Diary_root_folder)
else:
    pass

export = input("Do you have a DayOne export? (y/n):\n")
if export == "y":
    JSON_data = input("Enter where the DayOne export is located (JSON *.zip file):\n")
    try:
        user_entry_count = int(input(f"How many entries are there in {JSON_data}?:\n"))
    except ValueError:
        print("Please enter a valid number.")
        user_entry_count = int(input(f"How many entries are there in {JSON_data}?:\n"))
    try:
        with codecs.open(f"{JSON_data}", "r", encoding = "UTF-8") as f:
            data = json.load(f)

            count_2 = 1
            for count in range(user_entry_count):
                creation_date = data["entries"][count]["creationDate"]
                date = datetime.datetime.strptime(creation_date, '%Y-%m-%dT%H:%M:%SZ').date()
                time_orig = datetime.datetime.strptime(creation_date, '%Y-%m-%dT%H:%M:%SZ').time()
                time = time_orig.strftime("%H%M%S")
                text = data["entries"][count]["text"].replace("#### ", "").replace("#", "").replace("\\", "")

                date_folder = os.path.join(Diary_root_folder, str(date))
                if not os.path.exists(date_folder):
                    os.makedirs(date_folder)

                time_file = os.path.join(date_folder, time+'.txt')
                with open(time_file, "w", encoding = "UTF-8") as f:
                    try:
                        f.write(text)
                    except Exception as e:
                        print(e)

                count_2 += 1
            print("Entries saved.")
    except FileNotFoundError:
        print("File not found, please enter a valid file path.")
        JSON_data = input("Enter where the DayOne export is located (JSON *.zip file):\n")

elif export == "n":
    print("Why are you using this script? go use diary writer.py already")
    time.sleep(3)
    quit()
