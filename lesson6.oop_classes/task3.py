"""
3. Реализовать базовый класс Worker (работник), в котором определить атрибуты:
name, surname, position (должность), income (доход).
Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker.
В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и
дохода с учетом премии (get_total_income). Проверить работу примера на реальных данных
(создать экземпляры класса Position, передать данные, проверить значения атрибутов,
вызвать методы экземпляров).
"""


class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):

    def get_full_name(self):
        return f"{self.name} {self.surname}"

    def get_total_income(self):
        return sum(self._income.values())


first = Position("Иван", "Иванович", "Аналитик", 40000, 5000)
print(first.get_full_name(), first.get_total_income(), first.position)
second = Position("Петр", "Сидоров", "Менеджер", 35000, 5000)
print(second.get_full_name(), second.get_total_income(), second.position)
third = Position("Елена", "Петрова", "Бухгалтер", 50000, 5000)
print(third.get_full_name(), third.get_total_income(), third.position)
