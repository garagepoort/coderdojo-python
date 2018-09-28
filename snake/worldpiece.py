#!/usr/bin/python


class WorldPiece:

    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.rect = None

    def get_col(self):
        return self.col

    def get_row(self):
        return self.row

    def set_row(self, row):
        self.row = row

    def set_col(self, col):
        self.col = col

    def set_rect(self, rect):
        self.rect = rect

    def get_rect(self):
        return self.rect

    def has_same_position(self, piece):
        return self.col == piece.get_col() and self.row == piece.get_row()
