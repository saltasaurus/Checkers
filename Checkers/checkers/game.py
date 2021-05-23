import pygame as pg
from .constants import RED, WHITE, BLUE, SQUARE_SIZE
from checkers.board import Board

# The rules and actions of Checkers
class Game:
    def __init__(self, win):
        self._init()
        self.win = win

    # Draw board with updated state
    def update(self):
        self.board.draw(self.win)
        self.draw_valid_moves(self.valid_moves)
        pg.display.update()

    # Set piece, board and turn to default
    def _init(self):
        self.selected = None        
        self.board = Board()
        self.turn = RED
        self.valid_moves = {}

    # Select winner
    def winner(self):
        return self.board.winner()

    # Show winner
    def draw_win(self, winner):
        self.board.draw_win(winner)

    # Reset game to defaults
    def reset(self):
        self._init()

    # Decide which piece is clicked
    def select(self, row, col):
        if self.selected:
            result = self._move(row, col)
            if not result:
                self.selected = None
                self.select(row, col)

        piece = self.board.get_piece(row, col)
        if piece != 0 and piece.color == self.turn:
            self.selected = piece
            self.valid_moves = self.board.get_valid_moves(piece)
            return True
        
        return False

    # Draw piece in new position
    def _move(self, row, col):
        piece = self.board.get_piece(row, col)
        if self.selected and piece == 0 and (row, col) in self.valid_moves:
            self.board.move(self.selected, row, col)
            skipped = self.valid_moves[(row,col)]
            if skipped:
                self.board.remove(skipped)
            self.change_turn()
        else:
            return False
        
        return True

    # Show available moves for selected piece
    def draw_valid_moves(self, moves):
        for move in moves:
            row, col = move
            pg.draw.circle(self.win, BLUE, (col * SQUARE_SIZE + SQUARE_SIZE//2, row * SQUARE_SIZE + SQUARE_SIZE//2), 15)

    # Switch which color can move
    def change_turn(self):
        self.valid_moves = {}
        if self.turn == RED:
            self.turn = WHITE
        else:
            self.turn = RED
