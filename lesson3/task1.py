"""
1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
"""


def div_num(num1, num2):
    try:
        result = round((num1 / num2), 2)
        print(result)
    except ZeroDivisionError:
        print("На ноль делить нельзя.")


div_num(float(input("Введите первое число: ")), float(input("Введите второе число: ")))