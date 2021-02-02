"""
4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
Для решения используйте цикл while и арифметические операции.
"""


user_num = int(input("Введите целое положительное число: "))
max_num = user_num % 10
user_num = user_num // 10
while user_num > 0:
    if user_num % 10 > max_num:
        max_num = user_num % 10
    user_num = user_num // 10
print(max_num)
