import math

import pygame

import config as cfg


def draw(screen, lvl, color, flicker):
    '''
    Renders level matrix into the screen
    '''
    tile = cfg.TILE_SIZE

    # Iterates over level matrix
    for i in range(len(lvl)):
        for j in range(len(lvl[i])):
            # Pre-calculate the pixel coordinates of the current tile's top-left corner
            x = j * tile
            y = i * tile

            if lvl[i][j] == 1:
                # Small dot
                pygame.draw.circle(screen, 'white', (x + (0.5 * tile), y + (0.5 * tile)), 4)
            if lvl[i][j] == 2 and not flicker:
                # Big dot
                pygame.draw.circle(screen, 'white', (x + (0.5 * tile), y + (0.5 * tile)), 10)
            if lvl[i][j] == 3:
                # Straight line (vertical)
                pygame.draw.line(screen, color, (x + (0.5 * tile), y), (x + (0.5 * tile), y + tile), 3)
            if lvl[i][j] == 4:
                # Straight line (horizontal)
                pygame.draw.line(screen, color, (x, y + (0.5 * tile)), (x + tile, y + (0.5 * tile)), 3)
            if lvl[i][j] == 5:
                # Arch (left -> bottom)
                pygame.draw.arc(screen, color, [(x - (tile * 0.5)), (y + (0.5 * tile)), tile, tile], 0, math.pi / 2, 3)
            if lvl[i][j] == 6:
                # Arch (right -> bottom)
                pygame.draw.arc(screen, color, [(x + (tile * 0.5)), (y + (0.5 * tile)), tile, tile], math.pi / 2, math.pi, 3)
            if lvl[i][j] == 7:
                # Arch (top -> right)
                pygame.draw.arc(screen, color, [(x + (tile * 0.5)), (y - (0.5 * tile)), tile, tile], math.pi, 3 * math.pi / 2, 3)
            if lvl[i][j] == 8:
                # Arch (top -> left)
                pygame.draw.arc(screen, color, [(x - (tile * 0.5)), (y - (0.5 * tile)), tile, tile], 3 * math.pi / 2, 2 * math.pi, 3)
            if lvl[i][j] == 9:
                # Gate (horizontal)
                pygame.draw.line(screen, 'white', (x, y + (0.5 * tile)), (x + tile, y + (0.5 * tile)), 3)


def handle_side_hatches(pos_x, center_x):
    '''
    Teleport entities passing trought the hatches
    '''
    if center_x > 970:
        pos_x = -20
    elif center_x < -24:
        pos_x = 950

    return pos_x
