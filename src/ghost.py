import pygame

import config as cfg

blinky = pygame.transform.scale(pygame.image.load(f'assets/entities/ghost/blinky_{cfg.SKIN_PACK}_0.png'), (32, 32))
spooked = pygame.transform.scale(pygame.image.load(f'assets/entities/ghost/spooked_{cfg.SKIN_PACK}_0.png'), (32, 32))
dead = pygame.transform.scale(pygame.image.load(f'assets/entities/ghost/dead_{cfg.SKIN_PACK}_0.png'), (32, 32))

class Ghost:
    def __init__(self, position_x, position_y, target, speed, direction, dead, box, id, screen):
        self.pos_x = position_x
        self.pos_y = position_y
        self.center_x = self.pos_x + (cfg.TILE_SIZE // 2)
        self.center_y = self.pos_y + (cfg.TILE_SIZE // 2)
        self.target = target
        self.speed = speed
        self.dir = direction
        self.dead = dead
        self.id = id
        self.screen = screen
        self.turns, self.box = self.check_collisions()
        self.rect = self.draw()


    def draw(self):
        if (not cfg.power_up_active and not self.dead) or (cfg.eaten_ghosts[self.id] and cfg.power_up_active and not self.dead):
            self.screen.blit(blinky, (self.pos_x, self.pos_y))
        elif cfg.power_up_active and not self.dead and not cfg.eaten_ghosts[self.id]:
            self.screen.blit(spooked, (self.pos_x, self.pos_y))
        elif True:
            self.screen.blit(dead, (self.pos_x, self.pos_y))

        rect = pygame.rect.Rect((self.center_x - 16, self.center_y - 16), (32, 32))
        return rect


    def check_collisions(self):
        self.turns = [False, False, False, False]
        self.box = True

        return self.turns, self.box
