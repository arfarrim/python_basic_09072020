"""6. Реализовать два небольших скрипта:
б) итератор, повторяющий элементы некоторого списка, определенного заранее.
"""
from itertools import cycle
from sys import argv
_, user_list = argv # запрос списка
user_list = list(user_list)
ind = 0
iter_count = len(user_list)
for itm in cycle(user_list):  # троекратный вывод введенного списка
    if ind < iter_count * 3:
        print(itm)
        ind += 1
    else:
        break