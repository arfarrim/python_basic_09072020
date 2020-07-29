"""3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker. В классе Position
реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные, проверить значения
атрибутов, вызвать методы экземпляров).
"""


class Worker:

    def __init__(self, name, surname, position, _income):
        self._income = {}
        self.name = name
        self.surname = surname
        self.position = position
        self._income.update({"wage": float(_income) / 2})
        self._income.update({"bonus": float(_income) / 2})


class Position(Worker):

    def __init__(self, name, surname, position, _income):
        super().__init__(name, surname, position, _income)

    def get_full_name(self):
        print(f"{self.name} {self.surname}")

    def get_full_income(self):
        result = self._income["wage"] + self._income["bonus"]
        print(f"{result}")


vasya = Worker("vasya", "Pupkin", "fixer", 60)
print(vasya._income)
secretary = Position("Boris", "Chernenko", "secretary", 50)
secretary.get_full_name()
secretary.get_full_income()
