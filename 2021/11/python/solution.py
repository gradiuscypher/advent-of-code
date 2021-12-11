#!/usr/bin/env python3

"""
each step:
- energy of each octopus increases by 1
- anyone with energy greater than 9 flashes (energy == 9, otherwise he's already flashed)
- all adjacent foxes increase by 1, including diagonals, anything greater than 9 also flashes, etc
- any octopus that flashed has its energy set to 0 (dont have to track state, just change anything higher than 9 to 0)
"""

from pprint import pprint
from sys import argv


def load_grid(filename):
    grid = []

    with open(filename) as input:
        for line in input:
            grid.append([int(n) for n in line.strip()])
    return grid


def increase_energy(grid):
    for y in range(0, len(grid)):
        for x in range(0, len(grid[y])):
            grid[y][x] += 1


def check_flash(grid, already_flashed):
    should_flash = []

    for y in range(0, len(grid)):
        for x in range(0, len(grid[y])):
            if grid[y][x] > 9 and [x, y] not in already_flashed:
                should_flash.append([x, y])
                already_flashed.append([x, y])
    return should_flash


def flash_loc(loc, grid):
    modifiers = [
        (0, 1),  # north
        (1, 1),  # northeast
        (1, 0),  # east
        (1, -1),  # southeast
        (0, -1),  # south
        (-1, -1),  # southwest
        (-1, 0),  # west
        (-1, 1)  # northwest
    ]

    for m in modifiers:
        mx = loc[0] + m[0]
        my = loc[1] + m[1]

        if 0 <= my < len(grid) and 0 <= mx < len(grid[my]):
            grid[my][mx] += 1


def reset_flashed(grid):
    for y in range(0, len(grid)):
        for x in range(0, len(grid[y])):
            if grid[y][x] > 9:
                grid[y][x] = 0


def is_grid_sync(grid):
    sync = True
    for y in range(0, len(grid)):
        for x in range(0, len(grid[y])):
            if grid[y][x] != 0:
                sync = False
    return sync


if __name__ == '__main__':
    filename = argv[1]

    grid = load_grid(filename)
    total_flashes = 0

    for x in range(0, 2000):
        if is_grid_sync(grid):
            print("part2 ============ ", x)
            break

        print(f"Step: {x}")
        first_flash = True
        increase_energy(grid)
        already_flashed = []
        should_flash = check_flash(grid, already_flashed)

        while should_flash:
            for loc in should_flash:
                flash_loc(loc, grid)
                total_flashes += 1
            should_flash = check_flash(grid, already_flashed)
        reset_flashed(grid)

    print("part1", total_flashes)
