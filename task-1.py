# 1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала
# (т.е. 4 отдельных числа) для каждого предприятия.. Программа должна определить среднюю прибыль
# (за год для всех предприятий) и вывести наименования предприятий, чья прибыль выше среднего и отдельно вывести
# наименования предприятий, чья прибыль ниже среднего.


data = {}
while True:
    company = input('Введите название предприятия или 0 для выхода из цикла: ')
    if company == '0':
        break
    b = 1
    a = []
    while b != 5:
        a.append(input(f'Введите прибыль {company} за {b} квартал: '))
        b += 1
    c = 0
    for i in a:
        c += int(i)
    a.append(c / len(a))
    data[company] = a

average = 0
for j in data:
    average += data[j][-1]
average /= len(data)

higher = []
below = []
for k in data:
    if data[k][-1] > average:
        higher.append(k)
    else:
        below.append(k)
print(f'У следующих предприятий {higher} прибыль выше средней {average}')
print(f'У следующих предприятий {below} прибыль ниже средней {average}')
