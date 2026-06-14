import config as cfg

tile = cfg.TILE_SIZE

def handle_collisions(lvl, score, multiplier, pos_x, center_x, center_y):
    if 0 < pos_x < 970:
        # If player center touches small dot, clear the space
        if lvl[center_y // tile][center_x // tile] == 1:
            lvl[center_y // tile][center_x // tile] = 0
            score += 10 * multiplier
        # If player center touches big dot, clear the space
        if lvl[center_y // tile][center_x // tile] == 2:
            lvl[center_y // tile][center_x // tile] = 0
            score += 50 * multiplier
            cfg.power_up_active = True
            cfg.power_up_counter = 600

    return score
