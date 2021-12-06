#!/usr/bin/env python3
# ive left my slower methods in as reference for how I was doing it for part1, they don't work any more because of how I changed fish_list

import traceback
from sys import argv

filename = argv[1]

fish_list = [0, 0, 0, 0, 0, 0, 0, 0, 0]
current_day = 0


def parse_input_file(input_name):
    with open(input_name) as input:
        for line in input:
            in_fish = [int(n) for n in line.split(',')]
        for fish in in_fish:
            new_fish = {'a': fish}
            fish_list.append(new_fish)


def quicker_parse_input_file(input_name):
    with open(input_name) as input:
        for line in input:
            in_fish = [int(n) for n in line.split(',')]

        for fish in in_fish:
            fish_list[fish] += 1
    print(fish_list)


def run_cycle():
    new_fish_list = []
    for fish in fish_list:
        if fish['a'] == 0:
            new_fish = {'a': 8}
            new_fish_list.append(new_fish)
            fish['a'] = 6
        elif fish['a'] > 0:
            fish['a'] -= 1

    fish_list.extend(new_fish_list)


def quicker_cycle():
    zero_fish = fish_list[0]
    del fish_list[0]
    fish_list[6] = fish_list[6] + zero_fish
    fish_list.append(zero_fish)


if __name__ == '__main__':
    part1 = False

    if part1:
        quicker_parse_input_file(filename)

        for day in range(0, 80):
            quicker_cycle()

        print(sum(fish_list))

    else:
        quicker_parse_input_file(filename)

        for day in range(0, 256):
            quicker_cycle()

        print(sum(fish_list))
