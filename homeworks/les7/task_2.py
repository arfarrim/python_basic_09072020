"""2. Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого
проекта — одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа:
V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать
абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
"""
from abc import ABC, abstractmethod


class Clothes(ABC):

    @abstractmethod
    def fabric_cons(self):
        pass


class Coat(Clothes):

    _fabric_count = 0

    def __init__(self, size: float):
        self.__size = size
        Coat._fabric_count = Coat._fabric_count + size / 6.5 + 0.5

    @property
    def fabric_count(self):
        return Coat._fabric_count

    def fabric_cons(self):
        return self.__size / 6.5 + 0.5


class Suit(Clothes):

    _fabric_count = 0

    def __init__(self, height: float):
        Suit._fabric_count = Suit._fabric_count + height * 2 + 0.3
        self.height = height

    @property
    def fabric_count(self):
        return Suit._fabric_count

    def fabric_cons(self):
        return self.height * 2 + 0.3


new_suit = Suit(10)
black_suit = Suit(5)
red = Coat(7)
new_coat = Coat(12)
print(f"{red.fabric_cons()} расход ткани на конкретное пальто")
print(f"{red.fabric_count} сумма ткани на пальто")
print(f"{new_suit.fabric_count} сумма ткани на костюмы")
print(f"{red.fabric_count + new_suit.fabric_count} суммарны расход ткани")
