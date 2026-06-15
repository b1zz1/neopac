import pygame

import ai
import board
import config as cfg
import debug
import levels.level_1 as lvl_1
import player
import score
import ui

pygame.init()

DEBUG = True

screen = pygame.display.set_mode([cfg.WIDTH, cfg.HEIGHT])
timer = pygame.time.Clock()

font = pygame.font.Font("assets/fonts/Tiny5-Regular.ttf", cfg.TILE_SIZE)
font_lg = pygame.font.Font("assets/fonts/Tiny5-Regular.ttf", cfg.TILE_SIZE + 16)

level = lvl_1
counter = 0
startup_counter = 0
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
moving_allowed = False
turns_allowed = [False, False, False, False]

# Player score
player_score = 0
score_multiplier = 1.0

lives = 3

run = True
while run:
    timer.tick(cfg.FPS)

    # Delays game start
    if startup_counter < 280:
        startup_counter += 1

    if startup_counter < 180:
        moving_allowed = False
    elif not cfg.game_over and not cfg.game_won:
        moving_allowed = True

    # Big dots animation
    if counter < 19:
        counter += 1
        if counter > 3:
            flicker = False
    else:
        counter = 0
        flicker = True

    # Power-up
    if cfg.power_up_active and cfg.power_up_counter > 0:
        cfg.power_up_counter -= 1
    elif cfg.power_up_active and cfg.power_up_counter <= 0:
        cfg.power_up_active = False
        cfg.power_up_counter = 0
        cfg.alive_ghosts = [True, True, True, True]

    # User input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and (cfg.game_over or cfg.game_won):
                run = False

        if moving_allowed and not cfg.AI_MODE:
            buffered_direction = player.handle_input(event, buffered_direction, direction)

    # Core game logic
    player_center_x = player_position_x + (cfg.TILE_SIZE // 2)
    player_center_y = player_position_y + (cfg.TILE_SIZE // 2)

    player_score = score.handle_collisions(level.board, player_score, score_multiplier, player_position_x, player_center_x, player_center_y)

    # Update valid turning areas in real time
    turns_allowed = player.handle_collision(player_center_x, player_center_y, direction, level.board)

    # AI controller
    if moving_allowed and cfg.AI_MODE:
        if player_position_x % cfg.TILE_SIZE == 0 and player_position_y % cfg.TILE_SIZE == 0:
            grid_x = player_position_x // cfg.TILE_SIZE
            grid_y = player_position_y // cfg.TILE_SIZE

            target = ai.clean_a_star(grid_x, grid_y, level.board)
            buffered_direction = ai.get_direction(grid_x, grid_y, target)

    # Optimize grid navigation & process actual physical movement
    direction, player_position_x, player_position_y = player.handle_direction(direction, buffered_direction, turns_allowed, player_position_x, player_position_y)
    # Move the player to valid directions & update current position
    if moving_allowed:
        player_position_x, player_position_y = player.handle_movement(player_position_x, player_position_y, direction, turns_allowed)

    # Render graphics
    screen.fill('black')
    board.draw(screen, level.board, level.color, flicker)
    ui.draw_score(screen, font, player_score)
    ui.draw_lives(screen, lives)
    player.draw(screen, player_position_x, player_position_y, counter, direction)

    if startup_counter < 280:
        ui.draw_startup_countdown(screen, font_lg, startup_counter)

    if cfg.game_over:
        moving_allowed = False
        ui.draw_game_over(screen, font_lg)

    if cfg.game_won:
        moving_allowed = False
        ui.draw_game_won(screen, font_lg)

    if DEBUG:
        debug.draw_player_fudge(screen, direction, player_center_x, player_center_y)
        debug.draw_power_up_indicator(screen)

    # Teleport players passing through the hatches
    player_position_x = board.handle_side_hatches(player_position_x, player_center_x)

    pygame.display.flip()
pygame.quit()
