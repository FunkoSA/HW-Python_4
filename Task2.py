"""
# 2 - Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности. Не использовать множества.
* [1,1,1,1,2,2,2,3,3,3,4] -> [1,2,3,4]
"""

ish_list = [1,1,1,1,2,2,2,3,3,3,4]
def distinct_list(array):
    out_list = []
    for i in array:
        if i not in out_list:
            out_list.append(i)
    return out_list
print(f'Список {ish_list} состоит из следующих элементов: {distinct_list(ish_list)}')
