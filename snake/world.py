#!/usr/bin/python
from snake import *


class World:

    def __init__(self):
        self.max_rows = 30
        self.max_cols = 40
        self.score = 0
        self.food_pieces = [WorldPiece(15, 8)]
        self.removed_food_pieces = []
        self.snake = Snake(15, 20)
        self.game_over = False

    def get_snake(self):
        return self.snake

    def set_game_over(self):
        self.game_over = True

    def is_game_over(self):
        return self.game_over

    def has_snake_collided(self):
        head = self.snake.get_head()
        if self.snake.get_direction() == 'LEFT' and head.get_col() == 0:
            return True
        if self.snake.get_direction() == 'RIGHT' and head.get_col() == 39:
            return True
        if self.snake.get_direction() == 'UP' and head.get_row() == 0:
            return True
        if self.snake.get_direction() == 'DOWN' and head.get_row() == 29:
            return True

        for i in range(1, self.snake.get_length()):
            piece = self.snake.get_pieces()[i]
            if piece.has_same_position(head):
                return True

        return False

    def get_food_pieces(self):
        return self.food_pieces

    def get_removed_food_pieces(self):
        return self.removed_food_pieces

    def has_snake_found_food(self):
        head = self.snake.get_head()
        for piece in self.food_pieces:
            if piece.has_same_position(head):
                return True

    def place_food_in_world(self, row, col):
        self.food_pieces.append(WorldPiece(row, col))

    def remove_food(self):
        self.removed_food_pieces.append(self.food_pieces[0])
        self.food_pieces.pop(0)

    def set_score(self, score):
        self.score = score

    def get_score(self):
        return self.score

    def get_max_rows(self):
        return self.max_rows

    def get_max_cols(self):
        return self.max_cols
