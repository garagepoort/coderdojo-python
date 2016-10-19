#!/usr/bin/python
from snake import *
from random import randint

class Gamelogic:

	def execute(self, window, world):
		snake = world.getSnake()

		key = window.checkKey()
		if key == 'Right':
			snake.moveRight()
		if key == 'Left':
			snake.moveLeft()
		if key == 'Up':
			snake.moveUp()
		if key == 'Down':
			snake.moveDown()

		if world.hasSnakeCollided():
			world.setGameOver()

		if world.hasSnakeFoundFood():
			if snake.getLength() > 10:
				snake.grow(2)
			else:
				snake.grow(1)
				
			world.removeFood()
			world.placeFoodInWorld(randint(0,28), randint(0,38))
			world.setScore(world.getScore() + 10)








