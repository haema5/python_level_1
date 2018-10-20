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

import random


# класс работы с мешком
class Bag:
    def __init__(self):
        self.casks = list(range(1, 91))

    # достаем боченок из мешка
    @property
    def pull(self):
        cask = random.choice(self.casks)
        var = self.casks.index(cask)
        del self.casks[var]
        return cask


# класс работы с билетами
class Card:
    def __init__(self):
        self.check_card = ()
        self._new_line = []
        self.card = []

    # создаем билет
    @property
    def create_card(self):
        self.check_card = list(range(1, 91))
        for line in range(3):
            for elem in range(5):
                var = random.choice(self.check_card)
                self._new_line.append(var)
                var = self.check_card.index(var)
                del self.check_card[var]
            self._new_line.sort()
            self.card.append(self._new_line[:])
            self._new_line.clear()
        for line in range(len(self.card)):
            for i in range(9 - len(self.card[line])):
                self.card[line].insert(random.randrange(0, len(self.card[line])), ' ')
        return self.card

    # выводим билет
    @property
    def print_card(self):
        card = '-' * 23 + '\n'
        for line in range(len(self.card)):
            for elem in self.card[line]:
                card = card + ' ' + str(elem)
            card = card + '\n'
        card = card + '-' * 23
        return card

    # ищем значение в билете
    def search_num(self, num):
        for line in self.card:
            for elem in line:
                if elem == num:
                    return True
        return False

    # вычеркиваем значение из билета
    def rem_num(self, num):
        for line in range(len(self.card)):
            for elem in self.card[line]:
                if elem == num:
                    elem = self.card[line].index(num)
                    self.card[line][elem] = 'X'

    # проверяем, остались ли цифры в билете
    @property
    def win_card(self):
        for line in self.card:
            for unit in line:
                if str(unit).isdigit():
                    return False
        return True


# класс игрового процесса
class GamePlay:
    def __init__(self, username):
        self.player_1 = username
        self.player_2 = 'Computer'

    def play(self):
        bag = Bag()

        card_1 = Card()
        card_1.create_card

        card_2 = Card()
        card_2.create_card

        while len(bag.casks) > 0:
            number = bag.pull
            print('Из мешка вынут боченок: {}. В мешке осталось: {}.'.format(number, len(bag.casks)))
            print('Билет игрока - {}:\n'.format(self.player_1), card_1.print_card)
            print('Билет игрока - {}:\n'.format(self.player_2), card_2.print_card)
            answer = input('Введите <y>, чтобы зачеркнуть, иначе игра будет продолжена: ')
            if answer == 'y':
                if card_1.search_num(number):
                    card_1.rem_num(number)
                else:
                    print('Номера в карточке не существует, вы проиграли!')
                    break
            else:
                if card_1.search_num(number):
                    print('Пропущен существующий в карточке номер, вы проиграли!')
                    break

            if card_2.search_num(number):
                card_2.rem_num(number)

            if card_1.win_card and card_2.win_card:
                print('Ничья!')
                break
            elif card_1.win_card:
                print('Выиграл игрок:', self.player_1)
                break
            elif card_2.win_card:
                print('Выиграл игрок:', self.player_2)
                break


if __name__ == '__main__':
    username = input('Введите Ваше имя: ')
    Game = GamePlay(username)
    Game.play()
