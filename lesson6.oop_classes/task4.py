"""
4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
speed, color, name, is_police (булево). А также методы: go, stop, turn(direction),
которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат. Выполните вызов методов и также покажите результат.
"""


class Car:

    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        if self.speed > 0:
            print("Автомобиль движется!")

    def stop(self):
        if self.speed == 0:
            print("Автомобиль стоит на месте!")

    def turn(self, direction):
        if direction < 0 and self.speed > 0:
            print("Автомобиль повернул налево.")
        elif direction > 0 and self.speed > 0:
            print("Автомобиль повернул направо.")

    def show_speed(self):
        if self.speed == 0:
            return
        else:
            print(f"Текущая скорость движения автомобиля: {self.speed} км/ч.")

    def car_name(self):
        print(f"Марка автомобиля: {self.name}. Цвет: {self.color}.")


class TownCar(Car):

    def show_speed(self):
        if self.speed > 60:
            print(f"\033[31mСкорость движения автомобиля превышена!\033[0m Текущая скорость: "
                  f"{self.speed} км/ч.")
        elif self.speed == 0:
            return
        else:
            print(f"Текущая скорость движения автомобиля: {self.speed} км/ч.")


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f"\033[31mСкорость движения автомобиля превышена!\033[0m Текущая скорость: "
                  f"{self.speed} км/ч.")
        elif self.speed == 0:
            return
        else:
            print(f"Текущая скорость движения автомобиля: {self.speed} км/ч.")


class PoliceCar(Car):
    
    def __init__(self, speed, color, name, is_police=True):
        super().__init__(speed, color, name, is_police)
        print(f"* Полицейский автомобиль *")


town_car = TownCar(70, 'Зеленый', 'KIA', False)
town_car.car_name()
town_car.go()
town_car.stop()
town_car.turn(1)
town_car.show_speed()
print()

work_car = WorkCar(45, 'Бежевый', 'BMW', False)
work_car.car_name()
work_car.go()
work_car.stop()
work_car.turn(-1)
work_car.show_speed()
print()

sport_car = SportCar(0, 'Красный', 'Porsche', False)
sport_car.car_name()
sport_car.go()
sport_car.stop()
sport_car.turn(0)
sport_car.show_speed()
print()

police_car = PoliceCar(60, 'Сине-черный', 'Volvo', True)
police_car.car_name()
police_car.go()
police_car.stop()
police_car.turn(1)
police_car.show_speed()
print()
