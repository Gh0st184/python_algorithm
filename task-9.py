# Найти максимальный элемент среди минимальных элементов столбцов матрицы.

import random


def myfunc(matrix):
    min_list = []
    for j in range(len(matrix[0])):
        e = matrix[j][j]
        for i in matrix:
            if int(i[j]) < int(e):
                e = i[j]
        min_list.append(e)
    max_number = min_list[0]
    for k in min_list:
        if int(k) < int(max_number):
            max_number = k
    return max_number, min_list


random.seed(100)
a = []
n = 6
m = 6
for i in range(n):
    b = []
    for j in range(m):
        b.append(random.randint(1, 100))
    a.append(b)

for j in a:
    print(j)

print(f'Максимальное элемент {myfunc(a)[0]} среди минимальных элементов столбцов {myfunc(a)[1]}  ')
