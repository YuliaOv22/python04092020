"""
2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
Значения данных атрибутов должны передаваться при создании экземпляра класса.
Атрибуты сделать защищенными. Определить метод расчета массы асфальта,
необходимого для покрытия всего дорожного полотна.
Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом,
толщиной в 1 см * число см толщины полотна. Проверить работу метода.
Например: 20м * 5000м * 25кг * 5см = 12500 т
"""


class Road:

    def __init__(self, length, width, mass=25, thick=5):
        self._length = length
        self._width = width
        self._mass = mass
        self._thick = thick

    def asphalt(self):
        result = (self._length * self._width * self._mass * self._thick) / 1000
        return print(f"{self._length} м * {self._width} м * {self._mass} кг * {self._thick} см = {result} т")


a = Road(20, 5000)
a.asphalt()
b = Road(50, 1000)
b.asphalt()
c = Road(2, 542)
c.asphalt()
