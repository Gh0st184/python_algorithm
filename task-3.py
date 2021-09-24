# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.


def myfunc(list_numbers):
    k, j = int(list_numbers[0]), int(list_numbers[0])
    for i in list_numbers:
        if int(i) > j:
            j = int(i)
        if int(i) < k:
            k = int(i)
    k = str(k)
    j = str(j)
    list_numbers[list_numbers.index(j)], list_numbers[list_numbers.index(k)] = list_numbers[list_numbers.index(k)], list_numbers[list_numbers.index(j)]
    return list_numbers


numbers = input("Введите числа через пробел: ").split()
print(myfunc(numbers))
