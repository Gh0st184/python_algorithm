""" Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
Вывести на экран это число и сумму его цифр. """


def myfunc(numbers):
    n = 0
    b = ''
    for i in numbers:
        k = 0
        for j in i:
            k += int(j)
        if k > n:
            n = k
            b = i
    return n, b


number = input("Введите последовательность чисел разделенных пробелом: ").split()
print(f'Наибольшее по сумме цифр является число - {myfunc(number)[1]}, сумма его цифр - {myfunc(number)[0]}')
