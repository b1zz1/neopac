import pygame

import config as cfg
from utils import is_near_tile_center

tile = cfg.TILE_SIZE
fudge = cfg.FUDGE

for i in range(0, 4):
    cfg.player_frames.append(pygame.transform.scale(pygame.image.load(f'assets/entities/player/{cfg.SKIN_PACK}_{i}.png'), (32, 32)))


def draw(screen, pos_x, pos_y, counter, direction):
    '''
    Draws player character at parameter position
    '''
    if direction == 0:
        # RIGHT
        screen.blit(cfg.player_frames[counter // 5], (pos_x, pos_y))
    elif direction == 1:
        # LEFT
        screen.blit(pygame.transform.flip(cfg.player_frames[counter // 5], True, False), (pos_x, pos_y))
    elif direction == 2:
        # UP
        screen.blit(pygame.transform.rotate(cfg.player_frames[counter // 5], 90), (pos_x, pos_y))
    elif direction == 3:
        # DOWN
        screen.blit(pygame.transform.rotate(cfg.player_frames[counter // 5], -90), (pos_x, pos_y))


def handle_input(event, buffered_direction, direction):
    '''
    Recognizes keyboard input and changes movement direction accordingly.
    Simulates a joystick!
    '''
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RIGHT:
            buffered_direction = 0
        if event.key == pygame.K_LEFT:
            buffered_direction = 1
        if  event.key == pygame.K_UP:
            buffered_direction = 2
        if event.key == pygame.K_DOWN:
            buffered_direction = 3

    if event.type == pygame.KEYUP:
        if event.key == pygame.K_RIGHT and buffered_direction == 0:
            buffered_direction = direction
        if event.key == pygame.K_LEFT and buffered_direction == 1:
            buffered_direction = direction
        if  event.key == pygame.K_UP and buffered_direction == 2:
            buffered_direction = direction
        if event.key == pygame.K_DOWN and buffered_direction == 3:
            buffered_direction = direction

    return buffered_direction


def handle_collision(center_x, center_y, direction, lvl):
    turns = [False, False, False, False]
    fudge = cfg.FUDGE

    grid_x = center_x // tile
    grid_y = center_y // tile

    # Can always turn sideways in a corridor
    if grid_x >= 29 or grid_x < 0:
        turns[0] = True
        turns[1] = True
        return turns

    # Allows sideways movement
    if direction == 0:
        if lvl[grid_y][(center_x + fudge) // tile] < 3:
            turns[0] = True
    elif direction == 1:
        if lvl[grid_y][(center_x - fudge) // tile] < 3:
            turns[1] = True
    elif direction == 2:
        if lvl[(center_y - fudge) // tile][grid_x] < 3:
            turns[2] = True
    elif direction == 3:
        if lvl[(center_y + fudge) // tile][grid_x] < 3:
            turns[3] = True

    # BACKWARDS path detection
    if direction == 0:
        turns[1] = True # Moving Right -> Can always turn Left
    elif direction == 1:
        turns[0] = True # Moving Left -> Can always turn Right
    elif direction == 2:
        turns[3] = True # Moving Up -> Can always turn Down
    elif direction == 3:
        turns[2] = True # Moving Down -> Can always turn Up

    # UP and DOWN path detection
    if direction == 0 or direction == 1:
        if lvl[grid_y - 1][grid_x] < 3:
            turns[2] = True # Path UP exists
        if lvl[grid_y + 1][grid_x] < 3:
            turns[3] = True # Path DOWN exists

        if not is_near_tile_center(center_x):
            turns[2] = False
            turns[3] = False

    # RIGHT and LEFT path detection
    elif direction == 2 or direction == 3:
        if lvl[grid_y][grid_x + 1] < 3:
            turns[0] = True # Path RIGHT exists
        if lvl[grid_y][grid_x - 1] < 3:
            turns[1] = True # Path LEFT exists

        if not is_near_tile_center(center_y):
            turns[0] = False
            turns[1] = False

    return turns


def handle_direction(direction, buffered_dir, turns_allowed, pos_x, pos_y):
        # Check if buffered direction is allowed
        if turns_allowed[buffered_dir] and buffered_dir != direction:
            if buffered_dir != direction:
                # Turning UP or DOWN? Snap X to the center of the column
                if buffered_dir == 2 or buffered_dir == 3:
                    grid_x = (pos_x + tile // 2) // tile
                    pos_x = grid_x * tile
                # Turning RIGHT or LEFT? Snap Y to the center of the row
                elif buffered_dir == 0 or buffered_dir == 1:
                    grid_y = (pos_y + tile // 2) // tile
                    pos_y = grid_y * tile

            return buffered_dir, pos_x, pos_y

        # Turn invalid, moving frontwards allowed
        if turns_allowed[direction]:
            return direction, pos_x, pos_y

        # Turn invalid, moving frontwards blocked
        return direction, pos_x, pos_y


def handle_movement(pos_x, pos_y, direction, turns_allowed):
    '''
    Handles actual player movement...
    Kinda obvious I suppose.
    '''
    if direction == 0 and turns_allowed[0]:
        pos_x += cfg.PLAYER_SPEED
    elif direction == 1 and turns_allowed[1]:
        pos_x -= cfg.PLAYER_SPEED

    if direction == 2 and turns_allowed[2]:
        pos_y -= cfg.PLAYER_SPEED
    elif direction == 3 and turns_allowed[3]:
        pos_y += cfg.PLAYER_SPEED

    return pos_x, pos_y
