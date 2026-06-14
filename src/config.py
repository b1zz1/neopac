import pygame

# Window constants
TILE_SIZE = 32                   # 8x8 as in the original game
ROWS = 33                        # Vertical tiles
COLUMNS = 30                     # Horizontal tiles
WIDTH = COLUMNS * TILE_SIZE      # 30 * 32 = 960 pixels
HEIGHT = (ROWS * TILE_SIZE) + 50 # (33 * 32) + 50 = 1106 pixels

# Game constants
FPS = 60

# Player constants
FUDGE = 15
PLAYER_SPEED = 2

screen = pygame.display.set_mode([WIDTH, HEIGHT])
timer = pygame.time.Clock()
