"""
4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
уникальные для каждого типа оргтехники.

5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу в
определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники, а также других
данных, можно использовать любую подходящую структуру, например словарь.

6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных. Например, для
указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
"""


class Warehouse:

    def __init__(self):  # инициируется пустым
        self.items = {}
        self.__num = 1

    def acceptance(self, goods, count: int):
        goods.update({"количество": count, "хранение": "склад"})
        self.items.update({self.__num: goods})
        self.__num += 1

    def transfer(self, name, depart):
        if self.items.get(name):
            dict_update = self.items.get(name)
            dict_update.update({"хранение": depart})
            self.items.update({name: dict_update})


class OfiseAppl:

    def __init__(self, name, type):
        self.name = name
        self.type = type


class Print(OfiseAppl):

    def __init__(self, name, cart_type: str, is_color: bool):
        super().__init__(name, "принтер")
        self.cart_type = cart_type
        self.is_color = is_color

    def data(self):
        return {"название": self.name, "тип": "принтер"}


class Scaner(OfiseAppl):

    def __int__(self, name, is_bulk: bool):
        super().__init__(name, "сканер")
        self.is_bulk = is_bulk


slow_print = Print("hp", "laser", True)
wh1 = Warehouse()
wh1.acceptance(slow_print.data(), 5)
print(wh1.items)
wh1.transfer(1, "офис")
print(wh1.items)
