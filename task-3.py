# Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
# Например, если введено число 3486, то надо вывести число 6843.

number = input('Введите число: ')


def reverse(value):
    if len(value) == 0:
        return value
    else:
        return reverse(value[1:]) + value[0]


print(number)
number = reverse(number)
print(number)
