# В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.

number = []
for i in range(2, 99):
    k = True
    for j in range(2, 9):
        if i % j != 0:
            k = False
    if k is True:
        number.append([i])
print(f'{f"Следующие числа кратны диапазону от 2 до 9 {number}" if len(number) > 0 else "Ни одно число не кратно диапазону от 2 до 9" }')
