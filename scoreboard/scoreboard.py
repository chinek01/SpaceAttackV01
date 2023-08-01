"""

Portfolio: SpaceAttack Game
#100DaysOfCode with Python
Day: 93
Date: 2023-07-28
Author: MC

"""

import turtle
from turtle import Turtle
from turtle import Screen
import csv
import keyboard

FONT = ("Arial", 14, "normal")
ALIGN = "center"
FRAME_COLOR = 'white'


def int_check(func):
    def wrapper(self, *args, **kwargs):
        for arg in args:
            if not isinstance(arg, int):
                raise TypeError("Argument must be int type!")

        for key, value in kwargs.items():
            if not isinstance(value, int):
                raise TypeError("All keyword arguments must be int type!")

        return func(self, *args, **kwargs)

    return wrapper


def str_check(func):
    def wrapper(self, *args, **kwargs):
        for arg in args:
            if not isinstance(arg, str):
                raise TypeError("Argument must be str type!")

        for key, value in kwargs.items():
            if not isinstance(value, str):
                raise TypeError("All keyword arguments must be strings.")

        return func(self, *args, **kwargs)

    return wrapper


def none_check(func):
    def wrapper(self, *args, **kwargs):
        for arg in args:
            if arg is None:
                raise ValueError("Argument must be set!")

        for key, value in kwargs.items():
            if value is None:
                raise TypeError("All keyword arguments must be strings.")

        return func(self, *args, **kwargs)

    return wrapper


class Scoreboard(Turtle):

    def __init__(self,
                 screen_width=1024,
                 screen_height=768,
                 score_file_path=None):
        super().__init__()

        self.screen_width = None
        self.screen_height = None

        self.set_screen_width(screen_width)
        self.set_screen_height(screen_height)

        # at start project this line will be comment, but not in main app
        self.score_file_path = None
        self.set_score_file_path(score_file_path)
        self._score_data = None
        self._read_results_from_file()

        self._max_score = []
        self._find_max_score()
        self._curr_result = []

        self._text_color = FRAME_COLOR
        self._curr_score = 0
        self._life_info = 0

        self._frame_color = FRAME_COLOR
        self._frame_height = 100
        self._frame()

    @int_check
    def set_screen_width(self,
                         screen_width: int):
        self.screen_width = screen_width

    def get_screen_width(self):
        return self.screen_width

    @int_check
    def set_screen_height(self, screen_height: int):
        self.screen_height = screen_height

    def get_screen_height(self):
        return self.screen_height

    def get_screen(self):
        return self.screen_width, self.screen_height

    @str_check
    @none_check
    def set_score_file_path(self, score_file_path):
        self.score_file_path = score_file_path

    def _read_results_from_file(self):
        """
        Read scores from file
        :return: score list
        """
        try:
            with open(self.score_file_path, 'r') as file:
                self._score_data = list(csv.reader(file))
        except Exception as e:
            print(f"Something bad happened {e.__str__()}")

    def _save_results_to_file(self):
        """
        Save results to file
        :return:
        """

        try:
            with open(self.score_file_path, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(self._score_data)
        except Exception as e:
            print(f"Something bad happened {e.__str__()}")

    def _find_max_score(self):
        """
        Find The Max result
        """
        self._max_score = ['', '0']

        for row in self._score_data:
            # print(row)
            try:
                if int(self._max_score[1]) < int(row[1]):
                    self._max_score = row
            except Exception as e:
                print(f"Some error: {e.__str__()}")

    @int_check
    def set_life_info(self,
                      life_info: int):
        self._life_info = life_info

    def get_life_info(self):
        return self._life_info

    def set_curr_score(self):
        self._curr_score += 1
        self.refresh()

    def _frame(self):
        """
        Build scoreboard frame
        """
        myPen = turtle.Turtle()
        myPen.penup()
        myPen.setposition(
            -self.screen_width/2 + 10,
            -self.screen_height/2 + self._frame_height
        )
        myPen.color(self._frame_color)
        myPen.pendown()
        myPen.pensize(5)

        for side in range(2):
            myPen.forward(self.screen_width - 30)

        myPen.hideturtle()

    def refresh(self):
        """
        Refresh scoreboard
        """

        self.clear()

        # write score
        self.hideturtle()
        self.penup()
        self.color(self._text_color)

        # current score
        first_x = self.screen_width / 4
        first_y = -self.screen_height / 2 + self._frame_height / 2

        self.goto(
            first_x,
            first_y
        )
        self.write(
            f'Current score: {self._curr_score}',
            font=FONT
        )

        # current life
        first_x = -self.screen_width / 2 + 50

        self.goto(
            first_x,
            first_y
        )
        self.write(
            f"Life: {self._life_info}",
            font=FONT
        )


# some test
if __name__ == '__main__':
    width = 1024
    height = 768
    screen = Screen()
    screen.title("Scoreboard test")
    screen.setup(
        width=width,
        height=height
    )
    screen.bgcolor('#727272')
    screen.tracer(0)

    x = Scoreboard(
        screen_width=width,
        screen_height=height,
        score_file_path='../score_data.csv'
    )

    screen.listen()
    screen.onkey(key='a', fun=x.set_curr_score)
    x.set_curr_score()

    while True:
        screen.update()

        if keyboard.is_pressed('`'):
            break
        else:
            pass

    screen.exitonclick()