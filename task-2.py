"""
 Написать два алгоритма нахождения i-го по счёту простого числа.
Без использования «Решета Эратосфена»;
Используя алгоритм «Решето Эратосфена»
Примечание ко всему домашнему заданию: Проанализировать скорость и сложность алгоритмов.
Результаты анализа сохранить в виде комментариев в файле с кодом.
"""

import cProfile

n = int(input("Ввывод простых чисел до: "))


def eratosphen(n):
    a = [0] * n
    for i in range(n):
        a[i] = i
    a[1] = 0

    m = 2
    while m < n:
        if a[m] != 0:
            j = m * 2
            while j < n:
                a[j] = 0
                j = j + m
        m += 1

    b = []
    for i in a:
        if a[i] != 0:
            b.append(a[i])

    del a
    return b


def not_eratosphen(n):
    a = []
    for i in range(2, n):
        state = True
        for j in range(2, n):
            if j != i and i % j == 0:
                state = False
        if state is True:
            a.append(i)

    return a


def main():
    print(eratosphen(n))
    """
    Вычисление простых чисел до 1000, алгоритм решето Эратосфена. Предполагаю что здесь сложность алгоритма O(n log n),
    высокая скорость работы алгоритма.
    
    Ordered by: standard name

    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 task-2.py:14(eratosphen)
        1    0.000    0.000    0.000    0.000 task-2.py:55(main)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
      168    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}



    Process finished with exit code 0

    """

    # print(not_eratosphen(n))

    """
    Вычисление простых чисел до 1000. Сложность алгоритма O(n^2), т.к. для каждого элемента n мы перебираем все 
    элементы от 2 до n
    
    Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.034    0.034 <string>:1(<module>)
        1    0.034    0.034    0.034    0.034 task-2.py:42(not_eratosphen)
        1    0.000    0.000    0.034    0.034 task-2.py:55(main)
        1    0.000    0.000    0.034    0.034 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
      168    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
    """


if __name__ == '__main__':
    cProfile.run('main()')
