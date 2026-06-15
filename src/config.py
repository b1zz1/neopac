# Window constants
TILE_SIZE = 32                 # 32 pixels as in the original game
ROWS = 33                      # Vertical tiles
COLUMNS = 30                   # Horizontal tiles
WIDTH = COLUMNS * TILE_SIZE    # 30 * 32 = 960 pixels
HEIGHT = ROWS * TILE_SIZE + 50 # 33 * 32 + 50 = 1106 pixels

# Game constants
FPS = 60
AI_MODE = False
game_over = False
game_won = False

# Player constants
FUDGE = 16
PLAYER_SPEED = 2

# Player
player_frames = []

# Power up
power_up_active = False
power_up_counter = 0

# Ghosts
alive_ghosts = [True, True, True, True]
