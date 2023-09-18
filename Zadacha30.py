# Заполните массив элементами арифметической прогрессии.
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

def fill_list(number, pervEl, raznitsa):
    for i in range(number):
        if i == 0:
            an = pervEl
            masiv.append(an)
        else:
            an = pervEl + i * raznitsa
            masiv.append(an)
def print_list(array):
    for i in range(len(masiv)):
        print(masiv[i])
masiv = list()
a1 = int(input('Введите первый элемент арифметической прогрессии: '))
n = int(input('Введите количество элементов: '))
d = int(input('Введите разность: '))
fill_list(n, a1, d)
print_list(masiv)
