"""

Portfolio: SpaceAttack Game
#100DaysOfCode with Python
Day: 93
Date: 2023-07-28
Author: MC

Hero class

"""

import turtle
from turtle import Turtle, Screen
from time import sleep
import keyboard

COLOR = 'yellow'


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


class Hero:

    def __init__(self,
                 screen_width=1024,
                 screen_height=768,
                 color='white',
                 move_distance=80):
        self._screen_width = screen_width
        self._screen_height = screen_height
        self._color = color

        # start position
        self._y_pos = -self._screen_height / 2 + 30
        self._x_pos_start = 0
        self._max_left_pos = 0
        self._max_right_pos = 0
        self._move_distance = move_distance

        self._body = []

        self._max_left_right()

        self.my_hero()

    def my_hero(self):
        h = Turtle()
        h.shape('turtle')
        h.shapesize(2, 1)
        h.penup()
        h.color(COLOR)
        h.goto(0, 0)
        h.left(90)
        self._body.append(h)

    def get_move_distance(self):
        return self._move_distance

    @int_check
    def set_move_distance(self,
                          move_distance: int):
        self._move_distance = move_distance

    def _max_left_right(self):
        self._max_left_pos = self._screen_width / 2 + 20
        self._max_right_pos = self._screen_width / 2 - 20


# some test
if __name__ == '__main__':
    width = 1024
    height = 768
    screen = Screen()
    screen.title("Hero test")
    screen.setup(
        width=width,
        height=height
    )
    screen.bgcolor('#727272')
    screen.tracer(0)

    x = Hero()

    screen.listen()

    # move left and right func

    while True:
        screen.update()
        sleep(0.01)

        # to break loop
        if keyboard.is_pressed('p'):
            break
        else:
            pass

    screen.exitonclick()