# В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.

def myfunc(list_number):
    j = int(list_number[0])
    for i in list_number:
        if int(i) < j:
            j = int(i)
    return j, list_number.index(str(j))


numbers = input('Введите числа через пробел: ').split()
print(f'Минимальное число {myfunc(numbers)[0]} с индексом {myfunc(numbers)[1]}')
