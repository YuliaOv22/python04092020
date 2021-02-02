"""
3. Создайте собственный класс-исключение,
который должен проверять содержимое списка на наличие только чисел.
Проверить работу исключения на реальном примере.

Необходимо запрашивать у пользователя данные и заполнять список.
Класс-исключение должен контролировать типы данных элементов списка.

Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно,
пока пользователь сам не остановит работу скрипта, введя, например, команду “stop”.
При этом скрипт завершается, сформированный список выводится на экран.

Подсказка: для данного задания примем, что пользователь может вводить только числа и строки.
При вводе пользователем очередного элемента необходимо реализовать проверку типа элемента и
вносить его в список, только если введено число.
Класс-исключение должен не позволить пользователю ввести текст (не число) и
отобразить соответствующее сообщение. При этом работа скрипта не должна завершаться.
"""


class NumberInputError(Exception):
    def __init__(self, txt):
        self.txt = txt


def my_func():
    print('Для завершения ввода напишите "stop".')
    new_list = []
    while True:
        user_input = input("Введите целое число: ")
        if user_input == "stop":
            print(new_list)
            quit()
        try:
            if user_input.isdigit():
                new_list.append(int(user_input))
            else:
                raise NumberInputError("Вы ввели не целое число. Попробуйте еще раз.")
        except NumberInputError as err:
            print(err)


my_func()