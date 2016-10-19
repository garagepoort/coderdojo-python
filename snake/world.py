#!/usr/bin/python
from snake import *

class World:

 	def __init__(self):
 		self.maxRows = 30
 		self.maxCols = 40
 		self.score = 0
		self.foodPieces = [ WorldPiece(15, 8) ];
		self.removedFoodPieces = []
		self.snake = Snake(15, 20);
 		self.gameOver = False

	def getSnake(self):
		return self.snake

 	def setGameOver(self):
 		self.gameOver = True

 	def isGameOver(self):
 		return self.gameOver

	def hasSnakeCollided(self):
		head = self.snake.getHead()
		if self.snake.getDirection() == 'LEFT' and head.getCol() == 0:
			return True
		if self.snake.getDirection() == 'RIGHT' and head.getCol() == 39:
			return True
		if self.snake.getDirection() == 'UP' and head.getRow() == 0:
			return True
		if self.snake.getDirection() == 'DOWN' and head.getRow() == 29:
			return True

		for i in range(1, self.snake.getLength()):
			piece = self.snake.getPieces()[i];
			if piece.hasSamePosition(head):
				return True

		return False;

	def getFoodPieces(self):
		return self.foodPieces

	def	getRemovedFoodPieces(self):
		return self.removedFoodPieces

	def hasSnakeFoundFood(self):
		head = self.snake.getHead()
		for piece in self.foodPieces:
			if piece.hasSamePosition(head):
				return True

	def placeFoodInWorld(self, row, col):
		self.foodPieces.append(WorldPiece(row, col))

	def removeFood(self):
		self.removedFoodPieces.append(self.foodPieces[0])
		self.foodPieces.pop(0)

	def setScore(self, score):
		self.score = score

	def getScore(self):
		return self.score

	def getMaxRows(self):
		return self.maxRows

	def getMaxCols(self):
		return self.maxCols