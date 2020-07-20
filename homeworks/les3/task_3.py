"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента, и
возвращает сумму наибольших двух аргументов.
"""


def my_func(arg_1, arg_2, arg_3):
    """Возвращает сумму двух наибольших чисел.

    Именованные параметры:
    :arg_1 -- первое число
    :arg_2 -- второе число
    :arg_3 -- третье число

    """

    try:
        float(arg_1), float(arg_2), float(arg_3)  # проверка параметров
    except:
        return -1  # неверные входные аргументы, возврат -1
    arg_1, arg_2, arg_3 = float(arg_1), float(arg_2), float(arg_3)
    if arg_1 == arg_2 or arg_2 == arg_3:  # проверка наличия равных чисел
        return arg_1 + arg_3
    if arg_1 > arg_2:  # поиск двух максимальных чисел из входных значений
        if arg_2 > arg_3:
            return arg_1 + arg_2
        else:
            return arg_1 + arg_3
    else:
        if arg_1 > arg_3:
            return arg_2 + arg_1
        else:
            return arg_2 + arg_3


num_1 = input("введите число 1")
num_2 = input("введите число 2")
num_3 = input("введите число 3")
print(my_func(num_1, num_2, num_3))
