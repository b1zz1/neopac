import pygame

import config as cfg

tile = cfg.TILE_SIZE
window_height = cfg.HEIGHT
window_width = cfg.WIDTH


def draw_score(screen, font, score):
    score_txt = font.render(f'Score: {score}', True, 'white')
    screen.blit(score_txt, (tile / 2, window_height - (tile * 1.5)))


def draw_lives(screen, lives):
    for i in range(lives):
        screen.blit(pygame.transform.scale(cfg.player_frames[0], (tile, tile)), (window_width - (tile * 1.5) * (i + 1), window_height - (tile * 1.5)))


def draw_startup_countdown(screen, font, count):
    text = None

    if count < 180:
        countdown = (180 - count) // 60 + 1
        text = font.render(str(countdown), True, 'white')
    elif 180 <= count < 280:
        if (count // 10) % 2 == 0:
            text = font.render('START!!!', True, 'white')
        else:
            text = font.render('', True, 'white')

    if text:
        rect = text.get_rect()
        rect.center = (window_width // 2, window_height - tile)
        screen.blit(text, rect)

# TODO: Improve game over and game won messages!
def draw_game_over(screen, font):
    text = font.render('GAME OVER!\nPress SPACE BAR to quit.', True, 'red')

    pygame.draw.rect(screen, 'white', [50, 200, 800, 300], 0, 10)
    pygame.draw.rect(screen, 'dark gray', [70, 220, 760, 260], 0, 10)

    screen.blit(text, (100, 300))

def draw_game_won(screen, font):
    text = font.render('YOU WON!\nPress SPACE BAR to quit.', True, 'blue')

    pygame.draw.rect(screen, 'white', [50, 200, 800, 300], 0, 10)
    pygame.draw.rect(screen, 'dark gray', [70, 220, 760, 260], 0, 10)

    screen.blit(text, (100, 300))
