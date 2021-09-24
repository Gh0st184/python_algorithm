"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы.
Сортировка должна быть реализована в виде функции. По возможности доработайте алгоритм (сделайте его умнее).
"""

import random


def my_func(array):
    n = 1
    while n < len(array):
        count = 0
        for i in range(len(array) - 1 - (n - 1)):
            if array[i] < array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                count += 1
        if count == 0:
            break
        n += 1


size = 10
min_item = -100
max_item = 99
array = [random.randint(min_item, max_item) for _ in range(size)]

print(f'Before sort: {array}')
my_func(array)
print(f'After sort: {array}')