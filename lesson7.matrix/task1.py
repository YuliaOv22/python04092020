"""
1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц вы найдете в методичке.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix
(двух матриц). Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно —
первый элемент первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.
"""


class Matrix:

    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return "Матрица --v \n" + '\n'.join('  '.join(str(el) for el in row) for row in self.matrix) + "\n"

    def __add__(self, other):

        matrix_new = []
        if len(other.matrix) > len(self.matrix):
            self.matrix, other.matrix = other.matrix, self.matrix
        for i in range(len(self.matrix)):
            matrix_new.append([])
            for j in range(len(other.matrix[0])):
                try:
                    matrix_new[i].append(self.matrix[i][j] + other.matrix[i][j])
                except IndexError:
                    matrix_new[i].append(self.matrix[i][j] + 0)
        return f"Новая {Matrix(matrix_new)}"


matrix_1 = Matrix([[-10, 2], [3, 4], [5, 0]])
matrix_2 = Matrix([[7, 8], [-9, 10], [11, 12], [11, 12]])
print(matrix_1)
print(matrix_2)
print(matrix_1 + matrix_2)
