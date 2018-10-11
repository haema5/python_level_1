from os import mkdir, rmdir, listdir, remove
from os.path import exists, isdir
from shutil import copy

# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.
print('Задача-1:')


def make_dir():
    for dir_name in range(1, 9):
        mkdir('./dir_' + str(dir_name))


def del_dir():
    for dir_name in range(1, 9):
        rmdir('./dir_' + str(dir_name))


try:
    make_dir()
    print('Создал директории dir_1 - dir_9!')
except:
    print('Ошибка! Не смог создать директории.')
finally:
    try:
        del_dir()
        print('Удалил директории dir_1 - dir_9!')
    except:
        print('Ошибка! Не смог удалить директории.')

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.
print('\nЗадача-2:')

ls = [i for i in listdir('.') if isdir(i)]

for dir_name in ls:
    print(dir_name)

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
print('\nЗадача-3:')


def duplicate_file():
    copy(__file__, __file__ + '_dupl')
    if exists(__file__ + '_dupl'):
        return True
    else:
        return False


if duplicate_file():
    print('Файл {}_dupl был успешно создан!'.format(__file__))

    try:
        remove(__file__ + '_dupl')
        print('И удален...')
    except:
        print('А удалить не получилось...')

else:
    print('Ошибка! {}_dupl не был создан.'.format(__file__))
