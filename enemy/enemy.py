"""

Portfolio: SpaceAttack Game
#100DaysOfCode with Python
Day: 93
Date: 2023-07-28
Author: MC

Enemy class

"""

from turtle import Turtle, Screen
from time import sleep
import keyboard
from random import randint


BLOCK_COLORS = ["#69345F",
                "#171D69",
                "#B57952",
                "#B8B071",
                "#35AEB8",
                "#B8709B",
                "#7E7FB8",
                "#268EB8",
                "#519E21",
                "#6A839E",
                "white"]


class Enemy(Turtle):

    def __init__(self,
                 screen_width=1024,
                 screen_height=768,
                 color='white',
                 move_distance=10,
                 start_pos_x=0,
                 start_pos_y=0):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.color(color)
        self.right(90)

        # screen
        self._screen_width = screen_width
        self._screen_height = screen_height

        # start position
        self.start_pos_x = start_pos_x
        self.start_pos_y = start_pos_y
        self.goto(
            self.start_pos_x,
            self.start_pos_y
        )

        self._max_left_pos = 0
        self._max_right_pos = 0
        self._move_distance = move_distance

        self._max_left_right()

    def _max_left_right(self):
        self._max_left_pos = -self._screen_width / 2 + 20
        self._max_right_pos = self._screen_width / 2 - 20


# some tests
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

    x = Enemy(move_distance=15)

    screen.listen()

    # move left and right func
    # screen.onkey(key='a', fun=x.move_left)
    # screen.onkey(key='Left', fun=x.move_left)
    # screen.onkey(key='d', fun=x.move_right)
    # screen.onkey(key='Right', fun=x.move_right)

    # Fire missle
    # screen.onkey(key='space', fun=x.fire_bullet)
    # screen.onkey(key='Up', fun=x.fire_bullet)

    while True:
        screen.update()
        sleep(0.016)

        if len(x.bullets) > 0:
            for bullet in x.bullets:
                if bullet.get_max_flag() is False:
                    bullet.fire()
                else:
                    del x.bullets[0]

        # to break loop
        if keyboard.is_pressed('p'):
            break
        else:
            pass

    screen.exitonclick()
