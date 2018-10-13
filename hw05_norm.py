# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: 'Успешно создано/удалено/перешел',
# 'Невозможно создать/удалить/перейти'

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py

import os
import hw05_norm_functions as func

print('Задача-1:')
directory = os.path.abspath(os.path.dirname(__file__))

answer = ''
while answer != 'q':
    answer = input('Хочешь поработать? (y-Да/n-Нет/q-Выйти) ')
    if answer == 'y':
        print('Отлично!')
        print('Я умею делать следующие вещи:')
        print('  1 - Перейти в папку')
        print('  2 - Просмотреть содержимое текущей папки')
        print('  3 - Удалить папку')
        print('  4 - Создать папку')
        do = int(input('\nЧем могу помочь? '))
        if do == 1:
            directory = os.path.abspath(input('Введите путь: '))
            if os.path.exists(directory):
                print('Успешно перешел в {}!'.format(directory))
            else:
                print('Такой директории не существует.')
        elif do == 2:
            print('В директории {} следующие элементы: '.format(directory))
            print([i for i in os.listdir(directory)])
        elif do == 3:
            dir_name = input('Введите имя директории: ')
            try:
                path = os.path.join(directory, dir_name)
                func.del_dir(path)
                print('Успешно удалено!')
            except:
                dir_name = input('Невозможно удалить!')
        elif do == 4:
            dir_name = input('Введите имя директории: ')
            try:
                path = os.path.join(directory, dir_name)
                func.make_dir(path)
                print('Успешно создал!')
            except:
                dir_name = input('Невозможно создать!')
        else:
            print('Этого я не умею...')
    elif answer == 'n':
        print('Очень жалко, но я хочу работать! Жми <y>!')
    else:
        if do == 'q':
            print('Пока-пока!')
        else:
            print('Я не понимаю тебя...')
