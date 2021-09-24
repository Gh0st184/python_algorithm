""" Проанализировать скорость и сложность одного любого алгоритма,
разработанных в рамках домашнего задания первых трех уроков.
Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.

7 задание из 3 урока: В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба являться минимальными), так и различаться.

Здесь реализован алгоритм сортировки пузырьком, предпологаю что это сложность O(n^2),
т.к. получаем цикл в цикле и для каждого элемента проходим еще раз по всему списку.
Самое большое время выполнения
"""

import random
import cProfile


def myfunc(list_numbers):
    n = len(list_numbers)
    for i in range(0, n-1):
        for j in range(0, n-1-i):
            if list_numbers[j+1] < list_numbers[j]:
                list_numbers[j], list_numbers[j+1] = list_numbers[j+1], list_numbers[j]
    return list_numbers


"""
Алгоритм быстрой сортировки методом Хоара, сложность данного алгоритма O(n log n)
Время выполнения меньше чем у O(n^2)
"""


def sort_hoara(list_numbers):
    if len(list_numbers) > 1:
        x = list_numbers[random.randint(0, len(list_numbers) - 1)]
        low = [u for u in list_numbers if u < x]
        eq = [u for u in list_numbers if u == x]
        hi = [u for u in list_numbers if u > x]
        list_numbers = sort_hoara(low) + eq + sort_hoara(hi)

    return list_numbers


"""
Сортировка встроенной функцией sort, в статье про данную сортировку прочитал что худший случай для данного метода будет
O(n log n), в среднем она отрабатывает быстрее
"""


def sort_sort(list_numbers):
    list_numbers.sort()
    return list_numbers


def main():
    random.seed(10)
    numbers = []
    for _ in range(1000):
        numbers.append(random.randint(0, 10000))

    # print(f'Сортировка пузырьком: Минимальные числа {myfunc(numbers)[0:2]}, в массиве: \n{myfunc(numbers)}')
    """
    Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.060    0.060 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 random.py:126(seed)
     1000    0.000    0.000    0.000    0.000 random.py:237(_randbelow_with_getrandbits)
     1000    0.000    0.000    0.001    0.000 random.py:290(randrange)
     1000    0.000    0.000    0.001    0.000 random.py:334(randint)
        2    0.056    0.028    0.056    0.028 task-1.py:16(myfunc)
        1    0.000    0.000    0.060    0.060 task-1.py:41(main)
        1    0.000    0.000    0.060    0.060 {built-in method builtins.exec}
        2    0.000    0.000    0.000    0.000 {built-in method builtins.isinstance}
        2    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        1    0.003    0.003    0.003    0.003 {built-in method builtins.print}
        1    0.000    0.000    0.000    0.000 {function Random.seed at 0x0000020F4418CF70}
     1000    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
     1000    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
     1608    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
    """

    # print(f'Сортировка методом Хоара: Минимальные числа {sort_hoara(numbers)[0:2]}, в массиве: \n{sort_hoara(numbers)}')

    """
     Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.016    0.016 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 random.py:126(seed)
     2290    0.001    0.000    0.001    0.000 random.py:237(_randbelow_with_getrandbits)
     2290    0.001    0.000    0.002    0.000 random.py:290(randrange)
     2290    0.001    0.000    0.002    0.000 random.py:334(randint)
   2582/2    0.002    0.000    0.006    0.003 task-1.py:30(sort_hoara)
     1290    0.001    0.000    0.001    0.000 task-1.py:33(<listcomp>)
     1290    0.000    0.000    0.000    0.000 task-1.py:34(<listcomp>)
     1290    0.001    0.000    0.001    0.000 task-1.py:35(<listcomp>)
        1    0.000    0.000    0.016    0.016 task-1.py:41(main)
        1    0.000    0.000    0.016    0.016 {built-in method builtins.exec}
        2    0.000    0.000    0.000    0.000 {built-in method builtins.isinstance}
     3872    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        1    0.009    0.009    0.009    0.009 {built-in method builtins.print}
        1    0.000    0.000    0.000    0.000 {function Random.seed at 0x000001C1004DCF70}
     1000    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
     2290    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
     3824    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
    """

    print(f'Сортировка функцией sort: Минимальные числа {sort_sort(numbers)[0:2]}, в массиве: \n{sort_sort(numbers)}')

    """
    Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.006    0.006 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 random.py:126(seed)
     1000    0.000    0.000    0.000    0.000 random.py:237(_randbelow_with_getrandbits)
     1000    0.000    0.000    0.001    0.000 random.py:290(randrange)
     1000    0.000    0.000    0.001    0.000 random.py:334(randint)
        2    0.000    0.000    0.000    0.000 task-1.py:46(sort_sort)
        1    0.000    0.000    0.006    0.006 task-1.py:51(main)
        1    0.000    0.000    0.006    0.006 {built-in method builtins.exec}
        2    0.000    0.000    0.000    0.000 {built-in method builtins.isinstance}
        1    0.004    0.004    0.004    0.004 {built-in method builtins.print}
        1    0.000    0.000    0.000    0.000 {function Random.seed at 0x0000018153F0E040}
     1000    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
     1000    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
     1608    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
        2    0.000    0.000    0.000    0.000 {method 'sort' of 'list' objects}
    """


if __name__ == '__main__':
    cProfile.run('main()')
