import pygame

import config as cfg


def draw_player_fudge(screen, direction, center_x, center_y):
    '''
    DYNAMIC FUDGE VISUALIZER
    '''
    fudge_target_x = center_x
    fudge_target_y = center_y

    # Extend target point based on the current direction
    if direction == 0:    # RIGHT
        fudge_target_x += cfg.FUDGE
    elif direction == 1:  # LEFT
        fudge_target_x -= cfg.FUDGE
    elif direction == 2:  # UP
        fudge_target_y -= cfg.FUDGE
    elif direction == 3:  # DOWN
        fudge_target_y += cfg.FUDGE

    # Green line showing the look-ahead fudge vector
    pygame.draw.line(screen, (0, 255, 0), (center_x, center_y), (fudge_target_x, fudge_target_y), 3)
    # Red dot at the tip of the fudge line
    pygame.draw.circle(screen, (255, 0, 0), (int(fudge_target_x), int(fudge_target_y)), 4)
