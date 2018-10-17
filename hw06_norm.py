# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать
# в неограниченном кол-ве классов свой определенный предмет.
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.

# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика
#  (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе


class Klass:
    def __init__(self, class_room):
        self.class_room = class_room

    def get_name(self):
        return str(self.class_room['class_num']) + ' ' + self.class_room['class_letter']


class Person:
    def __init__(self, name, surname, father_name):
        self.name = name
        self.surname = surname
        self.father_name = father_name

    def get_full_name(self):
        return self.surname + ' ' + self.name[:1] + '.' + self.father_name[:1] + '.'


class Student(Person):
    def __init__(self, name, surname, father_name, class_room, father, mother):
        Person.__init__(self, name, surname, father_name)
        self.class_room = class_room
        self.father = father
        self.mother = mother

    def get_class_room(self):
        return self.class_room

    def get_parents(self):
        return self.father.get_full_name(), self.mother.get_full_name()


class Teacher(Person):
    def __init__(self, name, surname, father_name, classes, subject):
        Person.__init__(self, name, surname, father_name)
        self.classes = classes
        self.subject = subject

    def get_subject(self):
        return self.subject

    def get_classes(self):
        return self.classes


class_rooms = ['5 А', '4 В', '8 Б']
parents = [Person("Иван", "Сидоров", "Игоревич"),
           Person("Татьяна", "Сидорова", "Максимовна"),
           Person("Игорь", "Иванов", "Александрович"),
           Person("Ирина", "Иванова", "Александровна"),
           Person("Николай", "Петров", "Александрович"),
           Person("Светлана", "Петрова", "Николаевна")]
students = [Student("Александр", "Иванов", "Игоревич", class_rooms[0], parents[2], parents[3]),
            Student("Петр", "Сидоров", 'Иванович', class_rooms[2], parents[0], parents[1]),
            Student("Иван", "Петров", 'Николаевич', class_rooms[1], parents[4], parents[5])]
teachers = [Teacher("Иван", "Сидоров", "Игоревич", [class_rooms[0], class_rooms[1]], 'Математика'),
            Teacher("Игорь", "Иванов", "Александрович", [class_rooms[2], class_rooms[1]], 'История'),
            Teacher("Николай", "Петров", "Александрович", [class_rooms[0], class_rooms[2]], 'Английский')]

# Получить полный список всех классов школы
st = set([val.get_class_room() for val in students])
print(class_rooms)
print(st)

# Получить список всех учеников в указанном классе(каждый ученик отображается в формате "Фамилия И.О.")
cl_room = '4 В'
st_list = [val.get_full_name() for val in students if val.get_class_room() == cl_room]
print(st_list)

# 3. Получить список всех предметов указанного ученика (Ученик --> Класс --> Учителя --> Предметы)
student = students[0]
t_list = [val for val in teachers if student.get_class_room() in val.get_classes()]
t_names = [val.get_full_name for val in t_list]
subj = [val.subject for val in teachers]
print(student.get_full_name() + ' --> ' + student.get_class_room() + ' --> ' + ''.join(
    map(str, t_names)) + '--> ' + ''.join(map(str, subj)))

# 4. Узнать ФИО родителей указанного ученика
his_parents = student.get_parents()
print(his_parents)

# 5. Получить список всех Учителей, преподающих в указанном классе
# teach_list = [val.get_full_name for val in teachers if cl_room in val.get_classes]
# print(teach_list)