#!/usr/bin/env python3
# higher than 552, lower than 1898(?)

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
    already_lower = []

    for y in range(0, len(map_arr)):
        for x in range(0, len(map_arr[y])):
            # check spots around this point if it or its neighboors are considered a low point, if so, compare and determine who's lower
            low_point = [x, y]
            low_val = map_arr[y][x]

            if not low_point in low_points and not low_point in already_lower:
                low_points.append(low_point)

            # modification list
            mod_list = [
                (0, 1),  # north
                (0, -1),  # south
                (1, 0),  # east
                (-1, 0)  # west
            ]

            for m in mod_list:
                mx = x + m[0]
                my = y + m[1]
                if 0 <= mx < len(map_arr[y]) and 0 <= my < len(map_arr) and map_arr[my][mx] < low_val:
                    if low_point in low_points:
                        low_points.remove(low_point)
                        already_lower.append(low_point)

                    low_point = [mx, my]
                    low_val = map_arr[my][mx]

                    if low_point not in already_lower:
                        low_points.append(low_point)

    return low_points


if __name__ == '__main__':
    filename = argv[1]

    map_arr = parse_map(filename)
    low_points = find_low_points(map_arr)
    print(low_points)

    val = 0
    for point in low_points:
        val += map_arr[point[1]][point[0]] + 1

    print(val)
