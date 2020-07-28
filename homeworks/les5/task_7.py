"""7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название, форма
собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки,в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
 Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджеры контекста.
"""
import os
import json
file_path = os.path.join(os.path.dirname(__file__), "task_7")
file_path_2 = os.path.join(os.path.dirname(__file__), "task_7json")
dict_profit = {}
with open(file_path, "r", encoding="UTF-8") as file:
    for line in file:
        dump_list = line.split(" ")
        profit = int(dump_list[2]) - int(dump_list[3])
        dict_profit.update({dump_list[0]: profit})
dict_aver_profit = {}
sum_prof = 0
i = 0
for val in dict_profit.values():
    if val >= 0:
        sum_prof += val
        i += 1
else:
    dict_aver_profit["средняя прибыль"] = sum_prof / i
#print(dict_profit)
out_list = [{key: val} for key, val in dict_profit.items()]
out_list = out_list + [dict_aver_profit]
#print(out_list)
with open(file_path_2, "w", encoding="UTF-8") as file:
    file.write(json.dumps(out_list, ensure_ascii=False))
