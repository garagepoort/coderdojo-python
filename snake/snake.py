#!/usr/bin/python
from worldpiece import WorldPiece


class Snake:

    def __init__(self, start_row, start_col):
        self.pieces = []
        self.pieces_to_grow = []
        self.pieces.append(WorldPiece(start_row, start_col))
        self.pieces.append(WorldPiece(start_row, start_col + 1))
        self.pieces.append(WorldPiece(start_row, start_col + 2))
        self.pieces.append(WorldPiece(start_row, start_col + 3))

        self.last_tail_row = start_row
        self.last_tail_col = start_col + 3

        self.speed = 1
        self.direction = 'LEFT'

    def get_speed(self):
        return self.speed

    def get_direction(self):
        return self.direction

    def get_length(self):
        return len(self.pieces)

    def get_pieces(self):
        return self.pieces

    def move_left(self):
        if self.direction != 'RIGHT':
            self.direction = 'LEFT'

    def move_right(self):
        if self.direction != 'LEFT':
            self.direction = 'RIGHT'

    def move_up(self):
        if self.direction != 'DOWN':
            self.direction = 'UP'

    def move_down(self):
        if self.direction != 'UP':
            self.direction = 'DOWN'

    def grow(self, size):
        for i in range(0, size):
            self.pieces_to_grow.append(WorldPiece(self.last_tail_row, self.last_tail_col))

    def get_head(self):
        return self.pieces[0]

    def move(self):
        if self.pieces_to_grow:
            piece = self.pieces_to_grow.pop()
            self.pieces.append(piece)

        head = self.pieces[0]
        tail = self.pieces[-1]

        self.last_tail_row = tail.get_row()
        self.last_tail_col = tail.get_col()

        tail.set_col(head.get_col())
        tail.set_row(head.get_row())

        if self.direction == 'LEFT':
            tail.set_col(head.get_col() - 1)
        if self.direction == 'RIGHT':
            tail.set_col(head.get_col() + 1)
        if self.direction == 'UP':
            tail.set_row(head.get_row() - 1)
        if self.direction == 'DOWN':
            tail.set_row(head.get_row() + 1)

        self.pieces.remove(tail)
        self.pieces.insert(0, tail)
