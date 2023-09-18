# Заполните массив элементами арифметической прогрессии.
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

def fill_list(number, perv_el, raznitsa):
    for i in range(number):
        if i == 0:
            an = perv_el
            masiv.append(an)
        else:
            an = perv_el + i * raznitsa
            masiv.append(an)


def print_list(array):
    for i in range(len(array)):
        print(array[i])


masiv = list()
a1 = int(input('Введите первый элемент арифметической прогрессии: '))
n = int(input('Введите количество элементов: '))
d = int(input('Введите разность: '))
fill_list(n, a1, d)
print_list(masiv)
