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
from bullet.bullet import Bullet


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

        # bullet time
        self.my_bullet: Bullet = None
        self._fire_flag = False

    def _fire_bullet(self):

        if self.my_bullet is None:

            if randint(0, 1000) >= 990:

                flare = Bullet(
                    direction='down',
                    speed=3,
                    screen_width=self._screen_width,
                    screen_height=self._screen_height,
                    start_pos_x=self.xcor(),
                    start_pos_y=self.ycor()-20
                )

                self.my_bullet = flare
                self._fire_flag = True

        else:
            if self.my_bullet.get_max_flag() is False:
                self.my_bullet.fire()
            else:
                del self.my_bullet
                self.my_bullet = None

    def get_fire_flag(self):
        return self._fire_flag

    def _max_left_right(self):
        self._max_left_pos = -self._screen_width / 2 + 20
        self._max_right_pos = self._screen_width / 2 - 20

    def move(self):
        new_x = self.xcor() - self._move_distance
        if new_x <= self._max_left_pos:
            self._bounce()

        if new_x >= self._max_right_pos:
            self._bounce()

        self.goto(
            new_x,
            self.start_pos_y
        )

        self._fire_bullet()

    def _bounce(self):
        self._move_distance *= -1


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

    x = Enemy(move_distance=2)

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

        # if len(x.bullets) > 0:
        #     for bullet in x.bullets:
        #         if bullet.get_max_flag() is False:
        #             bullet.fire()
        #         else:
        #             del x.bullets[0]
        x.move()

        # to break loop
        if keyboard.is_pressed('p'):
            break
        else:
            pass

    screen.exitonclick()
