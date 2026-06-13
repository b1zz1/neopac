import pygame

import config as cfg
from board import draw_board
from levels.level_1 import board

pygame.init()

timer = pygame.time.Clock()
fps = 60
font = pygame.font.Font(None, 20)  # Improve font choice
level = board

run = True
while run:
    timer.tick(fps)
    cfg.screen.fill("black")
    draw_board(level)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.flip()
pygame.quit()
