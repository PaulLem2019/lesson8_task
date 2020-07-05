"""
== Лото ==

Правила игры в лото.

Игра ведется с помощью спе циальных карточек, на которых отмечены числа,
и фишек (бочонков) с цифрами.

Количество бочонков — 90 штук (с цифрами от 1 до 90).

Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр,
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:

--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86
--------------------------

В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается
случайная карточка.

Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.

Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
    Если цифра есть на карточке - она зачеркивается и игра продолжается.
    Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
    Если цифра есть на карточке - игрок проигрывает и игра завершается.
    Если цифры на карточке нет - игра продолжается.

Побеждает тот, кто первый закроет все числа на своей карточке.

Пример одного хода:

Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71
--------------------------
-- Карточка компьютера ---
 7 87     - 14    11
      16 49    55 88    77
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)

Подсказка: каждый следующий случайный бочонок из мешка удобно получать
с помощью функции-генератора.

Подсказка: для работы с псевдослучайными числами удобно использовать
модуль random: http://docs.python.org/3/library/random.html
"""
import random

class Card:
    def __init__(self, name):
        self.namecard = name
        self.card_delete_numb = [[0 for _ in range(5)] for _ in range(3)]
        self.number_card = [[0 for _ in range(5)] for _ in range(3)]

        numbers = [random.randint(1, 90) for _ in range(30)]
        numbers2 = [param for param in numbers if numbers.count(param) == 1]

        for numb in range (len(numbers2)-15):
            numbers2.pop(numb)

        for numb in range(3):
            for numb1 in range(5):
                self.number_card[numb][numb1] = numbers2[numb*5+numb1]

            self.number_card[numb].sort()

    def __str__(self):
        self.card = ''
        for numb in range(3):
            for numb1 in range (5):
                if self.card_delete_numb[numb][numb1] == 0:
                    self.card += " " + str (self.number_card[numb][numb1]) + "    " + " "*random.randint(0,6)
                else:
                    self.card += " --    " + " "*random.randint(0,6)

            self.card += "\n"
        return f'{"-"*(24 - int(len(self.namecard)/2))} {self.namecard} {"-"*(24-int(len(self.namecard)/2+0.5))} \n{self.card}{"-"*50}'

    def exclude_numb(self, number):
        for numb in range(3):
            for numb1 in range(5):
                if number == self.number_card[numb][numb1]:
                    self.card_delete_numb[numb][numb1] = -1
                    return True
        return False

    def check_numb(self, number):
        for numb in range(3):
            for numb1 in range(5):
                if number == self.number_card[numb][numb1]:
                    return True
        return False

    def check_win(self):
        numb_s = 0
        for numb, item in enumerate (self.card_delete_numb):
            numb_s += item.count(-1)
        if numb_s == 15:
            return True
        return False

class GamePlay():
    _numb_list = []

    def start(self):
        b_quit = True
        while b_quit:
            barrel = GamePlay.gen_barrel_number(GamePlay)
            print (f'Выпал боченок номер {barrel} осталось {90-len(GamePlay._numb_list)}')
            print (loto_card_user)
            print (loto_card_computer)
            answer = input("Зачеркнуть цифру? (y/n)")
            if answer == "y":
                state = loto_card_user.exclude_numb(barrel)
                if state == True:
                    print ("Хорошо, играем дальше")
                else:
                    print ("Вы проиграли! Такой цифры нет")
                    b_quit = False
            else:
                state = loto_card_user.check_numb(barrel)
                if state == True:
                    print ("Вы проиграли! Такая цифра есть!")
                    b_quit = False
                else:
                    print ("Хорошо, играем дальше")
            loto_card_computer.exclude_numb(barrel)

            if loto_card_computer.check_win():
                print (f"{loto_card_computer.namecard} выиграл! Зачеркнуты все цифры в карточке")
                print (loto_card_computer)
                b_quit = False

            if loto_card_user.check_win():
                print (f"{loto_card_user.namecard} выиграл! Зачеркнуты все цифры в карточке")
                print (loto_card_user)
                b_quit = False

    def gen_barrel_number(self):
        b_quit = True
        prom = 0
        while b_quit:
            prom = random.randint(1, 90)
            if len(GamePlay._numb_list) >= 90:
                b_quit = False
                prom = -1
            if GamePlay._numb_list.count(prom) == 0:
                GamePlay._numb_list.append(prom)
                b_quit = False
        return prom

loto_card_user = Card('user')
loto_card_computer = Card('computer')
game = GamePlay()

game.start()
