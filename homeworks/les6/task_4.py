"""4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name,
is_police (булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала,
остановилась, повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в
базовый класс метод show_speed, который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar
переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение
о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат. Выполните
вызов методов и также покажите результат.
"""


class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def show_speed(self):
        print(f"Текущая скорость {self.speed}")

    def go(self):
        print("Движение началось")

    def stop(self):
        print("Машина остановилась")

    def turn(self, direction):
        if direction.lower() == "налево" or direction.lower() == "направо":
            print(f"Машина повернула {direction}")
        else:
            raise ValueError("Система управления не расчитана на подобное")


class TownCar(Car):

    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)

    def show_speed(self):
        print(f"Текущая скорость {self.speed}")
        if int(self.speed) > 60:
            print("Превышен предел скорости 60")


class WorkCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)

    def show_speed(self):
        print(f"Текущая скорость {self.speed}")
        if int(self.speed) > 40:
            print("Превышен предел скорости 40")


class SportCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, True)


red_car = SportCar(120, "red", 'opel')
print(red_car.is_police)
red_car.turn("налево")
red_car.stop()
blue_car = WorkCar(100, "blue", "lada")
green_car = TownCar(55, "green", "mazda")
blue_car.show_speed()
green_car.show_speed()
gibdd_car = PoliceCar(150, "white", "gaz")
print(gibdd_car.is_police)
print(gibdd_car.color)
