#!/usr/bin/python
from graphics import *


class GameDrawer:

    def __init__(self, window):
        self.score = Text(Point(3, 4), '0')
        self.border = 10
        self.blockSize = 10
        self.window = window

    def draw(self, world):
        if not self.window.isClosed():
            snake = world.get_snake()

            if not world.is_game_over():
                for piece in world.get_removed_food_pieces():
                    if piece.get_rect() is not None:
                        piece.get_rect().undraw()

                for piece in world.get_food_pieces():
                    self.draw_world_piece(piece, self.blockSize, 'red')

                for piece in snake.get_pieces():
                    self.draw_world_piece(piece, self.blockSize, 'black')

            self.score.undraw()
            self.score = Text(Point(400, 320), world.get_score())
            self.score.draw(self.window)

    def draw_borders(self, world):
        a_rectangle = Rectangle(Point(self.border, self.border), Point(world.get_max_cols() * self.blockSize + self.border, world.get_max_rows() * self.blockSize + self.border))
        a_rectangle.draw(self.window)

    def draw_world_piece(self, piece, size, color):
        if piece.get_rect() is not None:
            piece.get_rect().undraw()

        x = (piece.col * size) + self.border
        y = (piece.row * size) + self.border

        a_rectangle = Rectangle(
            Point(x, y),
            Point(x + size, y + size))

        a_rectangle.setFill(color)
        a_rectangle.setOutline('white')
        a_rectangle.draw(self.window)
        piece.set_rect(a_rectangle)
