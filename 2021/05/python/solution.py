#!/usr/bin/env python3

import copy
from pprint import pprint
import traceback
from sys import argv

filename = argv[1]

sea = [[0] * 1000 for _ in range(1000)]


def line_iterator(start, end):
    path_list = []
    # figure out whether x or y is changing
    # this means x is changing
    if start[0] != end[0] and start[1] == end[1]:
        # this means x is decreasing
        if start[0] > end[0]:
            # print(f"going from {start} to {end}")
            for x in range(start[0], end[0]-1, -1):
                # print(f"shrinking x value: {x},{start[1]}")
                path_list.append([x, start[1]])

        # this means x is increasing
        if start[0] < end[0]:
            # print(f"going from {start} to {end}")
            for x in range(start[0], end[0]+1, 1):
                # print(f"shrinking x value: {x},{start[1]}")
                path_list.append([x, start[1]])

    # this means y is changing
    elif start[1] != end[1] and start[0] == end[0]:
        if start[1] > end[1]:
            # print(f"going from {start} to {end}")
            for y in range(start[1], end[1]-1, -1):
                # print(f"shrinking x value: {x},{start[1]}")
                path_list.append([start[0], y])

        # this means y is increasing
        if start[1] < end[1]:
            # print(f"going from {start} to {end}")
            for y in range(start[1], end[1]+1, 1):
                # print(f"shrinking x value: {x},{start[1]}")
                path_list.append([start[0], y])

    else:
        # print(f"{start} to {end} looks like a diagonal")
        if start[0] > end[0]:
            xmod = -1
        else:
            xmod = 1

        if start[1] > end[1]:
            ymod = -1
        else:
            ymod = 1

        # I could use list[-1] but my brain cant fix this right now
        current_pos = [start[0], start[1]]
        path_list.append([start[0], start[1]])

        # can we do a combined move to get there? (+/-1 in both directions)
        while (current_pos[0] != end[0]) and (current_pos[1] != end[1]):
            if (current_pos[0] != end[0]) and (current_pos[1] != end[1]):
                current_pos[0] += xmod
                current_pos[1] += ymod
                # print("both up:", current_pos)
                # path_list.append(current_pos)

            elif current_pos[0] != end[0]:
                current_pos[0] += xmod
                # path_list.append(current_pos)
                # print("x up:", current_pos)

            elif current_pos[1] != end[1]:
                current_pos[1] += ymod
                # path_list.append(current_pos)
                # print("y up:", current_pos)

            path_list.append(copy.deepcopy(current_pos))

    # figure out which direction x/y is changing in (+/-)
    # generate all points between those two points as a list and return
    # print(f"{start} to {end} path: {path_list}")
    # print()
    return path_list


def count_bad():
    tally = 0
    for row in sea:
        for col in row:
            if col >= 2:
                tally += 1
    return tally


def fill_map():
    with open(filename) as input:
        for line in input:
            data = line.strip().split(' -> ')
            start_point = [int(n) for n in data[0].split(',')]
            end_point = [int(n) for n in data[1].split(',')]
            path_points = line_iterator(start_point, end_point)

            # iterate over every path point and increase value on map
            for point in path_points:
                x = point[0]
                y = point[1]
                sea[x][y] = sea[x][y] + 1
        print(f"answer: {count_bad()}")


if __name__ == '__main__':
    fill_map()
