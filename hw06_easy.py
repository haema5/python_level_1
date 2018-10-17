# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.
import math


class Triangle:
    def __init__(self, apoint, bpoint, cpoint):
        self.apoint = apoint
        self.bpoint = bpoint
        self.cpoint = cpoint
        self.len_a = math.hypot(bpoint[1] - apoint[1], bpoint[0] - apoint[0])
        self.len_b = math.hypot(cpoint[1] - bpoint[1], cpoint[0] - bpoint[0])
        self.len_c = math.hypot(apoint[1] - cpoint[1], apoint[0] - cpoint[0])

    @property
    def perimetr(self):
        return self.len_a + self.len_b + self.len_c

    @property
    def height(self):
        p = self.perimetr / 2
        return 2 * math.sqrt(p * (p - self.len_a) * (p - self.len_b) * (p - self.len_c)) / self.len_c

    @property
    def area(self):
        return 0.5 * self.len_c * self.height



# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

class Trapezium:
    def __init__(self, apoint, bpoint, cpoint, dpoint):
        self.apoint = apoint
        self.bpoint = bpoint
        self.cpoint = cpoint
        self.dpoint = dpoint
        self.diag_1 = math.hypot(cpoint[1] - apoint[1], cpoint[0] - apoint[0])
        self.diag_2 = math.hypot(dpoint[1] - bpoint[1], dpoint[0] - bpoint[0])

    def check(self):
        if self.diag_1 == self.diag_2:
            return True
        else:
            return False

    @property
    def len_a(self):
        return math.hypot(self.bpoint[1] - self.apoint[1], self.bpoint[0] - self.apoint[0])

    @property
    def len_b(self):
        return math.hypot(self.cpoint[1] - self.bpoint[1], self.cpoint[0] - self.bpoint[0])

    @property
    def len_c(self):
        return math.hypot(self.dpoint[1] - self.cpoint[1], self.dpoint[0] - self.cpoint[0])

    @property
    def len_d(self):
        return math.hypot(self.apoint[1] - self.dpoint[1], self.apoint[0] - self.dpoint[0])

    def perimetr(self):
        return self.len_a + self.len_b + self.len_c + self.len_d

    def area(self):
        area = 0.25 * (self.len_b + self.len_d) * math.sqrt(4 * self.len_a ** 2 - (self.len_d - self.len_b) ** 2)
        return area

if __name__ == '__main__':
    trglk = Triangle((0, 0), (30, 15), (0, 30))

    print('Задача-1:\nПериметр треугольника:\n {}'.format(trglk.perimetr))
    print('Высота треугольника:\n {}'.format(trglk.height))
    print('Площадь треугольника:\n {}'.format(trglk.area))

    rb_trap = Trapezium((0, 0), (2, 6), (4, 6), (6, 0))
    if rb_trap.check():
        print('\nЗадача-2:\nФигура равнобочная трапеция.\n')

        print('Длины сторон трапеции:\n AB = {}, \n BC = {}, \n CD = {}, \n DA = {}'.format(rb_trap.len_a, rb_trap.len_b, rb_trap.len_c, rb_trap.len_d))

        print('Периметр трапеции:\n', rb_trap.perimetr())
        print('Площадь трапеции:\n', rb_trap.area())
    else:
        print('Фигура не равнобочная трапеция.')