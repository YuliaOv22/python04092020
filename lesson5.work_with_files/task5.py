"""
5. Создать (программно) текстовый файл, записать в него программно набор чисел,
разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и
выводить ее на экран.
"""


with open("text_5.txt", "w+", encoding="utf-8") as text_5:
    user_str = input("Введите набор чисел через пробел: ")
    text_5.write(user_str)
    text_5.seek(0)
    summary = 0
    for i in text_5.readlines():
        num = i.split()
        for el in range(len(num)):
            try:
                num[el] = int(num[el])
            except ValueError:
                num[el] = 0
            summary += num[el]
    print(f"Сумма чисел в файле text_5.txt: {summary}")
