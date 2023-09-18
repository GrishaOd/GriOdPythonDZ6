# Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)

import random


def fill_rand_array(array, number):
    for i in range(number):
        ai = random.randint(-99, 100)
        array.append(ai)


n = int(input('Введите количество элементов массива: '))
max = int(input('Введите максимальное значение: '))
min = int(input('Введите минимальное значение: '))
masiv = list()
fill_rand_array(masiv, n)
print(masiv)
for i in range(len(masiv)):
    if masiv[i] < max and masiv[i] > min:
        print(f'Элемент с индексом {i} входит в диапазон ({min}, {max})')


