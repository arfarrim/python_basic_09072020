"""3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников
и величину их окладов. Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода
сотрудников.
"""
import os
file_path = os.path.join(os.path.dirname(__file__), "task_3")
with open(file_path, "r", encoding="UTF-8") as file:
    mod_dict = {}
    for line in file:
        if line[len(line)-1] == "\n":
            line = line[:len(line) - 1]
        mod_line = line.split(" ")
        mod_dict.update({mod_line[0]: int(mod_line[1])})
for key, val in mod_dict.items():
    print(f"{key} имеет оклад {val}")
    if val < 20000:
        print(f"{key} получает меньше 20 тысяч")
aver_sal = sum(mod_dict.values()) / len(mod_dict)
print("Средняя зарплата сотрудников = " + "%.2f" % aver_sal)
print(mod_dict)
