# Задание-1:
# Написать программу, выполняющую операции (сложение и вычитание) с простыми дробями.
# Дроби вводятся и выводятся в формате:
# n x/y ,где n - целая часть, x - числитель, у - знаменатель.
# Дроби могут быть отрицательные и не иметь целой части, или иметь только целую часть.
# Примеры:
# Ввод: 5/6 + 4/7 (всё выражение вводится целиком в виде строки)
# Вывод: 1 17/42  (результат обязательно упростить и выделить целую часть)
# Ввод: -2/3 - -2
# Вывод: 1 1/3

import math
import fractions


def operation_type(expression):
    expression = expression.split(' ')
    for type in expression:
        if type == '+' or type == '-':  # or type == '*' or type == '/' or type == '**':
            result = ' ' + type + ' '
            break
        else:
            result = False
    return result


def decomposition(expression):
    expression = expression.split(operation_type(expression))

    a_fraction = expression[0].split(' ')
    b_fraction = expression[1].split(' ')

    return (a_fraction, b_fraction)


def solve_it(expression):
    def is_int(x):
        try:
            int(x)
            return True
        except ValueError:
            return False

    def add_null(fraction):
        while len(fraction) < 2:
            if is_int(fraction[0]):
                fraction.append('')
            else:
                fraction.insert(0, '')
        return fraction

    def reduce_frac(n, m):
        x = math.gcd(n, m)
        return (n // x, m // x)

    def summ(a, b):
        summ = a + b
        return summ

    def razn(a, b):
        razn = a - b
        return razn

    def frac_summ(a, b, c, d):
        x = a * d + b * c
        y = b * d
        z = math.gcd(x, y)
        return (x // z, y // z)

    def frac_razn(a, b, c, d):
        x = a * d - b * c
        y = b * d
        z = math.gcd(x, y)
        return (x // z, y // z)

    a_fraction, b_fraction = decomposition(expression)

    a_fraction = add_null(a_fraction)
    b_fraction = add_null(b_fraction)

    print('a_fraction {}, b_fraction {}, syml {}'.format(a_fraction, b_fraction, operation_type(expression)))
    print(operation_type(expression))
    dt = [a_fraction[0], b_fraction[0]]
    pt = [a_fraction[1], b_fraction[1]]
    if operation_type(expression) == ' + ':
        # вычисление целой части
        if is_int(dt[0]) and is_int(dt[1]):
            dt = summ(int(dt[0]), int(dt[1]))
        elif is_int(dt[0]):
            dt = int(dt[0])
        elif is_int(dt[1]):
            dt = int(dt[1])
        else:
            dt = 0

        # вычисление дробной части
        if a_fraction[1] != '' and b_fraction[1] != '':
            pt = fractions.Fraction(a_fraction[1]) + fractions.Fraction(b_fraction[1])
        elif a_fraction[1] == '':
            pt = b_fraction[1]
        elif b_fraction[1] == '':
            pt = a_fraction[1]
        else:
            pt = ''

    elif operation_type(expression) == ' - ':
        dt = razn(int(dt[0]), int(dt[1]))

    if is_int(pt):
        dt = dt + pt
        pt = ''

    print('{} {}'.format(dt, pt))
    return ('{} {}'.format(dt, pt))


#expression = '1 2/3 + 2 1/3'
expression = '5/6 + 4/7'

print(solve_it(expression))
# print(solve_it(expression))\


# Задание-2:
# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки
# они получают удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"


# Задание-3:
# Дан файл ("data/fruits") со списком фруктов.
# Записать в новые файлы все фрукты, начинающиеся с определенной буквы.
# Т.е. в одном файле будут все фрукты на букву “А”, во втором на “Б” и т.д.
# Файлы назвать соответственно.
# Пример имен файлов: fruits_А, fruits_Б, fruits_В ….
# Важно! Обратите внимание, что нет фруктов, начинающихся с некоторых букв.
# Напишите универсальный код, который будет работать с любым списком фруктов
# и распределять по файлам в зависимости от первых букв, имеющихся в списке фруктов.
# Подсказка:
# Чтобы получить список больших букв русского алфавита:
# print(list(map(chr, range(ord('А'), ord('Я')+1))))
