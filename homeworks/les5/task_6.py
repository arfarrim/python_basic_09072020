"""6. Необходимо создать (не программно) текстовый файл, где каждая строка
описывает учебный предмет и наличие лекционных, практических и лабораторных занятий
по этому предмету и их количество. Важно, чтобы для каждого предмета не обязательно
были все типы занятий. Сформировать словарь, содержащий название предмета и общее
количество занятий по нему. Вывести словарь на экран.
Примеры строк файла:
Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —

Пример словаря:
{“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""

import os
file_path = os.path.join(os.path.dirname(__file__), "task_6")

dump_dict = {}
with open(file_path, "r", encoding="UTF-8") as file:
    for line in file:
        dump_list = line.split(" ")
        out_dict_key = dump_list[0].replace(":", "")
        dump_dict[out_dict_key] = dump_list[1:]

out_dict = {}
for key, itm in dump_dict.items():
    out_dict[key] = sum([int(val.split("(")[0]) for val in itm if val.split("(")[0].isdigit()])
print(out_dict)
