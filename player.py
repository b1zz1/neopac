import pygame

import config as cfg

PLAYER_X = 450
PLAYER_Y = 663
direction = 0

player_frames = []
skin = 'simple'

for i in range(0, 4):
    player_frames.append(pygame.transform.scale(pygame.image.load(f'assets/entities/player/{skin}_{i}.png'), (45, 45)))


def draw_player(counter):
    if direction == 0:
        # RIGHT
        cfg.screen.blit(player_frames[counter // 5], (PLAYER_X, PLAYER_Y))
    elif direction == 1:
        # LEFT
        cfg.screen.blit(pygame.transform.flip(player_frames[counter // 5], True, False), (PLAYER_X, PLAYER_Y))
    elif direction == 2:
        # UP
        cfg.screen.blit(pygame.transform.rotate(player_frames[counter // 5], 90), (PLAYER_X, PLAYER_Y))
    elif direction == 3:
        # DOWN
        cfg.screen.blit(pygame.transform.rotate(player_frames[counter // 5], -90), (PLAYER_X, PLAYER_Y))
