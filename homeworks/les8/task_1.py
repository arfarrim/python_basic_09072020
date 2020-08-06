"""
1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата
«день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число,
месяц, год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию
числа, месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
"""


class Date:

    def __init__(self, date: str):
        self.date = date

    @classmethod
    def convert(cls, date: str):
        tmp = [int(itm) for itm in date.split("-")]
        return tmp

    @staticmethod
    def valid(date: str):
        tmp = Date.convert(date)
        if tmp[1] > 12 or tmp[1] < 1 or tmp[0] > 31 or tmp[0] < 1 or tmp[2] < 1:  # проверка общих допустимых пределов
            return 0
        if tmp[1] in [4, 6, 9, 11] and tmp[0] > 30:  # проверка верхней границы для 30дневных месяцев
            return 0
        if tmp[1] == 2:  # проверка апреля в зависимости от високосности года
            if not tmp[2] % 4:
                if tmp[0] > 29:
                    return 0
            else:
                if tmp[0] > 28:
                    return 0
        return 1


monday = Date("29-02-2040")
print(Date.convert("12-07-2040"))
print(monday.valid("29-02-2039"))
