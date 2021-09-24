"""
1. Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько вариантов кода для одной и той же задачи.
Результаты анализа вставьте в виде комментариев к коду.
Также укажите в комментариях версию Python и разрядность вашей ОС.

Здесь реализован алгоритм сортировки пузырьком.
"""
import random


# @profile
# def myfunc(list_numbers):
#     n = len(list_numbers)
#     for i in range(0, n-1):
#         for j in range(0, n-1-i):
#             if list_numbers[j+1] < list_numbers[j]:
#                 list_numbers[j], list_numbers[j+1] = list_numbers[j+1], list_numbers[j]
#     return list_numbers


# """
# Алгоритм быстрой сортировки методом Хоара.
# """
#
# @profile
# def sort_hoara(list_numbers):
#     if len(list_numbers) > 1:
#         x = list_numbers[random.randint(0, len(list_numbers) - 1)]
#         low = [u for u in list_numbers if u < x]
#         eq = [u for u in list_numbers if u == x]
#         hi = [u for u in list_numbers if u > x]
#         list_numbers = sort_hoara(low) + eq + sort_hoara(hi)
#
#     return list_numbers
#

# """
# Сортировка встроенной функцией sort
# """
#
@profile
def sort_sort(list_numbers):
    list_numbers.sort()
    return list_numbers


def main():
    random.seed(10)
    numbers = []
    for _ in range(1000):
        numbers.append(random.randint(0, 10000))
    return numbers


# print(f'Сортировка пузырьком: Минимальные числа {myfunc(main())[0:2]}, в массиве: \n{myfunc(main())}')

"""
По какой-то причине сортировка пузырьком съела меньше памяти чем в методе сортировки хоара

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    13   19.812 MiB   19.805 MiB           2   @profile
    14                                         def myfunc(list_numbers):
    15   19.812 MiB    0.008 MiB           2       n = len(list_numbers)
    16   19.840 MiB    0.000 MiB        2000       for i in range(0, n-1):
    17   19.840 MiB    0.008 MiB     1000998           for j in range(0, n-1-i):
    18   19.840 MiB    0.000 MiB      999000               if list_numbers[j+1] < list_numbers[j]:
    19   19.840 MiB    0.020 MiB      507708                   list_numbers[j], list_numbers[j+1] = list_numbers[j+1], list_numbers[j]
    20   19.840 MiB    0.000 MiB           2       return list_numbers

"""

# print(f'Сортировка методом Хоара: Минимальные числа {sort_hoara(main())[0:2]}, в массиве: \n{sort_hoara(main())}')

"""
Тут памяти по неведомой причине использовано больше чем в сортировке пузырьком, но меньше действий Occurences
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    27   20.094 MiB   20.020 MiB        2618   @profile
    28                                         def sort_hoara(list_numbers):
    29   20.094 MiB    0.008 MiB        2618       if len(list_numbers) > 1:
    30   20.094 MiB    0.004 MiB        1308           x = list_numbers[random.randint(0, len(list_numbers) - 1)]
    31   20.094 MiB    0.004 MiB       27776           low = [u for u in list_numbers if u < x]
    32   20.094 MiB    0.000 MiB       27776           eq = [u for u in list_numbers if u == x]
    33   20.094 MiB    0.059 MiB       27776           hi = [u for u in list_numbers if u > x]
    34   20.094 MiB    0.000 MiB        1308           list_numbers = sort_hoara(low) + eq + sort_hoara(hi)
    35
    36   20.094 MiB    0.000 MiB        2618       return list_numbers

"""


print(f'Сортировка функцией sort: Минимальные числа {sort_sort(main())[0:2]}, в массиве: \n{sort_sort(main())}')

"""
Здесь наиболее эффективное использование памяти.

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    43   19.840 MiB   19.832 MiB           2   @profile
    44                                         def sort_sort(list_numbers):
    45   19.840 MiB    0.008 MiB           2       list_numbers.sort()
    46   19.840 MiB    0.000 MiB           2       return list_numbers

"""
