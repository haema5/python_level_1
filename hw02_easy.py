__author__ = 'Пашков Игорь Владимирович'

import random

# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

# Подсказка: воспользоваться методом .format()

list_0 = ["яблоко", "банан", "киви", "арбуз"]

i = 0
while i < len(list_0):
    print('{}. {}'.format(i + 1, list_0[i]))
    i += 1

# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.

list_1 = ["яблоко", "банан", "киви", "арбуз", "арбуз"]
list_2 = ["томат", "киви", "баклажан", "арбуз"]

print('Первый список:', list_1)
print('Второй список:', list_2)
print('')

x = 0
y = 0

for x in range(len(list_1)):
    for y in range(len(list_2)):
        li1 = list_1[x]
        li2 = list_2[y]
        if li1 == li2:
            del list_1[x]

print(list_1)
# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.
