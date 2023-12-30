import pygame
from const import *
from board import Board


class Game:
    def __init__(self, screen):
        self.board = Board()
        self.screen = screen
        self.valid_moves = []
        self.selected = None
        self.turn = WHITE
        self.is_check = False

    def create(self):
        self.board.draw(self.screen)

    def move(self, row, col):
        if self.selected and (row, col) in self.valid_moves:
            self.selected.moved = True
            self.board.move(row, col, self.selected)
            self.change_turn()
        else:
            return False
        return True

    def draw_valid_moves(self, moves):
        for move in moves:
            row, col = move
            pygame.draw.circle(self.screen, BLUE, (col * SQUARE_SIZE + SQUARE_SIZE//2, row * SQUARE_SIZE + SQUARE_SIZE//2), 15)

    def change_turn(self):
        self.valid_moves.clear()
        self.turn = WHITE if self.turn == BLACK else BLACK

    def pick_king(self, piece):
        threats = piece.threat_squares(self.board.squares)
        valid_moves = piece.get_valid_moves(self.board.squares)
        self.valid_moves = [move for move in valid_moves if move not in threats]

    def pick_piece(self, piece):
        valid_moves = piece.get_valid_moves(self.board.squares)
        pined_moves = piece.get_pined_moves(self.board.squares)
        if pined_moves:
            self.valid_moves = [move for move in valid_moves if move in pined_moves]
        else:
            self.valid_moves = valid_moves

    # added
    def is_checking(self, piece):
        #self.valid_moves = []
        valid_moves = piece.get_valid_moves(self.board.squares)
        for move in valid_moves:
            row, col = move
            square = self.board.squares[row][col]
            if square.has_piece() and square.piece.name == 'king' and square.piece.color != piece.color:
                return True
        return False

    

    def select(self, row, col):
        if self.selected:
            destenation = self.move(row, col)
            if not destenation:
                self.selected = None
                self.select(row, col)
        piece = self.board.squares[row][col].piece
        if piece and piece.color == self.turn:
            self.selected = piece
            if piece.name == 'king':
                self.pick_king(piece)
            else:
                self.pick_piece(piece)

            return True
        return False

    def update(self):
        self.create()
        self.draw_valid_moves(self.valid_moves)
        pygame.display.update()



