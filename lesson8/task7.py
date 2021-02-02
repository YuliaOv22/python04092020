"""
7. Реализовать проект «Операции с комплексными числами».
Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и
умножения комплексных чисел. Проверьте работу проекта,
создав экземпляры класса (комплексные числа) и выполнив сложение и
умножение созданных экземпляров. Проверьте корректность полученного результата.
"""


class ComplexNum:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x} + {self.y}j)"

    def __add__(self, other):
        return f"Сложение: {ComplexNum(self.x + other.x, self.y + other.y)}"

    def __mul__(self, other):
        new_x = self.x * other.x - self.y * other.y
        new_y = self.y * other.x + self.x * other.y
        return f"Умножение: {ComplexNum(new_x, new_y)}"


num_1 = ComplexNum(1, 2)
num_2 = ComplexNum(3, 2)
print(num_1)
print(num_2)
print(num_1 + num_2)
print(num_1 * num_2)
