"""
4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и
считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""


from googletrans import Translator

translator = Translator()
with open("text_4.txt", "r", encoding="utf-8") as text_4:
    words = []
    for i in text_4.readlines():
        words.append(i.split())
    for el in range(len(words)):
        result = translator.translate(words[el][0], dest='ru')
        words[el][0] = result.text
with open("text_41.txt", "w+", encoding="utf-8") as text_41:
    for a in range(len(words)):
        text_41.write(f"{' '.join(words[a])}\n")
    text_41.seek(0)
    content = text_41.read()
    print(f"{content}")
