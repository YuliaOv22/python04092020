"""
2. Представлен список чисел. Необходимо вывести элементы исходного списка,
значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка.
Для формирования списка использовать генератор.
Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
Результат: [12, 44, 4, 10, 78, 123].
"""


from random import shuffle


def my_func():
    my_list = [el for el in range(0, 16)]
    shuffle(my_list)
    print(f"{'Исходный список:':23} {str(my_list):}")
    new_list = []
    for i in range(1, len(my_list)):
        if my_list[i - 1] < my_list[i]:
            new_list.append(my_list[i])
        else:
            continue
    print("Отфильтрованный список:", new_list)


my_func()