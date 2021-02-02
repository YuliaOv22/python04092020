"""
1. Создать программно файл в текстовом формате, записать в него построчно данные,
вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.
"""

with open("text_1.txt", "w+", encoding="utf-8") as first_try:
    print("Для окончания записи, нажмите 'Enter' с пустой строкой.")
    while True:
        user_str = input("Введите данные: ")
        if user_str == "":
            break
        first_try.write(f"{user_str}\n")
    print("Ввод данных закончен. Содержимое файла ниже.")
    first_try.seek(0)
    content = first_try.read()
    print(f"\nСодержимое файла text_1.txt: \n{content}")
