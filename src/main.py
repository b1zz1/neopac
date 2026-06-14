import pygame

import board
import config as cfg
import debug
import levels.level_1 as lvl_1
import player

pygame.init()

DEBUG = False
FONT = pygame.font.Font(None, 20)  # TODO: Improve font choice
level = lvl_1
counter = 0
flicker = False

# Player tarting position
player_grid_x = 14  # Column 14
player_grid_y = 24  # Row 24
# Player position
player_position_x = player_grid_x * cfg.TILE_SIZE
player_position_y = player_grid_y * cfg.TILE_SIZE
# Player direction
direction = 0
buffered_direction = 0
turns_allowed = [False, False, False, False]

run = True
while run:
    cfg.timer.tick(cfg.FPS)

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

    # Update valid turning areas in real time
    turns_allowed = player.handle_collision(player_center_x, player_center_y, direction, level.board)
    # Optimize grid navigation for smoother UX
    direction, player_position_x, player_position_y = player.handle_direction(direction, buffered_direction, turns_allowed, player_position_x, player_position_y)
    # Move the player to valid directions & update current position
    player_position_x, player_position_y = player.handle_movement(player_position_x, player_position_y, direction, turns_allowed)

    # Render graphics
    cfg.screen.fill('black')
    board.draw(level.board, level.color, flicker)

    player.draw(player_position_x, player_position_y, counter, direction)

    if DEBUG:
        debug.draw_player_fudge(direction, player_center_x, player_center_y)

    if player_center_x > 970:
        player_position_x = -20
    elif player_center_x < -24:
        player_position_x = 950
    pygame.display.flip()
pygame.quit()
