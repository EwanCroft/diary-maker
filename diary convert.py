import json
import os
import codecs
import datetime

JSON_data = input("Enter where the DayOne export is located:\n")
Diary_root_folder = "C:\\Users\\Ewan\\Documents\\Diary"

if not os.path.exists(Diary_root_folder):
    os.makedirs(Diary_root_folder)
else:
    pass

with codecs.open(f"{JSON_data}", "r", encoding = "UTF-8") as f:
    data = json.load(f)

count_2 = 1
for count in range(424):
    creation_date = data["entries"][count]["creationDate"]
    date = datetime.datetime.strptime(creation_date, '%Y-%m-%dT%H:%M:%SZ').date()
    time_orig = datetime.datetime.strptime(creation_date, '%Y-%m-%dT%H:%M:%SZ').time()
    time = time_orig.strftime("%H%M%S")
    text = data["entries"][count]["text"].replace("#### ", "").replace("#", "").replace("\\", "")

    if not os.path.exists(f"{Diary_root_folder}\\{date}\\"):
        os.makedirs(f"{Diary_root_folder}\\{date}\\")

    file_name = f"{Diary_root_folder}\\{date}\\{time}.txt"
    with open(file_name, "w", encoding = "UTF-8") as f:
        f.write(text)

    count_2 += 1
    print("Entry saved.")
