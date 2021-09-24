""" В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба являться минимальными), так и различаться."""

import random


def myfunc(list_numbers):
    n = len(list_numbers)
    for i in range(0, n-1):
        for j in range(0, n-1-i):
            if list_numbers[j+1] < list_numbers[j]:
                list_numbers[j], list_numbers[j+1] = list_numbers[j+1], list_numbers[j]
    return list_numbers


random.seed(10)
numbers = []
for _ in range(20):
    numbers.append(random.randint(0, 100))


print(f'Минимальные числа {myfunc(numbers)[0:2]}, в массиве: \n{myfunc(numbers)}')
