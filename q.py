#1

python
import os

path = "data"
files = os.listdir(path)

print(f"Количество файлов в папке {path}: {len(files)}")


#2
python
import os

path = "data"
files = os.listdir(path)

count = 0
for file in files:
    if any(char.isdigit() for char in file):
        count += 1

print(f"Количество файлов в папке {path}, в названии которых есть цифра: {count}")


#3

import os

folder_path = "data"
file_count = 0
g_count = 0

for filename in os.listdir(folder_path):
    if os.path.isfile(os.path.join(folder_path, filename)):
        file_count += 1
        if "g" in filename:
            g_count += 1

print(f"В папке {folder_path} находится {file_count} файлов, из них {g_count} файлов содержат букву 'g' в имени.")




#4

import os

folder_path = "data"

count = 0

for filename in os.listdir(folder_path):
    if os.path.isfile(os.path.join(folder_path, filename)):
        if "gg" in filename:
            count += 1

print(f"Количество файлов с двумя буквами g подряд в папке {folder_path}: {count}")







