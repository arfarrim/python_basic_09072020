"""
4. Программа принимает действительное положительное число x и целое отрицательное
число y. Необходимо выполнить возведение числа x в степень y. Задание необходимо
реализовать в виде функции my_func(x, y). При решении задания необходимо обойтись
без встроенной функции возведения числа в степень.
"""


def invol_neg(base, degree):
    """Возвращает результат вычисления первого аргумента
    в отрицательную степень(второй аргумент).

    Именованные параметры:
    :base -- основание
    :degree -- степень(принимает только отрицательные целые числа)

    """

    try:  # проверка аргументов
        float(base) and int(degree) and int(degree) < 0 and float(base) > 0
    except:  # возврат пустого значения при ошибке аргументов
        return None
    base = float(base)
    degree = float(degree) * -1  # модуль(degree всегда < 0)
    if base == 0:  # ситуация деленяи на 0
        return None
    out_num = 1.0
    i = 0
    while i <= degree:  # цикл возведения base в степень degree
        out_num = out_num * base
        i += 1
    return (1 / out_num)


n = True
while n:  # зацикленный вызов функции invol_neg с запросом значений и выхода
    while True:
        num_1 = input("введите действительное положительное число")
        try:
            float(num_1)
        except:
            continue
        break
    while True:
        num_2 = input("введите целое отрицательное число")
        try:
            int(num_2)
        except:
            continue
        break
    print(invol_neg(num_1, num_2))
    while True:
        user_input = input("Повторить? да/нет")
        if user_input.lower() == "нет":
            n = 0
            break
        if user_input.lower() == "да":
            break
