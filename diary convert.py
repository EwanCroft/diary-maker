import json
import os
import codecs
import datetime
import time

user = os.getlogin()
Diary_root_folder = rf"C:\Users\{user}\Documents\Diary"
export = input("Do you have a DayOne export? (y/n):\n")
if export == "y":
    JSON_data = input("Enter where the DayOne export is located (JSON *.zip file):\n")
    user_entry_count = int(input(f"How many entries are there in {JSON_data}?:\n"))
    with codecs.open(f"{JSON_data}", "r", encoding = "UTF-8") as f:
        data = json.load(f)

        count_2 = 1
        for count in range(user_entry_count):
            creation_date = data["entries"][count]["creationDate"]
            date = datetime.datetime.strptime(creation_date, '%Y-%m-%dT%H:%M:%SZ').date()
            time_orig = datetime.datetime.strptime(creation_date, '%Y-%m-%dT%H:%M:%SZ').time()
            time = time_orig.strftime("%H%M%S")
            text = data["entries"][count]["text"].replace("#### ", "").replace("#", "").replace("\\", "")

            if not os.path.exists(f"{Diary_root_folder}\\{date}\\"):
                try:
                    os.makedirs(f"{Diary_root_folder}\\{date}\\")
                except Exception as e:
                    print(e)

            file_name = f"{Diary_root_folder}\\{date}\\{time}.txt"
            with open(file_name, "w", encoding = "UTF-8") as f:
                try:
                    f.write(text)
                except Exception as e:
                    print(e)

            count_2 += 1
        print("Entry saved.")

elif export == "n":
    print("Why are you using this script? go use diary writer.py already")
    time.sleep(3)
    quit()

if not os.path.exists(Diary_root_folder):
    os.makedirs(Diary_root_folder)
else:
    pass