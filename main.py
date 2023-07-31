"""

Portfolio: SpaceAttack Game
#100DaysOfCode with Python
Day: 93
Date: 2023-07-28
Author: MC

"""


from turtle import Screen
from time import sleep
from random import randint

import keyboard

from scoreboard import Scoreboard
from game_core import Game_core
from hero import Hero
from enemy import Enemy


# game start options
SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 768
SCREEN_BG_COLOR = "#727272"

ROWS = 7
COLS = 7
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


# ------------------------------ screen setup ------------------------------
screen = Screen()
screen.title('..:: Space Attack by MC ::..')
screen.setup(
    width=SCREEN_WIDTH,
    height=SCREEN_HEIGHT
)
screen.bgcolor(SCREEN_BG_COLOR)
screen.tracer(0)

# ------------------------------ init game core ------------------------------
game_core = Game_core()

# ------------------------------ init scoreboard ------------------------------
scoreboard = Scoreboard(
    screen_width=SCREEN_WIDTH,
    screen_height=SCREEN_HEIGHT,
    score_file_path='score_data.csv'
)
scoreboard.set_life_info(
    game_core.cur_life
)
scoreboard.refresh()

# ------------------------------ init hero ------------------------------
hero = Hero(
    screen_width=SCREEN_WIDTH,
    screen_height=SCREEN_HEIGHT,
)

# ------------------------------ init enemies ------------------------------
enemies = []

for row in range(ROWS):
    y_pos = int(SCREEN_HEIGHT/2 - 50 - 50 * row)
    x_pos = int(-SCREEN_HEIGHT/2 + randint(0, 150))
    for col in range(COLS):
        x_pos = x_pos+ 50 * col
        enemies.append(
            Enemy(
                screen_width=SCREEN_WIDTH,
                screen_height=SCREEN_HEIGHT,
                color=BLOCK_COLORS[row],
                start_pos_x=x_pos,
                start_pos_y=y_pos
            )
        )

# ------------------------------ main loop ------------------------------

screen.listen()

screen.onkey(key='a', fun=hero.move_left)
screen.onkey(key='Left', fun=hero.move_left)
screen.onkey(key='d', fun=hero.move_right)
screen.onkey(key='Right', fun=hero.move_right)

screen.onkey(key='space', fun=hero.fire_bullet)
screen.onkey(key='Up', fun=hero.fire_bullet)

while True:
    screen.update()
    sleep(0.016)

    # hero fire
    if len(hero.bullets) > 0:
        for bullet in hero.bullets:
            if bullet.get_max_flag() is False:
                bullet.fire()
            else:
                del hero.bullets[0]

    for enemie in enemies:
        enemie.move()
        if enemie.get_fire_flag() is True:
            if enemie.my_bullet.distance(hero) < 20:
                print("You was kill")
                game_core.loose_life()

    # todo: collision detector

    # press 'p' to break loop
    if keyboard.is_pressed('p'):
        break
    else:
        pass

# ------------------------------ exit ------------------------------
screen.exitonclick()

