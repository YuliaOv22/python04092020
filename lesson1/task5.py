"""
5. Запросите у пользователя значения выручки и издержек фирмы.
Определите, с каким финансовым результатом работает фирма
(прибыль — выручка больше издержек, или убыток — издержки больше выручки).
Выведите соответствующее сообщение. Если фирма отработала с прибылью,
вычислите рентабельность выручки (соотношение прибыли к выручке).
Далее запросите численность сотрудников фирмы и
определите прибыль фирмы в расчете на одного сотрудника.
"""


income = float(input("Введите выручку Вашей компании: "))
costs = float(input("Введите издержки Вашей компании: "))
profit = income - costs
if profit > 0:
    rent = profit / income * 100
    print(f"Ваша компания заработала прибыль: {profit:.2f} руб.")
    print(f"Рентабельность составляет: {rent:.0f}%")
    employees = int(input("Введите количество сотрудников в компании: "))
    emplo_profit = profit / employees
    print(f"Прибыль компании в расчете на одного сотрудника составляет: {emplo_profit:.2f} руб.")
elif profit < 0:
    print(f"Ваша компания получила убыток: {profit:.2f} руб.")
else:
    print("Ваша компания ничего не заработала, но и не получила убыток.")

