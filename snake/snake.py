#!/usr/bin/python

class Snake:

	def __init__(self):
		self.pieces = []
		self.pieces.append(SnakePiece(3,0))
		self.pieces.append(SnakePiece(3,1))
		self.pieces.append(SnakePiece(3,2))
		self.pieces.append(SnakePiece(3,3))
		self.pieces.append(SnakePiece(3,4))
		self.pieces.append(SnakePiece(3,5))
		self.pieces.append(SnakePiece(3,6))
		self.speed = 1;
		self.direction = 'DOWN';

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

	def move(self):
		head = self.pieces[0]
		tail = self.pieces[-1]

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


class SnakePiece:

	def __init__(self, row, col):
		self.row = row;
		self.col = col;
		self.rect = None

	def getCol(self):
		return self.col;

	def getRow(self):
		return self.row;

	def setRow(self, row):
		self.row = row

	def setCol(self, col):
		self.col = col

	def setRect(self, rect):
		self.rect = rect

	def getRect(self):
		return self.rect