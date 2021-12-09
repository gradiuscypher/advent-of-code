#!/usr/bin/env python3

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
            # check spots around this point if it or its neighboors are considered a low point, if so, compare and determine who's lower
            low_points.append([x, y])

            low_val = map_arr[y][x]
            low_point = [x, y]

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
                if 0 < mx < len(map_arr[y]) and 0 < my < len(map_arr) and map_arr[my][mx] < low_val:
                    print(low_points, low_val)
                    low_points.remove(low_point)
                    low_val = map_arr[my][mx]
                    low_point = [mx, my]
                    low_points.append(low_point)

    return low_points


if __name__ == '__main__':
    filename = argv[1]

    map_arr = parse_map(filename)
    pprint(find_low_points(map_arr))
