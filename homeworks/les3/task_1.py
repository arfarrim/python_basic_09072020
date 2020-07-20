"""
1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую
их деление. Числа запрашивать у пользователя, предусмотреть обработку ситуации
деления на ноль.
"""


def devide_2_num(d_1, d_2) -> float:
    """Возвращает частное от деления.

    Именованные параметры:
    d_1 -- делимое
    d_2 -- делитель

    """
    if float(d_2) == 0:
        return -1
    return (float(d_1) / float(d_2))


while True:
    try:
        dev_1 = float(input('введите делимое'))
    except ValueError:
        continue
    break
while True:
    try:
        dev_2 = float(input('введите делитель'))
    except ValueError:
        continue
    break
print(devide_2_num(dev_1, dev_2))
