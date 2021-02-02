"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и
величину их окладов. Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
"""


with open("text_3.txt", "r", encoding="utf-8") as text_3:
    content = text_3.readlines()
    salary_range = 20000
    i = 0
    el = 0
    count_str = []
    list_min_sal = []
    sum_salary = 0
    for i in range(len(content)):
        count_str.append(content[i].split())
        for el in range(len(count_str[i])):
            if el == 1:
                count_str[i][el] = float(count_str[i][el])
                if count_str[i][el] < salary_range:
                    list_min_sal.append(count_str[i][el - 1])
                sum_salary += count_str[i][el]
            el += 1
        i += 1
    amount_salary = round((sum_salary / len(count_str)), 2)
    print("Список сотрудников с окладом менее 20 тыс. руб.:")
    for a in range(len(list_min_sal)):
        print(f"{a + 1}. {list_min_sal[a]}")
    print(f"\nСредняя величина дохода сотрудников: {amount_salary} руб.")
