#!/usr/bin/python
from snake import *

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







