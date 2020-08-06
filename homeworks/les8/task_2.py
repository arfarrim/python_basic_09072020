"""
2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных,
вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту
ситуацию и не завершиться с ошибкой.
"""


class ZeroDivError(Exception):

    def __init__(self, mes):
        self.mes = mes


while True:
    user_input = input("введите делимое и делитель через пробел")
    try:
        divident = float(user_input.split()[0])
        divider = float(user_input.split()[1])
        if not divider:
            raise ZeroDivError("делитель не должен быть равен нулю")
        print(divident / divider)
    except ZeroDivisionError:
        print("деление на ноль")
    except ZeroDivError as err:
        print(err)
