'''
This is where I stop looking at a tutorial and start my research.
The idea is to implement an utility-based agent using A* to move through the map.
While the first implementation will focus on collecting dots, subsequent work will add 'ghost avoiding' capabilities.
'''
import heapq

import config as cfg


# Heuristic
def get_manhattan_distance(start_x, start_y, target_x, target_y):
    ''' Calculates total horizontal and vertical distance between two nodes. '''
    return abs(start_x - target_x) + abs(start_y - target_y)


def find_nearest_pellet(pos_x, pos_y, lvl):
    ''' Search for the nearest pellet (big & small). '''
    closest_pellet = None
    min_distance = float('inf')

    for row in range(cfg.ROWS):
        for col in range(cfg.COLUMNS):
            if lvl[row][col] in [1, 2]:
                distance = get_manhattan_distance(pos_x, pos_y, col, row)
                if distance < min_distance:
                    min_distance = distance
                    closest_pellet = col, row

    return closest_pellet


def clean_a_star(pos_x, pos_y, lvl):
    # Destination
    target = find_nearest_pellet(pos_x, pos_y, lvl)

    if not target:
        return (pos_x, pos_y)

    tgt_x, tgt_y = target

    # Priority queue
    initial_h = get_manhattan_distance(pos_x, pos_y, tgt_x, tgt_y)
    open_set = [(initial_h, 0, pos_x, pos_y, [])]

    visited = set()

    # While there's tiles to evaluate
    while open_set:
        # Pull out the tile with the lowest total f_score
        f, g, cx, cy, path = heapq.heappop(open_set)

        # Best path found!
        if (cx, cy) == (tgt_x, tgt_y):
            return path[0] if path else (cx, cy)

        visited.add((cx, cy))

        # Neighbor inspection
        directions = [(1, 0), (-1, 0), (0, -1), (0, 1)] # Right, Left, Up, Down

        for dx, dy in directions:
            nx = cx + dx
            ny = cy + dy

            # Neightbor is inside boundary limits
            if 0 <= nx < cfg.COLUMNS and 0 <= ny < cfg.ROWS:
                if lvl[ny][nx] not in [3, 4, 5, 6, 7, 8, 9] and (nx, ny) not in visited:
                    # Neightbor is 1 tile away from start
                    next_g = g +  1
                    next_h = get_manhattan_distance(nx, ny, tgt_x, tgt_y)
                    next_f = next_g + next_h

                    # Record the path taken to reach this specific neighbor node
                    next_path = path + [(nx, ny)]

                    # Push neighbor into priority queue to be sorted automatically
                    heapq.heappush(open_set, (next_f, next_g, nx, ny, next_path))

    return (pos_x, pos_y) # Fallback


def get_direction(pos_x, pos_y, next_tile):
    """
    Convert next target grid tile into direction layout.
    """
    print(f'next_tile = {next_tile}')
    nx, ny = next_tile
    dx = nx - pos_x
    dy = ny - pos_y

    if dx == 1:
        return 0  # Right
    if dx == -1:
        return 1  # Left
    if dy == -1:
        return 2  # Up
    if dy == 1:
        return 3  # Down

    return 0
