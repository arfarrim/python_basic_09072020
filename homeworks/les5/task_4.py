"""4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно
данные. При этом английские числительные должны заменяться на русские. Новый блок
строк должен записываться в новый текстовый файл.
"""
import os
dir_path = os.path.dirname(__file__)
file_1_path = os.path.join(dir_path, "task_4_1")
file_2_path = os.path.join(dir_path, "task_4_2")
dict_numerals = {"one": "один", "two": "два", "three": "три", "four": "четыре"}
mod_list = []
with open(file_1_path, "r", encoding="UTF-8") as file:
    for line in file:
        mod_line = line.lower()
        for key, val in dict_numerals.items():
            if mod_line.find(key) != -1:
                mod_list.append(mod_line.replace(key, val))
with open(file_2_path, "w", encoding="UTF-8") as file:
    for itm in mod_list:
        file.write(itm)
