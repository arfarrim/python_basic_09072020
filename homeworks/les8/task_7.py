"""7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте перегрузку
методов сложения и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры к
и выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.
"""


class ComplexNum:

    def __init__(self, re, im):
        self.re = float(re)
        self.im = float(im)

    def __add__(self, other):
        re_tmp = self.re + other.re
        im_tmp = self.im + other.im
        return ComplexNum(re_tmp, im_tmp)

    def __mul__(self, other):   # (a+bi)(c+di)=ac+adi+bci-bd=(ac-bd)+(ad+bc)i
        re_tmp = self.re * other.re - self.im * other.im
        im_tmp = self.re * other.im + self.im * other.re
        return ComplexNum(re_tmp, im_tmp)

    def __str__(self):
        if self.im >= 0:
            return f"{self.re} +{self.im}*i"
        else:
            return f"{self.re} {self.im}*i"


numy = ComplexNum(10, -5)
numy2 = ComplexNum(10, 5)
numy3 = numy + numy2
numy4 = numy * numy2
print(numy, numy2)
print(numy3, numy4)
