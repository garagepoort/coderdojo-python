#!/usr/bin/python
from snake import *

class Gamelogic:

	def __init__(self):
		self.snake = Snake();

	def getSnake(self):
		return self.snake

	def execute(self, window):
		key = window.checkKey()
		if key == 'Right':
			self.snake.moveRight()
		if key == 'Left':
			self.snake.moveLeft()
		if key == 'Up':
			self.snake.moveUp()
		if key == 'Down':
			self.snake.moveDown()
