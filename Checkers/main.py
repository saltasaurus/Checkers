import pygame as pg
from checkers.constants import *
from checkers.game import Game

WIN = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption('Checkers')

# Returns x,y of mouse
def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

# Play Checkers!
def main():
    run = True
    clock = pg.time.Clock()
    game = Game(WIN)

    # Game loop
    while run:
        clock.tick(FPS)

        # Check if there is a winner
        if game.winner() != None:
            game.draw_win(game.winner())
            print("Winner is ", game.winner())
            run = False

        # Check for events
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False

            # Get mouse click
            if event.type == pg.MOUSEBUTTONDOWN:
                pos = pg.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                game.select(row, col)

        # Update game state
        game.update()
    

    # Close pygame
    pg.quit()

### Start Checkers ###
main()