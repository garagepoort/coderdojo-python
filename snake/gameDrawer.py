#!/usr/bin/python
from graphics import *

class GameDrawer:

	def __init__(self, window):
		self.score = Text(Point(3,4), '0')
		self.border = 10
		self.blockSize = 10
		self.window = window

	def draw(self, world):
		if self.window.isClosed() == False:
			snake = world.getSnake()

			if world.isGameOver() == False:
				for piece in world.getRemovedFoodPieces():
					if piece.getRect() is not None:
						piece.getRect().undraw()

				for piece in world.getFoodPieces():
					self.drawWorldPiece(piece, self.blockSize, 'red')

				for piece in snake.getPieces():
					self.drawWorldPiece(piece, self.blockSize, 'black')

			self.score.undraw()
			self.score = Text(Point(400,320), world.getScore())
			self.score.draw(self.window)

	def drawBorders(self, world):
		aRectangle = Rectangle(Point(self.border, self.border),Point(world.getMaxCols() * self.blockSize + self.border, world.getMaxRows() * self.blockSize + self.border))
		aRectangle.draw(self.window)

	def drawWorldPiece(self, piece, size, color):
		if piece.getRect() is not None:
			piece.getRect().undraw()

		x = (piece.col * size) + self.border
		y = (piece.row * size) + self.border

		aRectangle = Rectangle(
			Point(x, y),
			Point(x + size, y + size))

		aRectangle.setFill(color)
		aRectangle.setOutline('white')
		aRectangle.draw(self.window)
		piece.setRect(aRectangle)