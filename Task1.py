"""
Данные, функции и модули в Python. Продолжение

1 - Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
N = 20 -> [2,5]
N = 30 -> [2, 3, 5]
"""
n = int(input('Введите натуральное число: '))
def get_simple_list (number):
    '''Функция получения списка простых чисел'''
    lst=[2]
    for i in range(3, number+1, 2):
        if (i > 10) and (i%10==5):
            continue
        for j in lst:
            if j*j-1 > i:
                lst.append(i)
                break
            if (i % j == 0):
                break
        else:
            lst.append(i)
    return lst

def simple_mylt (array, numnber):
    '''Функция получения множителей числа'''
    out_list = []
    for i in array:
        if numnber % i == 0:
            out_list.append(i)
    return out_list

print (f'Число {n} можно получить из произведения следующих простых чисел: {simple_mylt(get_simple_list(n),n)}')
exit()


import math
numbers = [i for i in range (2,int(input('Введите число для расчета: ')) + 1)]
#print (numbers)
sq_numbers = int(math.sqrt(max(numbers)))
print (sq_numbers)
for i in numbers:
    if numbers.index(i) < sq_numbers+1:
        print(i)

