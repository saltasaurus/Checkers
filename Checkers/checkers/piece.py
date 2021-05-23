import pygame as pg
from .constants import BLUE, RED, WHITE, GRAY, SQUARE_SIZE, CROWN

# Checkers Piece characteristics
class Piece:
    PADDING = 10
    OUTLINE = 2

    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.king = False
        self.selected = False
        self.x = 0
        self.y = 0
        self.calc_pos()

    # Determine piece position on board
    def calc_pos(self):
        self.x = SQUARE_SIZE * self.col + SQUARE_SIZE // 2
        self.y = SQUARE_SIZE * self.row + SQUARE_SIZE // 2

    # Set the piece to a King
    def make_king(self):
        self.king = True

    # Draw piece on board
    def draw(self, win):
        radius = SQUARE_SIZE//2 - self.PADDING
        pg.draw.circle(win, self.color, (self.x, self.y), radius)
        pg.draw.circle(win, GRAY, (self.x, self.y), radius, 2)
        if self.king:
            win.blit(CROWN, (self.x - CROWN.get_width()//2, self.y - CROWN.get_height()//2))

    # Set piece's position
    def move(self, row, col):
        self.row = row
        self.col = col
        self.calc_pos()

    # Returns piece & color
    def __repr__(self):
        if self.color == RED:
            return "RED Piece"
        else:
            return "WHITE Piece"
