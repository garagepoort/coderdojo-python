#!/usr/bin/python

class WorldPiece:

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

	def hasSamePosition(self, piece):
		return self.col == piece.getCol() and self.row == piece.getRow()