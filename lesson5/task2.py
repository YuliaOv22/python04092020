"""
2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""


with open("text_2.txt", "w+", encoding="utf-8") as text_2:
    print("Для окончания записи, нажмите 'Enter' с пустой строкой.")
    while True:
        user_str = input("Введите данные: ")
        if user_str == "":
            break
        text_2.write(f"{user_str}\n")
    text_2.seek(0)
    content = text_2.readlines()
    i = 0
    el = 0
    count_str = []
    count_words = []
    for i in range(len(content)):
        count_str.append(content[i].split())
        for el in range(len(count_str[i])):
            el += 1
        count_words.append(el)
        i += 1
    print(f"\nКоличество строк в файле text_2.txt: {i}.")
    for a in range(len(count_words)):
        print(f"Количество слов в строке {a+1}: {count_words[a]}.")