# == Лото ==
# Правила игры в лото.
# Игра ведется с помощью специальных карточек, на которых отмечены числа,
# и фишек (бочонков) с цифрами.
# Количество бочонков — 90 штук (с цифрами от 1 до 90).
# Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр,
# расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:
# --------------------------
#     9 43 62          74 90
#  2    27    75 78    82
#    41 56 63     76      86
# --------------------------
# В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается
# случайная карточка.
# Каждый ход выбирается один случайный бочонок и выводится на экран.
# Также выводятся карточка игрока и карточка компьютера.
# Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
# Если игрок выбрал "зачеркнуть":
# 	Если цифра есть на карточке - она зачеркивается и игра продолжается.
# 	Если цифры на карточке нет - игрок проигрывает и игра завершается.
# Если игрок выбрал "продолжить":
# 	Если цифра есть на карточке - игрок проигрывает и игра завершается.
# 	Если цифры на карточке нет - игра продолжается.
#
# Побеждает тот, кто первый закроет все числа на своей карточке.
# Пример одного хода:
# Новый бочонок: 70 (осталось 76)
# ------ Ваша карточка -----
#  6  7          49    57 58
#    14 26     -    78    85
# 23 33    38    48    71
# --------------------------
# -- Карточка компьютера ---
#  7 11     - 14    87
#       16 49    55 77    88
#    15 20     -       76  -
# --------------------------
# Зачеркнуть цифру? (y/n)
# Подсказка: каждый следующий случайный бочонок из мешка удобно получать
# с помощью функции-генератора.
# Подсказка: для работы с псевдослучайными числами удобно использовать
# модуль random: http://docs.python.org/3/library/random.html
#
import random


class Create_cards:
    def __init__(self):
        self.numbers = ()
        self.card = []
        self._new_line = []

    def new_card(self):\
        self.numbers = list(range(1, 91))
        for line in range(3):
            for elem in range(5):
                var = random.choice(self.numbers)
                self._new_line.append(var)
                var = self.numbers.index(var)
                del self.numbers[var]
                self._new_line.sort()
            self.card.append(self._new_line[:])
            self._new_line.clear()
        for line in range(len(self.card)):
            for i in range(9 - len(self.card[line])):
                self.card[line].insert(random.randrange(0, len(self.card[line])), ' ')
        return self.card

    # def open_bag(self):
    #     return self.numbers

    def print_card(self):
        card = '-' * 23 + '\n'
        for line in range(len(self.card)):
            for elem in self.card[line]:
                card = card + ' ' + str(elem)
            card = card + '\n'
        card = card + '-' * 23
        return card


card_1 = Create_cards()
card_2 = Create_cards()
# print('one_line', bag.open_bag())
# print('one_line', len(bag.open_bag()))
# print('one_new_card', bag.new_card())
# print('one_line', len(bag.open_bag()))
print(card_1.new_card())
print(card_2.new_card())

print(card_1.print_card())
print(card_2.print_card())
