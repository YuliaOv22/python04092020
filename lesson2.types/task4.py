"""
4. Пользователь вводит строку из нескольких слов, разделённых пробелами.
Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
Если в слово длинное, выводить только первые 10 букв в слове.
"""


user_list = list(input("Введите несколько слов через пробел: ").split())
for i, j in enumerate(user_list, 1):
    print(f"{str(i):}. {str(j):.10}")