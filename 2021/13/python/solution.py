#!/usr/bin/env python3
# DEBUG : 1424 too high, 1417 too high

import logging
from pprint import pprint, pformat, PrettyPrinter
from string import ascii_letters
from sys import argv

# logging so that I can throw debug strings around without feeling bad
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)

bigprint = PrettyPrinter(width=320)


def load_input(filename):
    grid = []
    temp_point_list = []
    folds = []

    with open(filename) as input:
        for line in input:
            if len(line.split(',')) == 2:
                temp_point_list.append([int(n)
                                       for n in line.strip().split(',')])
            elif len(line.strip()) > 0:
                folds.append(line.strip())

    max_x = max(n[0] for n in temp_point_list)
    max_y = max(n[1] for n in temp_point_list)
    grid = [[0] * (max_x+1) for _ in range(max_y+1)]

    for point in temp_point_list:
        grid[point[1]][point[0]] = 1

    return grid, folds


def fold_grid(grid, fold_string):
    fold_axis = fold_string.split('=')[0][-1]
    fold_value = int(fold_string.split('=')[1])
    logger.debug(f"Fold Axis: {fold_axis} Fold Value: {fold_value}")

    # horizontal fold
    if fold_axis == 'y':
        top_half = grid[:fold_value]
        bottom_half = grid[(fold_value+1):]
        logger.debug("Top Half")
        logger.debug(pformat(top_half))
        logger.debug('')
        logger.debug("Bottom Half")
        logger.debug(pformat(bottom_half))
        logger.debug('')

        for y in range(0, len(bottom_half)):
            for x in range(0, len(bottom_half[y])):
                top_half[(
                    len(top_half)-1)-y][x] = top_half[(len(top_half)-1)-y][x] or bottom_half[y][x]
        return top_half

    if fold_axis == 'x':
        folded_grid = []

        for y in range(0, len(grid)):
            row = []
            for x in range(0, (len(grid[y])-1) - fold_value):
                row.append(
                    1 if (grid[y][x] == 1 or grid[y][(len(grid[y])-1)-x] == 1) else 0)
            folded_grid.append(row)
        return folded_grid


def print_ascii(grid):
    for y in range(0, len(grid)):
        row = ""
        for x in range(0, len(grid[y])):
            row += "#" if grid[y][x] == 1 else "."
        print(row)


if __name__ == '__main__':
    logger.setLevel(logging.INFO)
    # logger.setLevel(logging.DEBUG)
    filename = argv[1]

    grid, folds = load_input(filename)

    # logger.debug("First Fold")
    # logger.debug(folds[0])
    # fold = fold_grid(grid, folds[0])
    # logger.info(f"part1: {sum(sum(fold, []))}")

    for fold in folds:
        grid = fold_grid(grid, fold)
    print_ascii(grid)
