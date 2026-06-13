import pygame

import config as cfg
import levels.level_1 as lvl_1
from board import draw_board

pygame.init()

timer = pygame.time.Clock()
fps = 60
font = pygame.font.Font(None, 20)  # Improve font choice
level = lvl_1

run = True
while run:
    timer.tick(fps)
    cfg.screen.fill('black')
    draw_board(level.board, level.color)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.flip()
pygame.quit()
