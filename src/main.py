import pygame

import board
import config as cfg
import debug
import levels.level_1 as lvl_1
import player
import score

pygame.init()

DEBUG = False

screen = pygame.display.set_mode([cfg.WIDTH, cfg.HEIGHT])
timer = pygame.time.Clock()
font = pygame.font.Font(None, 20)  # TODO: Improve font choice

level = lvl_1
counter = 0
flicker = False

# Player starting position
player_grid_x = 14  # Column 14
player_grid_y = 24  # Row 24
# Player position
player_position_x = player_grid_x * cfg.TILE_SIZE
player_position_y = player_grid_y * cfg.TILE_SIZE
# Player direction
direction = 0
buffered_direction = 0
turns_allowed = [False, False, False, False]

# Player score
player_score = 0
score_multiplier = 1.0


run = True
while run:
    timer.tick(cfg.FPS)

    # Counter & animations
    if counter < 19:
        counter += 1
        if counter > 3:
            flicker = False
    else:
        counter = 0
        flicker = True

    # User input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        buffered_direction = player.handle_input(event, buffered_direction, direction)

    # Core game logic
    player_center_x = player_position_x + (cfg.TILE_SIZE // 2)
    player_center_y = player_position_y + (cfg.TILE_SIZE // 2)

    player_score = score.handle_collisions(level.board, player_score, score_multiplier, player_position_x, player_center_x, player_center_y)

    # Update valid turning areas in real time
    turns_allowed = player.handle_collision(player_center_x, player_center_y, direction, level.board)
    # Optimize grid navigation for smoother UX
    direction, player_position_x, player_position_y = player.handle_direction(direction, buffered_direction, turns_allowed, player_position_x, player_position_y)
    # Move the player to valid directions & update current position
    player_position_x, player_position_y = player.handle_movement(player_position_x, player_position_y, direction, turns_allowed)

    # Render graphics
    screen.fill('black')
    board.draw(screen, level.board, level.color, flicker)

    player.draw(screen, player_position_x, player_position_y, counter, direction)

    if DEBUG:
        debug.draw_player_fudge(screen, direction, player_center_x, player_center_y)

    # Teleport players passing through the hatches
    player_position_x = board.handle_side_hatches(player_position_x, player_center_x)

    pygame.display.flip()
pygame.quit()
