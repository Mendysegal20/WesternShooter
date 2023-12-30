import pygame
from const import *
from piece import *


class Board:
    def __init__(self):
        self.squares = [[0, 0, 0, 0, 0, 0, 0, 0] for row in range(ROWS)]
        self._init_squares()
        self._init_pieces('white')
        self._init_pieces('black')

    def _init_squares(self):
        for row in range(ROWS):
            for col in range(COLS):
                self.squares[row][col] = Square(row, col)

    def _draw_squares(self, screen):
        for row in range(ROWS):
            for col in range(COLS):
                if (row + col) % 2 == 0:
                    color = WHITE
                else:
                    color = GREEN

                rect = (row * SQUARE_SIZE, col * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)
                pygame.draw.rect(screen, color, rect)

    def _init_pieces(self,color):
        pawn_row, other_row = (6, 7) if color == 'white' else (1, 0)

        # pawns
        for col in range(COLS):
            self.squares[pawn_row][col] = Square(pawn_row, col, Pawn(pawn_row, col, color))

        # knights
        self.squares[other_row][1] = Square(other_row, col, Knight(other_row, 1, color))
        self.squares[other_row][6] = Square(other_row, col, Knight(other_row, 6, color))

        # bishops
        self.squares[other_row][2] = Square(other_row, 2, Bishop(other_row, 2, color))
        self.squares[other_row][5] = Square(other_row, 5, Bishop(other_row, 5, color))

        # rooks
        self.squares[other_row][0] = Square(other_row, 0, Rook(other_row, 0, color))
        self.squares[other_row][7] = Square(other_row, 7, Rook(other_row, 7, color))

        # king
        self.squares[other_row][4] = Square(other_row, 4, King(other_row, 4, color))

        # queen
        self.squares[other_row][3] = Square(other_row, 3, Queen(other_row, 3, color))

    def _draw_pieces(self, screen):
        for row in range(ROWS):
            for col in range(COLS):
                if self.squares[row][col].has_piece():
                    piece = self.squares[row][col].piece
                    piece.draw(screen)

    def draw(self, screen):
        self._draw_squares(screen)
        self._draw_pieces(screen)

    def move(self, row, col, piece):
        if self.squares[row][col].has_piece():
            self.squares[row][col].clear_square()
        self.squares[row][col], self.squares[piece.row][piece.col] = self.squares[piece.row][piece.col], self.squares[row][col]
        piece.move(row, col)


class Square:
    def __init__(self, row, col, piece=None):
        self.row = row
        self.col = col
        self.piece = piece

    def has_piece(self):
        return self.piece != None

    def clear_square(self):
        del self.piece
        self.piece = None
