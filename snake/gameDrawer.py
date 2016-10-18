#!/usr/bin/python
from graphics import *

class GameDrawer:

	def __init__(self, window):
		self.blockSize = 10
		self.window = window

	def draw(self, world):
		snake = world.getSnake()

		if world.isGameOver() == False:
			for piece in world.getRemovedFoodPieces():
				if piece.getRect() is not None:
					piece.getRect().undraw()

			for piece in world.getFoodPieces():
				self.drawWorldPiece(piece, self.blockSize, 'red')

			for piece in snake.getPieces():
				self.drawWorldPiece(piece, self.blockSize, 'black')

	def drawWorldPiece(self, piece, size, color):
		if piece.getRect() is not None:
			piece.getRect().undraw()

		x = piece.col * size
		y = piece.row * size

		aRectangle = Rectangle(
			Point(x, y),
			Point(x + size, y + size))

		aRectangle.setFill(color)
		aRectangle.setOutline('white')
		piece.setRect(aRectangle)
		aRectangle.draw(self.window)