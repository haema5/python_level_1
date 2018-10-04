# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1
print()
print('Задание-1:')


def fibonacci(n, m):
    fib = []
    f1, f2 = 1, 1
    i = 0
    while i <= m:
        fib.append(f1)
        f1, f2 = f2, f1 + f2
        i += 1
    return fib[n - 1:m]


print(fibonacci(5, 20))

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()
print()
print('Задание-2:')


def sort_to_max(origin_list):
    x = 1
    while x < len(origin_list):
        for y in range(len(origin_list) - x):
            if origin_list[y] > origin_list[y + 1]:
                origin_list[y], origin_list[y + 1] = origin_list[y + 1], origin_list[y]
        x += 1
    return origin_list


print('Отсортированный список:', sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0]))

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.
print()
print('Задание-3:')


def my_filter(function_name, sequence):
    filter_sequence = []
    for i in sequence:
        if function_name(i):
            filter_sequence.append(i)
    return filter_sequence


def positive(x):
    if x > 0:
        return True
    else:
        return False


lst = [2, 10, -12, 2.5, 20, -11, 4, 4, 0]

lst = my_filter(positive, lst)
lst = list(lst)

print(lst)

# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.
print()
print('Задание-4:')
import math


def length(a, b):
    length = math.sqrt(math.fabs(((b[1] - a[1]) ** 2) + ((b[0] - a[0]) ** 2)))
    return length


a1 = [1, 1]
a2 = [2, 3]
a3 = [7, 3]
a4 = [6, 1]

a1a2 = length(a1, a2)
a3a4 = length(a3, a4)
a2a3 = length(a2, a3)
a1a4 = length(a1, a4)

# a1a2=a3a4, a2a3=a1a4
if a1a2 == a3a4 and a2a3 == a1a4:
    print('Даны вершины параллелограмма')
else:
    print('Даны не вершины параллелограмма')
