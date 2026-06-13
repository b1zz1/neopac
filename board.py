import pygame

import config as cfg


# Renders level matrix into the screen
def draw_board(lvl):
    num_1 = (cfg.HEIGHT - 50) // 32
    num_2 = cfg.WIDTH // 30

    # Iterates over level matrix
    for i in range(len(lvl)):
        for j in range(len(lvl[i])):
            if lvl[i][j] == 1:
                # Small dot
                pygame.draw.circle(cfg.screen, "white", (j * num_2 + (0.5 * num_2), i * num_1 + (0.5 * num_1)), 4)
            if lvl[i][j] == 2:
                # Big dot
                pygame.draw.circle(cfg.screen, "white", (j * num_2 + (0.5 * num_2), i * num_1 + (0.5 * num_1)), 10)
