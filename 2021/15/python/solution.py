#!/usr/bin/env python3

import logging
from sys import argv


# logging so that I can throw debug strings around without feeling bad
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)


def load_input(filename):
    grid = []

    with open(filename) as input:
        for line in input:
            grid.append([int(n) for n in line.strip()])

    return grid


def lowest_risk_path(grid, source=(0, 0)):
    dist = {source: 0}
    queue = []

    for y in range(0, len(grid)):
        for x in range(0, len(grid[y])):
            if (x, y) != source:
                dist[(x, y)] = grid[y][x]
            queue.append((x, y))


def get_neighbors(point, grid):
    x, y = point
    nlist = []

    # # modification list
    mod_list = [
        (0, 1),  # north
        (0, -1),  # south
        (1, 0),  # east
        (-1, 0)  # west
    ]

    for m in mod_list:
        mx = x + m[0]
        my = y + m[1]

        if 0 <= mx < len(grid[y]) and 0 <= my < len(grid) and grid[my][mx]:
            nlist.append([mx, my])

    return nlist


if __name__ == '__main__':
    filename = argv[1]

    grid = load_input(filename)
