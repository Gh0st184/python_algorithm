""" Напишите программу, доказывающую или проверяющую,
что для множества натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2, где n - любое натуральное число.
"""


def myfunc(number):
    i = 0
    for j in range(i, (number + 1)):
        i += j
    k = number * (number + 1) / 2
    print(i)
    print(k)
    if i == k:
        return True
    else:
        return False


n = int(input('Введите натуральное число: '))
print(myfunc(n))
