import pygame

import config as cfg
import levels.level_1 as lvl_1
from board import draw_board
from player import draw_player

pygame.init()

FPS = 60
font = pygame.font.Font(None, 20)  # Improve font choice
level = lvl_1

timer = pygame.time.Clock()
counter = 0

run = True
while run:
    timer.tick(FPS)
    if counter < 19:
        counter += 1
    else:
        counter = 0

    cfg.screen.fill('black')

    draw_board(level.board, level.color)
    draw_player(counter)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.flip()
pygame.quit()
