#!/usr/bin/env python3
# higher than 552, lower than 1898(?)

from functools import reduce
import operator
from pprint import pprint
from sys import argv


def parse_map(filename):
    map_arr = []
    with open(filename) as input:
        for line in input:
            map_arr.append([int(n) for n in line.strip()])
    return map_arr


def find_low_points(map_arr):
    low_points = []

    for y in range(0, len(map_arr)):
        for x in range(0, len(map_arr[y])):
            # iterate over every point, if the point is in already_lower, ignore it completely
            # otherwise figure out what point is lowest and add it to the low_points list
            low_point = [x, y]
            low_val = map_arr[y][x]

            # # modification list
            mod_list = [
                (0, 1),  # north
                (0, -1),  # south
                (1, 0),  # east
                (-1, 0)  # west
            ]

            is_lower = True
            for m in mod_list:
                mx = x + m[0]
                my = y + m[1]
                if 0 <= mx < len(map_arr[y]) and 0 <= my < len(map_arr) and map_arr[my][mx] <= low_val:
                    is_lower = False

            if is_lower:
                low_points.append(low_point)

    return low_points


def get_neighbors(point, map_arr):
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

        if 0 <= mx < len(map_arr[y]) and 0 <= my < len(map_arr) and map_arr[my][mx] and map_arr[my][mx] != 9:
            nlist.append([mx, my])

    return nlist


def find_basin(low_point, map_arr):
    basin = []
    queue = []

    basin.append(low_point)
    queue.append(low_point)

    while queue:
        p = queue.pop(0)
        neighbors = get_neighbors(p, map_arr)

        for n in neighbors:
            if n not in basin:
                basin.append(n)
                queue.append(n)

    return basin


if __name__ == '__main__':
    filename = argv[1]

    map_arr = parse_map(filename)
    low_points = find_low_points(map_arr)

    val = 0
    for point in low_points:
        val += map_arr[point[1]][point[0]] + 1

    print(f"part1: {val}")

    basins = []
    for p in low_points:
        basins.append(len(find_basin(p, map_arr)))
    basins.sort()
    tally = reduce(operator.mul, basins[-3:], 1)
    print(f"part2: {tally}")
