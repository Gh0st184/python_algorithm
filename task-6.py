""" В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать. """


def myfunc(list_numbers):
    k, j = int(list_numbers[0]), int(list_numbers[0])
    for i in list_numbers:
        if int(i) > j:
            j = int(i)
        if int(i) < k:
            k = int(i)
    sum = 0
    for a, b in enumerate(list_numbers):
        if list_numbers.index(str(j)) > a > list_numbers.index(str(k)):
            sum += int(b)
    return sum


numbers = input('Введите числа через пробел: ').split()
print(f'Сумму чисел {myfunc(numbers)}')
