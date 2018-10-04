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


def oper(x):
    x = x.split(' ')
    for i in x:
        if i == '+' or i == '-' or i == '*' or i == '/' or i == '**':
            # result = ' ' + i + ' '
            result = i
            break
        else:
            result = False
    return result


def do_that(a, b, s):
    if s == '+':
        result = a + b
    elif s == '-':
        result = a - b
    elif s == '*':
        result = a * b
    elif s == '/':
        result = a / b
    elif s == '**':
        result = a ** b
    return result

def wo_wh(drob):
    def is_int(x):
        try:
            int(x)
            return True
        except ValueError:
            return False

    if len(drob) > 1:
        drob_cz = drob[1].split('/')
        if drob[0][0] == '-':
            result = '-' + (str(math.fabs(int(drob[0])) * int(drob_cz[1]) + int(drob_cz[0])) + '/' + drob_cz[1])
        else:
            result = str(int(drob[0]) * int(drob_cz[1]) + int(drob_cz[0])) + '/' + drob_cz[1]
        result = float(result.split('/')[0]) / float(result.split('/')[1])
    else:
        if is_int(drob[0]):
            result = float(drob[0])
        else:
            drob_cz = drob[0].split('/')
            result = str(int(drob_cz[0]) / int(drob_cz[1]))
            result = float(result)
    return result


def reduce_frac(n, m):
    x = math.gcd(n, m)
    return (n // x, m // x)

def add(a,b,c,d):
    x = a*d + b*c
    y = b*d
    z = math.gcd(x, y)
    return (x//z, y//z)

print('ADDDDDD',add(1,4,1,2))

def to_drob(d_drob):
    dt = 0
    pt = 0

    pt, dt = math.modf(d_drob)

    print(dt, pt)

    pt = int(str(pt).split('.')[1])
    print('to_drob dt, pt', dt, pt)
    print(len(str(pt)))

    print('1' + '0' * len(str(pt)))
    n, m = reduce_frac(int(pt), int('1' + '0' * len(str(pt))))
    result = str(int(dt)) + ' ' + str(n) + '/'+ str(m)

    return result


# vir = '1 5/6 + -5 4/7'
vir = '1/3 + 1/2'
print(oper(vir))

if oper(vir):
    drob_a = vir.split(' ' + oper(vir) + ' ')[0].split(' ')
    drob_b = vir.split(' ' + oper(vir) + ' ')[1].split(' ')

    print(drob_a, oper(vir), drob_b)

    print()
    print(wo_wh(drob_a))
    print(wo_wh(drob_b))
    print()

    print('result', do_that(wo_wh(drob_a), wo_wh(drob_b), oper(vir)))

    summ = (do_that(wo_wh(drob_a), wo_wh(drob_b), oper(vir)))

    print('DROOOOOB', to_drob(summ))



else:
    print('Ошибка! Нет арифметического действия.')

# math.modf
# ['1', '5/6', '+', '4/7']

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
