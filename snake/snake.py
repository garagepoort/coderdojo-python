#!/usr/bin/python
from worldpiece import WorldPiece

class Snake:

	def __init__(self, startRow, startCol):
		self.pieces = []
		self.pieces.append(WorldPiece(startRow, startCol))
		self.pieces.append(WorldPiece(startRow, startCol + 1))
		self.pieces.append(WorldPiece(startRow, startCol + 2))
		self.pieces.append(WorldPiece(startRow, startCol + 3))

		self.lastTailRow = startRow
		self.lastTailCol = startCol + 3

		self.speed = 1;
		self.direction = 'LEFT';

	def getSpeed(self):
		return self.speed;

	def getDirection(self):
		return self.direction

	def getLength(self):
		return len(self.pieces)

	def getPieces(self):
		return self.pieces

	def moveLeft(self):
		if(self.direction != 'RIGHT'):
			self.direction = 'LEFT'

	def moveRight(self):
		if(self.direction != 'LEFT'):
			self.direction = 'RIGHT'
	
	def moveUp(self):
		if(self.direction != 'DOWN'):
			self.direction = 'UP'
	
	def moveDown(self):
		if(self.direction != 'UP'):
			self.direction = 'DOWN'

	def grow(self):
		self.pieces.append(WorldPiece(self.lastTailRow, self.lastTailCol))

	def getHead(self):
		return self.pieces[0]

	def move(self):
		head = self.pieces[0]
		tail = self.pieces[-1]

		self.lastTailRow = tail.getRow()
		self.lastTailCol = tail.getCol()

		tail.setCol(head.getCol())
		tail.setRow(head.getRow())

		if self.direction == 'LEFT':
			tail.setCol(head.getCol() - 1)
		if self.direction == 'RIGHT':
			tail.setCol(head.getCol() + 1)
		if self.direction == 'UP':
			tail.setRow(head.getRow() - 1)
		if self.direction == 'DOWN':
			tail.setRow(head.getRow() + 1)

		self.pieces.remove(tail)
		self.pieces.insert(0, tail)
