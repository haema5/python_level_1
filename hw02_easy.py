__author__ = 'Пашков Игорь Владимирович'

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
print('Задача 1')
print('')
rvn = 0
z1_list1 = ["яблоко", "банан", "киви", "арбуз"]

print('С помощью while:')

z1_count1 = 0
while z1_count1 < len(z1_list1):
    rvn = 10 - len(z1_list1[z1_count1])
    print(str(z1_count1 + 1) + '.' + ' ' * rvn + z1_list1[z1_count1])
    # print('{}. {}'.format(z1_count1 + 1, z1_list1[z1_count1]))
    z1_count1 += 1

print('')
print('С помощью for:')

z1_count2 = 0
for z1_unit1 in z1_list1:
    z1_count2 += 1
    rvn = 10 - len(z1_unit1)
    print(str(z1_count2) + '.' + ' ' * rvn + z1_unit1)
    # print('{}. {}'.format(z1_count2, z1_unit1))

print('')

# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.
print('Задача 2')
print('')

z2_list1 = ["яблоко", "банан", "киви", "арбуз", "арбуз"]
z2_list2 = ["томат", "киви", "баклажан", "арбуз"]

print('Первый список:', z2_list1)
print('Второй список:', z2_list2)
print('')

z2_count1 = 0

for z2_unit1 in range(len(z2_list2)):
    while z2_count1 < len(z2_list1):
        if z2_list1[z2_count1] == z2_list2[z2_unit1]:
            del z2_list1[z2_count1]
            z2_count1 -= 1
        z2_count1 += 1
    z2_count1 = 0

print('Отредактированный список:', z2_list1)

# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.

print('')
print('Задача 3')
print('')

z3_list1 = [3, 5, 1, 2, 4, 6, 3, 2, 3, 4]
z3_list2 = []

print('Исходный список:', z3_list1)

for z3_unit1 in z3_list1:
    if z3_unit1 % 2:
        z3_list2.append(z3_list1[z3_unit1] * 2)
    else:
        z3_list2.append(z3_list1[z3_unit1] / 4)

print('Новый список:', z3_list2)
