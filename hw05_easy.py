from os import mkdir, rmdir, listdir, remove
from os.path import exists, isdir, abspath
from shutil import copy

# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.
print('Задача-1:')


def make_dir(dir_name):
    mkdir(abspath(dir_name))


def del_dir(dir_name):
    rmdir(abspath(dir_name))


for i in range(1, 10):
    dir_name = 'dir_' + str(i)
    try:
        make_dir(dir_name)
        print('Создал директорию {}!'.format(dir_name))
    except:
        print('Ошибка! Не смог создать директории.')

print('\n########\n')

for i in range(1, 10):
    dir_name = 'dir_' + str(i)
    try:
        del_dir(dir_name)
        print('Удалил директорию {}!'.format(dir_name))
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
