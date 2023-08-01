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
MAX_HERO_BULLETS = 5
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
    move_distance=20,
    max_hero_bullets=MAX_HERO_BULLETS
)

# ------------------------------ init enemies ------------------------------
enemies = []


def create_enemies():
    global enemies

    for row in range(ROWS):
        y_pos = int(SCREEN_HEIGHT/2 - 50 - 50 * row)
        x_pos = int(-SCREEN_HEIGHT/2 + randint(0, 150))
        for col in range(COLS):
            x_pos = x_pos + 50 * col
            if x_pos < SCREEN_WIDTH/2 - 40:
                enemies.append(
                    Enemy(
                        screen_width=SCREEN_WIDTH,
                        screen_height=SCREEN_HEIGHT,
                        color=BLOCK_COLORS[row],
                        start_pos_x=x_pos,
                        start_pos_y=y_pos
                    )
                )


create_enemies()

# ------------------------------ main loop ------------------------------

screen.listen()

screen.onkey(key='a', fun=hero.move_left)
screen.onkey(key='Left', fun=hero.move_left)
screen.onkey(key='d', fun=hero.move_right)
screen.onkey(key='Right', fun=hero.move_right)

screen.onkey(key='space', fun=hero.fire_bullet)
screen.onkey(key='Up', fun=hero.fire_bullet)

while game_core.get_game_over_flag():
    screen.update()
    sleep(0.016)
    # sleep(0.05)

    if len(enemies) == 0:
        create_enemies()

    for enemie in enemies:
        enemie.move()
        if enemie.get_fire_flag() is True:
            if enemie.my_bullet.distance(hero) < 15:
                print("You was kill")
                enemie.my_bullet.reset()
                enemie.my_bullet.hideturtle()
                enemie.my_bullet.color(SCREEN_BG_COLOR)
                enemie.my_bullet.set_max_flag(False)
                game_core.loose_life()
                scoreboard.set_life_info(
                    game_core.cur_life
                )
                scoreboard.refresh()
                hero.reset_hero()
                break

    # hero fire
    if len(hero.bullets) > 0:
        for bullet_idx in range(len(hero.bullets)):

            is_target_hit = False

            if len(enemies) > 0:
                for index in range(len(enemies)):
                    if hero.bullets[bullet_idx].distance(enemies[index]) < 15:
                        # is enemie fire
                        if enemies[index].get_fire_flag() is True:
                            enemies[index].my_bullet.reset()
                            enemies[index].my_bullet.hideturtle()
                            enemies[index].my_bullet.color(SCREEN_BG_COLOR)
                            enemies[index].my_bullet.set_max_flag(False)

                        enemies[index].hideturtle()
                        enemies[index].reset()
                        enemies[index].color(SCREEN_BG_COLOR)
                        enemies.pop(index)
                        is_target_hit = True
                        scoreboard.set_curr_score()
                        break

            if is_target_hit is True:
                hero.bullets[bullet_idx].reset()
                hero.bullets[bullet_idx].hideturtle()
                hero.bullets[bullet_idx].set_max_flag(True)

            if hero.bullets[bullet_idx].get_max_flag() is False:
                hero.bullets[bullet_idx].fire()
            else:
                del hero.bullets[bullet_idx]
                break

    # press 'p' to break loop
    if keyboard.is_pressed('p'):
        break
    else:
        pass

if game_core.get_game_over_flag() is False and scoreboard.get_curr_score() > 0:
    game_core.set_win_name()
    scoreboard.add_curr_result(game_core.name)


# ------------------------------ exit ------------------------------
screen.exitonclick()

