#!/usr/bin/env python3

import pprint
from functools import reduce
from sys import argv

bigprint = pprint.PrettyPrinter(width=320)


def parse_map(filename, map_list):
    with open(filename) as map_in:
        if len(map_list) == 0:
            # print('starting!')
            for line in map_in:
                map_list.append([0 if c == '.' else 1 for c in line.strip()])

        # the function is being called again to extend the map further
        else:
            iterator = 0
            # print('extending!')
            for line in map_in:
                map_list[iterator].extend(
                    [0 if c == '.' else 1 for c in line.strip()])
                iterator += 1


def calc_trees(filename, map_list, slope=(3, 1)):
    x, y = 0, 0
    tree_count = 0

    while y < len(map_list):
        # print("currentpos", x, y)
        # print("maplen", len(map_list[0]), len(map_list))
        # check current loc
        if map_list[y][x] == 1:
            tree_count += 1

        # step forward one iteration
        x += slope[0]
        y += slope[1]

        # if our next step brings us out of bounds, extend the map
        if x >= len(map_list[0])-1:
            while x >= len(map_list[0])-1:
                # print(x, len(map_list[0]))
                parse_map(filename, map_list)

    return tree_count


if __name__ == '__main__':
    filename = argv[1]
    map_list = []

    # part 1
    parse_map(filename, map_list)
    print("part1:", calc_trees(filename, map_list))

    # part 2
    result_list = []
    slope_list = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    for slope in slope_list:
        result_list.append(calc_trees(filename, map_list, slope=slope))
    print("part2:", reduce(lambda x, y: x*y, result_list))
