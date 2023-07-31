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


class Hero(Turtle):

    def __init__(self,
                 screen_width=1024,
                 screen_height=768,
                 color='white',
                 move_distance=80):
        super().__init__()
        self.shape('turtle')
        self.shapesize(2, 1)
        self.penup()
        self.color(COLOR)
        self.left(90)
        self._screen_width = screen_width
        self._screen_height = screen_height
        self._color = color

        # start position
        self._y_pos = -self._screen_height / 2 + 30
        self._x_pos_start = 0
        self._max_left_pos = 0
        self._max_right_pos = 0
        self._move_distance = move_distance
        self.goto(
            self._x_pos_start,
            self._y_pos
        )

        self._max_left_right()

    def get_move_distance(self):
        return self._move_distance

    @int_check
    def set_move_distance(self,
                          move_distance: int):
        self._move_distance = move_distance

    def _max_left_right(self):
        self._max_left_pos = -self._screen_width / 2 + 20
        self._max_right_pos = self._screen_width / 2 - 20

    def move_left(self):
        new_x = self.xcor() - self._move_distance
        if new_x >= self._max_left_pos:
            self._move(new_x)

    def move_right(self):
        new_x = self.xcor() + self._move_distance
        if new_x <= self._max_right_pos:
            self._move(new_x)

    def _move(self,
              new_x):
        self.goto(
            new_x,
            self._y_pos
        )


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

    x = Hero(move_distance=15)

    screen.listen()

    # move left and right func
    screen.onkey(key='a', fun=x.move_left)
    screen.onkey(key='Left', fun=x.move_left)
    screen.onkey(key='d', fun=x.move_right)
    screen.onkey(key='Right', fun=x.move_right)

    # Fire missle

    while True:
        screen.update()
        sleep(0.016)

        # to break loop
        if keyboard.is_pressed('p'):
            break
        else:
            pass

    screen.exitonclick()
