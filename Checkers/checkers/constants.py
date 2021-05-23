import pygame as pg

FPS = 60

WIDTH, HEIGHT = 800,800
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH//COLS

# RGB color codes
RED = (255, 0 ,0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GRAY = (128, 128, 128)

CROWN_PATH = r'assets/crown.png'
CROWN = pg.transform.scale(pg.image.load(CROWN_PATH), (45, 35))


