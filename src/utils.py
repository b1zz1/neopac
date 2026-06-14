import config as cfg


def is_near_tile_center(pos):
    return 12 <= pos % cfg.TILE_SIZE <= 20
