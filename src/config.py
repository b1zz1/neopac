# Window constants
TILE_SIZE = 32                 # 32 pixels as in the original game
ROWS = 33                      # Vertical tiles
COLUMNS = 30                   # Horizontal tiles
WIDTH = COLUMNS * TILE_SIZE    # 30 * 32 = 960 pixels
HEIGHT = ROWS * TILE_SIZE + 50 # 33 * 32 + 50 = 1106 pixels

# Game constants
FPS = 60
AI_MODE = True
SKIN_PACK = 'simple'
game_over = False
game_won = False

# Player constants
FUDGE = 16
PLAYER_SPEED = 2

# Visuals & animations
player_frames = []
blinky_frames = []
ghost_spooked_frames = []
ghost_dead_frames = []

# Power up
power_up_active = False
power_up_counter = 0

# Ghosts
ghost_speed = 2
eaten_ghosts = [False, False, False, False]
alive_ghosts = [True, True, True, True]
