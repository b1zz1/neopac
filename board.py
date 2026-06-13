import pygame

import config as cfg


# Renders level matrix into the screen
def draw_board(lvl, color):
    num_1 = (cfg.HEIGHT - 50) // 32
    num_2 = cfg.WIDTH // 30

    # Iterates over level matrix
    for i in range(len(lvl)):
        for j in range(len(lvl[i])):
            if lvl[i][j] == 1:
                # Small dot
                pygame.draw.circle(cfg.screen, 'white', (j * num_2 + (0.5 * num_2), i * num_1 + (0.5 * num_1)), 4)
            if lvl[i][j] == 2:
                # Big dot
                pygame.draw.circle(cfg.screen, 'white', (j * num_2 + (0.5 * num_2), i * num_1 + (0.5 * num_1)), 10)
            if lvl[i][j] == 3:
                # Straight line (vertical)
                pygame.draw.line(cfg.screen, color, (j * num_2 + (0.5 * num_2), i * num_1), (j * num_2 + (0.5 * num_2), i * num_1 + num_1), 3)
            if lvl[i][j] == 4:
                # Straight line (horizontal)
                pygame.draw.line(cfg.screen, color, (j * num_2, i * num_1 + (0.5 * num_1)), (j * num_2 + num_2, i * num_1 + (0.5 * num_1)), 3)
            if lvl[i][j] == 5:
                # Arch (left -> bottom)
                pygame.draw.arc(cfg.screen, color, [(j * num_2 - (num_2 * 0.5)), (i * num_1 + (0.5 * num_1)), num_2, num_1], 0, cfg.PI / 2, 3)
            if lvl[i][j] == 6:
                # Arch (right -> bottom)
                pygame.draw.arc(cfg.screen, color, [(j * num_2 + (num_2 * 0.5)), (i * num_1 + (0.5 * num_1)), num_2, num_1], cfg.PI / 2, cfg.PI, 3)
            if lvl[i][j] == 7:
                # Arch (top -> right)
                pygame.draw.arc(cfg.screen, color, [(j * num_2 + (num_2 * 0.5)), (i * num_1 - (0.5 * num_1)), num_2, num_1], cfg.PI, 3 * cfg.PI / 2, 3)
            if lvl[i][j] == 8:
                # Arch (top -> left)
                pygame.draw.arc(cfg.screen, color, [(j * num_2 - (num_2 * 0.5)), (i * num_1 - (0.5 * num_1)), num_2, num_1], 3 * cfg.PI / 2, 2 * cfg.PI, 3)
            if lvl[i][j] == 9:
                # Gate (horizontal)
                pygame.draw.line(cfg.screen, 'white', (j * num_2, i * num_1 + (0.5 * num_1)), (j * num_2 + num_2, i * num_1 + (0.5 * num_1)), 3)
