"""
2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем.
При вводе пользователем нуля в качестве делителя программа
должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""


class ZeroDivError(Exception):
    def __init__(self, txt):
        self.txt = txt


num_1 = input("Введите делимое число: ")
num_2 = input("Введите делитель: ")

try:
    num_1, num_2 = int(num_1), int(num_2)
    if num_2 == 0:
        raise ZeroDivError("На ноль делить нельзя!")
except ValueError:
    print("Вы ввели не число.")
except ZeroDivError as err:
    print(err)
else:
    print(f"Частное равно: {round(num_1 / num_2, 2)}")
