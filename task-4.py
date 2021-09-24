# Определить, какое число в массиве встречается чаще всего.


def myfunc(list_number):
    a = 0
    b = ''
    for i in list_number:
        k = 0
        for j in list_number:
            if j == i:
                k += 1
        if k > a:
            a = k
            b = i
    return a, b


numbers = input('Введите числа через пробел: ').split()
print(f'Цифра {myfunc(numbers)[1]} встречается {myfunc(numbers)[0]} раз')
