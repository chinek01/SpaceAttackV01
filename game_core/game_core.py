"""

Portfolio: SpaceAttack Game
#100DaysOfCode with Python
Day: 93
Date: 2023-07-28
Author: MC

Game Core class

"""

from turtle import textinput


LIFE = 3


class Game_core:

    def __init__(self):
        self.cur_life = LIFE
        self.is_game_over_flag = True
        self.is_start_game_flag = False
        self.name = 'MC'

    def set_win_name(self):
        self.name = textinput(
            "Enter your name: ",
            "Name: "
        )

    def loose_life(self):
        self.cur_life -= 1
        self.check_life()

    def check_life(self):
        if self.cur_life == 0:
            self.is_game_over_flag = False

    def get_game_over_flag(self):
        return self.is_game_over_flag

    def start_game(self):
        if self.is_start_game_flag is False:
            self.is_start_game_flag = True
            self.is_game_over_flag = False

    def reset_game(self):
        self.cur_life = LIFE
        self.is_game_over_flag = True
        self.is_start_game_flag = False


# some test
if __name__ == '__main__':
    x = Game_core()
    x.set_win_name()
    print(f"{x.name}")
