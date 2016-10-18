#!/usr/bin/python
from snake import *

class World:

 	def __init__(self):
		self.snake = Snake();
 		self.gameOver = False

	def getSnake(self):
		return self.snake

 	def setGameOver(self):
 		self.gameOver = True

 	def isGameOver(self):
 		return self.gameOver

	def hasSnakeCollided(self):
		head = self.snake.getPieces()[0]
		if head.getCol() == -1:
			return True
		if head.getCol() == 40:
			return True
		if head.getRow() == -1:
			return True
		if head.getRow() == 30:
			return True

		for i in range(1, self.snake.getLength()):
			piece = self.snake.getPieces()[i]; 
			if piece.getCol() == head.getCol() and piece.getRow() == head.getRow():
				return True

		return False;