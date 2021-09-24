# Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

number = input('Введите число: ')

even = []
odd = []
for i in number:
    if int(i) % 2 == 0:
        even.append(i)
    else:
        odd.append(i)


def declination(numbers):
    if int(str(numbers)[-2:]) in range(10, 20) or int(str(numbers)[-1]) in [5, 6, 7, 8, 9, 10, 0]:
        state = 'четных цифр'
    elif str(numbers)[-1] == '1':
        state = 'четная цифра'
    else:
        state = 'четные цифры'
    return state


print(f'Введено число {number}, у него {len(even)} {declination(len(even))} {even} и '
      f'{len(odd)} не {declination(len(odd))} {odd}')
