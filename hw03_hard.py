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


# Определение операции
def operation_type(vyr):
    vyr = vyr.split(' ')

    for type in vyr:
        if type == '+' or type == '-':
            result = ' ' + type + ' '
            break
        else:
            result = False

    return result


# Разбор вырожения на элементы
def decomposition(vyr):
    vyr = vyr.split(operation_type(vyr))

    a_fraction = vyr[0].split(' ')
    b_fraction = vyr[1].split(' ')

    return (a_fraction, b_fraction)


# Замена пустых значений нулями
def add_null(fraction):
    while len(fraction) < 2:
        if is_int(fraction[0]):
            fraction.append(0)
        else:
            fraction.insert(0, 0)
    return fraction


# Проверка типа данных
def is_int(x):
    try:
        int(x)
        return True
    except ValueError:
        return False


# Приведение дроби к неправильному виду
def bad_view(fraction):
    if fraction[1] != 0:
        if int(fraction[0]) >= 0:
            n_frac = fractions.Fraction(fraction[1]) + int(fraction[0])
        else:
            n_frac = - fractions.Fraction(fraction[1]) + int(fraction[0])
    else:
        n_frac = fraction[0]
    return n_frac


# Приведение дроби к правильному виду
def true_view(fraction):
    if is_int(str(fraction)) == False:
        fraction = str(fraction).split('/')
        n = int(fraction[0])
        d = int(fraction[1])
        x = 0
        if math.fabs(n) > d:
            x = n // d
            x = '{} {}/{}'.format(x, (n - d * x), d)
        else:
            x = '{}/{}'.format(n, d)
    else:
        x = fraction
    return x

def answer(a_fraction, b_fraction):
    if operation_type(vyr) == ' + ':
        answer = true_view(fractions.Fraction(bad_view(a_fraction)) + fractions.Fraction(bad_view(b_fraction)))
    elif operation_type(vyr) == ' - ':
        answer = true_view(fractions.Fraction(bad_view(a_fraction)) - fractions.Fraction(bad_view(b_fraction)))
    return answer

# Исходные данные
# vyr = '5/6 + 4/7'
# vyr = '-2/3 - -2'
vyr = input('Введите выражение: ')

# Разбор вырожения на элементы
a_fraction, b_fraction = decomposition(vyr)

# Замена пустых значений нулями
a_fraction = add_null(a_fraction)
b_fraction = add_null(b_fraction)

# Расчет
if operation_type(vyr) == ' + ':
    answer = true_view(fractions.Fraction(bad_view(a_fraction)) + fractions.Fraction(bad_view(b_fraction)))
elif operation_type(vyr) == ' - ':
    answer = true_view(fractions.Fraction(bad_view(a_fraction)) - fractions.Fraction(bad_view(b_fraction)))

# Вывод ответа
print('Ответ: {} = {}'.format(vyr, answer))

print(answer(a_fraction,b_fraction))

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
