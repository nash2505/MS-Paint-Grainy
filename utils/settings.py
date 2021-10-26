import pygame
pygame.init()
pygame.font.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 255, 0)
GREEN = (0, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 128, 0)
VIOLET = (238,130,238)
INDIGO = (75,0,130)
BROWN = (165,42,42)
PINK = (255,20,147)

FPS = 240

WIDTH, HEIGHT = 600, 700

ROWS = COLS = 100

TOOLBAR_HEIGHT = HEIGHT - WIDTH

PIXEL_SIZE = WIDTH // COLS

BG_COLOR = WHITE

DRAW_GRID_LINES = False


def get_font(size):
    return pygame.font.SysFont("comicsans", size)
