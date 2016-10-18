#!/usr/bin/python
from graphics import *

class GameDrawer:

	def __init__(self):
		self.blockSize = 10

	def draw(self, window, gamelogic):
		snake = gamelogic.getSnake()

		for i in range(0, snake.getLength()):
			piece = snake.pieces[i]

			if piece.getRect() is not None:
				piece.getRect().undraw()

			x = (piece.col + 1) * self.blockSize
			y = (piece.row + 1) * self.blockSize

			aRectangle = Rectangle(
				Point(x, y),
				Point(x + self.blockSize, y + self.blockSize))

			piece.setRect(aRectangle)
			aRectangle.draw(window)

