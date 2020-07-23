"""6. Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного
"""
from itertools import count
from sys import argv
_, count_start = argv  # запрос стартового числа
count_start = int(count_start)
for itm in count(count_start):  # генерация чисел от стартового 7 позиций с шагом 1
    if itm <= (count_start + 7):
        print(itm)
    else:
        break
