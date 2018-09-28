#!/usr/bin/python
from snake import *
from random import randint


class GameLogic:

    def execute(self, window, world):
        snake = world.get_snake()

        key = window.checkKey()
        if key == 'Right':
            snake.move_right()
        if key == 'Left':
            snake.move_left()
        if key == 'Up':
            snake.move_up()
        if key == 'Down':
            snake.move_down()

        if world.has_snake_collided():
            world.set_game_over()

        if world.has_snake_found_food():
            if snake.get_length() > 10:
                snake.grow(2)
            else:
                snake.grow(1)

            world.remove_food()
            world.place_food_in_world(randint(0, 28), randint(0, 38))
            world.set_score(world.get_score() + 10)
