"""
7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
название, форма собственности, выручка, издержки. Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
а также словарь со средней прибылью. Если фирма получила убытки,
также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта: [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
Подсказка: использовать менеджеры контекста.
"""


import json

companies_profit = {}
average_profit = {}
comp_profit = []
with open("text_7.txt", "r", encoding="utf-8") as text_7:
    for line in text_7:
        companies = [line.split()[0]]
        profit = int(line.split()[2]) - int(line.split()[3])
        if profit >= 0:
            comp_profit.append(profit)
        companies_profit[companies[0]] = profit
average_profit['Средняя прибыль компаний'] = round(sum(int(i) for i in comp_profit) / len(comp_profit))
result = [companies_profit, average_profit]
print(result)
with open("text_7_new.json", "w", encoding="utf-8") as new_f7:
    json.dump(result, new_f7, ensure_ascii=False)
