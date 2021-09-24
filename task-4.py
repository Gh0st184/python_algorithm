"""
Написать программу, которая генерирует в указанных пользователем границах:

случайное целое число;
случайное вещественное число;
случайный символ.

Для каждого из трех случаев пользователь задает свои границы диапазона.
Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы.
Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.
"""

import random

left_border = input('Введите левую границу диапазона: ')
right_border = input('Введите правую границу диапазона: ')


def check(number):
    try:
        float(number)
        state = 'float'
    except ValueError:
        try:
            int(number)
            state = 'int'
        except ValueError:
            state = 'str'
    return state


if __name__ == '__main__':
    if right_border.isdigit() and left_border.isdigit():
        print(random.randrange(int(left_border), int(right_border)))
    elif check(right_border) == 'float' and check(left_border) == 'float':
        print(round(random.uniform(float(left_border), float(right_border)), 2))
    elif check(right_border) == 'str' and check(left_border) == 'str':
        print(chr(random.randrange(ord(left_border.lower()), ord(right_border.lower()))))
