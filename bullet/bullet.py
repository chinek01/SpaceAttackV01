"""

Portfolio: SpaceAttack Game
#100DaysOfCode with Python
Day: 93
Date: 2023-07-28
Author: MC

Bullet class

"""

from turtle import Turtle, Screen
import keyboard
from time import sleep


class Bullet(Turtle):

    def __init__(self,
                 start_pos_x=None,
                 start_pos_y=None,
                 speed=1,
                 direction='Up',
                 screen_width=800,
                 screen_height=600):
        """
        init bullet class
        :param start_pos_x: start position x coordinate
        :param start_pos_y: start position y coordinate
        :param speed: bullet speed
        :param direction: up or down
        """
        super().__init__()
        self.penup()
        self.start_pos_x = start_pos_x
        self.start_pos_y = start_pos_y
        self.speed = speed
        self.direction = direction
        self.screen_width = screen_width
        self.screen_height = screen_height

        if self.direction.__str__().lower() == 'up':
            self.left(90)
        else:
            self.right(90)
            self.speed = -self.speed

        self.max_top_y = None
        self.max_down_y = None
        self.max_xy()
        self.max_flag = False

    def get_max_flag(self):
        return self.max_flag

    def max_xy(self):
        self.max_top_y = self.screen_height/2 + 20
        self.max_down_y = -self.screen_height/2 - 20

    def fire(self):
        new_x = self.xcor()
        new_y = self.ycor() + self.speed

        if self.max_down_y < new_y < self.max_top_y:
            self.max_flag = False
        else:
            self.max_flag = True

        self.goto(new_x, new_y)


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

    x = Bullet(direction='up',
               speed=10,
               screen_width=width,
               screen_height=height)

    screen.listen()

    # move left and right func

    fire_flag = False

    while x.get_max_flag() is False:
        screen.update()
        sleep(0.1)

        if keyboard.is_pressed('space'):
            fire_flag = True

        if fire_flag:
            x.fire()

        # to break loop
        if keyboard.is_pressed('p'):
            break
        else:
            pass

    screen.exitonclick()
