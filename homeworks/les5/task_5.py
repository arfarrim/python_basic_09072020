"""5. Создать (программно) текстовый файл, записать в него программно набор чисел,
разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить
ее на экран.
"""
import os
dir_path = os.path.dirname(__file__)
file_1_path = os.path.join(dir_path, "task_5")
with open(file_1_path, "w", encoding="UTF-8") as file:
    user_input = input("введите числа через пробел")
    file.write(user_input)
with open(file_1_path, "r", encoding="UTF-8") as file:
    dump_line = file.readline()
mod_dump = dump_line.split(" ")
dump = []
for elm in mod_dump:
    dump.append(int(elm))
print(mod_dump)
print(sum(dump))
