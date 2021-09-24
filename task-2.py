"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50).
Выведите на экран исходный и отсортированный массивы.
"""

import random


def merge_sort(array):
    def merge(fst, snd):
        res = []
        i, j = 0, 0
        while i < len(fst) and j < len(snd):
            if fst[i] < snd[j]:
                res.append(fst[i])
                i += 1
            else:
                res.append(snd[j])
                j += 1
        res.extend(fst[i:] if i < len(fst) else snd[j:])
        return res

    def div_half(lst):
        if len(lst) == 1:
            return lst
        elif len(lst) == 2:
            return lst if lst[0] <= lst[1] else lst[::-1]
        else:
            return merge(div_half(lst[:len(lst)//2]), div_half(lst[len(lst)//2:]))
    return div_half(array)


size = 10
min_item = 0
max_item = 50
array = [random.randint(min_item, max_item) for _ in range(size)]

print(f'Before sort: {array}')
print(f'After sort: {array}')