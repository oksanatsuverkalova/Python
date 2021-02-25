# 1. Реализовать класс Matrix (матрица).
# Обеспечить перегрузку конструктора класса (метод __init__()), который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц вы найдете в методичке.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц).
# Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой
# строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.

class Matrix:
     def __init__(self, input_data):
         self.input = input_data

     def __str__(self):
         return '\n'.join([' '.join(map(str, line)) for line in self.input])

     def __add__(self, other):
         answer = ''
         if len(self.input) == len(other.input):
             for line_1, line_2 in zip(self.input, other.input):
                 if len(line_1) != len(line_2):
                     return 'Problems with shape'

                 summed_line = [x + y for x, y in zip(line_1, line_2)]
                 answer += ' '.join(map(str, summed_line)) + '\n'
         else:
             return 'Problems with shape'
         return answer


matrix_1 = Matrix([[56, 2], [345, 5], [22, 6], [80, 43]])
matrix_2 = Matrix([[2, 1], [213, 90], [31, 8], [10, 11]])
print(matrix_1)
print()
print(matrix_2)
print()
print(matrix_1 + matrix_2)