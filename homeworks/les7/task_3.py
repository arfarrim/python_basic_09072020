"""3. Реализовать программу работы с органическими клетками. Необходимо создать класс Клетка. В его конструкторе
инициализировать параметр, соответствующий количеству клеток (целое число). В классе должны быть реализованы методы
перегрузки арифметических операторов: сложение (__add__()), вычитание (__sub__()), умножение (__mul__()),
деление (__truediv__()).Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение,
умножение и обычное (не целочисленное) деление клеток, соответственно. В методе деления должно осуществляться
округление значения до целого числа.
Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.
Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность количества ячеек двух клеток больше
 нуля, иначе выводить соответствующее сообщение.
Умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется как произведение количества ячеек этих
 двух клеток.
Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется как целочисленное деление количества
ячеек этих двух клеток.
В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду.
Данный метод позволяет организовать ячейки по рядам.
Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному аргументу.
Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5. Тогда метод make_order() вернет
строку: *****\n*****\n**.
Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5. Тогда метод make_order() вернет
строку: *****\n*****\n*****.
"""
from math import fabs


class Cell:

    def __init__(self, num: int):
        self.cells = int(num)

    def __str__(self) -> str:
        return self.cells * "*"

    def make_order(self, rows: int):
        if self.cells <= rows:
            print("*" * self.cells)
        if self.cells > rows:
            for itm in range(0, self.cells // rows):
                print("*" * rows)
        if self.cells % rows != 0:
            print("*" * (self.cells % rows))

    def __add__(self, other):
        return Cell(self.cells + other.cells)

    def __sub__(self, other):
        if self.cells != other.cells:
            return Cell(fabs(self.cells - other.cells))
        else:
            print("клетки аннигилировали")

    def __mul__(self, other):
        return Cell(self.cells * other.cells)

    def __truediv__(self, other):
        return Cell(float(self.cells) // float(other.cells))


cancer = Cell(3)
tissue_sampl = Cell(5)
print(f"{cancer - tissue_sampl} sub 3 5")
print(f"{cancer + tissue_sampl} add 3 5")
print(f"{cancer * tissue_sampl} mul 3 5")
print(f"{tissue_sampl / cancer} div 5 3")
cancer = Cell(11)
cancer.make_order(5)
cancer.make_order(2)
cancer.make_order(3)
cancer.make_order(15)
