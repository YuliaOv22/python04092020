"""
1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату
в виде строки формата «день-месяц-год». В рамках класса реализовать два метода.
Первый, с декоратором @classmethod, должен извлекать число, месяц,
год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod,
должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных.
"""


class Date:

    def __init__(self, date):
        self.date = date

    @classmethod
    def format_date(cls, date):
        d_m_y = [int(i) for i in date.split("-")]
        day = d_m_y[0]
        month = d_m_y[1]
        year = d_m_y[2]
        lst = [day, month, year]
        return lst

    @staticmethod
    def check(lst):
        if lst[0] < 1 or lst[0] > 31:
            print("Некорректно введено число.")
        elif lst[1] < 1 or lst[1] > 12:
            print("Некорректно введен месяц.")
        elif lst[2] > 2020 or len(str(lst[2])) < 4 or lst[2] < 1700:
            print("Некорректно введен год.")
        else:
            print(f"{lst[0]:02}-{lst[1]:02}-{lst[2]}")


date = input("Введите дату в формате «день-месяц-год»: ")
Date.check(Date.format_date(date))
obj_2 = Date(date)
Date.check(obj_2.format_date(date))
