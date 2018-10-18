# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать
# в неограниченном кол-ве классов свой определенный предмет.
# Т.е. Учитель Уханов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.

# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате 'Фамилия И.О.')
# 3. Получить список всех предметов указанного ученика
#  (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе

class Klass:
    def __init__(self, klass_name):
        self.klass_name = klass_name

    @property
    def get_klass_name(self):
        return self.klass_name


class Persons:
    def __init__(self, name, surname, father_name):
        self.name = name
        self.surname = surname
        self.father_name = father_name

    def get_fio(self):
        return self.surname + ' ' + self.name[:1] + '.' + self.father_name[:1] + '.'


class Student(Persons):
    def __init__(self, name, surname, father_name, klass, father, mother):
        Persons.__init__(self, name, surname, father_name)
        self.klass = klass
        self.father = father
        self.mother = mother

    def get_klass(self):
        return self.klass

    def get_parents(self):
        return self.father.get_fio(), self.mother.get_fio()


class Teacher(Persons):
    def __init__(self, name, surname, father_name, classes, subject):
        Persons.__init__(self, name, surname, father_name)
        self.classes = classes
        self.subject = subject

    def get_subject(self):
        return self.subject

    def get_classes(self):
        klass_name = [var for var in self.classes]
        return klass_name


klass = [Klass('5 А'),
         Klass('4 В'),
         Klass('8 Б')]
parents = [Persons('Иван', 'Сафронов', 'Игоревич'),
           Persons('Татьяна', 'Сафронова', 'Максимовна'),
           Persons('Игорь', 'Уханов', 'Александрович'),
           Persons('Ирина', 'Уханова', 'Александровна'),
           Persons('Николай', 'Каунев', 'Александрович'),
           Persons('Светлана', 'Каунева', 'Николаевна')]
students = [Student('Александр', 'Уханов', 'Игоревич', klass[0].get_klass_name, parents[2], parents[3]),
            Student('Петр', 'Сафронов', 'Уханович', klass[2].get_klass_name, parents[0], parents[1]),
            Student('Иван', 'Каунев', 'Николаевич', klass[1].get_klass_name, parents[4], parents[5])]
teachers = [Teacher('Иван', 'Сафронов', 'Игоревич', [klass[0].get_klass_name, klass[1].get_klass_name], 'Математика'),
            Teacher('Игорь', 'Уханов', 'Александрович', [klass[2].get_klass_name, klass[1].get_klass_name], 'История'),
            Teacher('Николай', 'Каунев', 'Александрович', [klass[0].get_klass_name, klass[2].get_klass_name],
                    'Английский')]

# 1. Получить полный список всех классов школы
print('Список всех классов:\n', [var.get_klass_name for var in klass])

# 2. Получить список всех учеников в указанном классе
# klass_name = '4 В'
klass_name = klass[1].get_klass_name
print('\nВ классе <{}> учатся:\n'.format(klass_name),
      [var.get_fio() for var in students if var.get_klass() == klass_name])

# 3. Получить список всех предметов указанного ученика
#  (Ученик --> Класс --> Учителя --> Предметы)
# pupil_name = 'Сафронов П.И.'
pupil_name = students[1]

print('\nУченик:\n', pupil_name.get_fio())
print('Класс:\n', pupil_name.get_klass())
print('Учителя:\n', [var.get_fio() for var in teachers if pupil_name.get_klass() in var.get_classes()])
print('Предметы:\n', [var.get_subject() for var in teachers if pupil_name.get_klass() in var.get_classes()])

# # 4. Узнать ФИО родителей указанного ученика
# pupil_name = 'Сафронов П.И.'
pupil_name = students[1]
print('\nРодители ученика <{}>:\n'.format(pupil_name.get_fio()), pupil_name.get_parents())

# # 5. Получить список всех Учителей, преподающих в указанном классе
# klass_name = '4 В'
klass_name = klass[1].get_klass_name
print('\nКласс <{}> обучают:\n'.format(klass_name),
      [var.get_fio() for var in teachers if klass_name in var.get_classes()])
