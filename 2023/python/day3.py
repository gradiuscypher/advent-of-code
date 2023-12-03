#!/usr/bin/env python3
"""
solution for dayN
tags:
old answers:
322449 - too low
"""

import logging
from helpers import get_input

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
ch = logging.StreamHandler()
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
ch.setFormatter(formatter)
logger.addHandler(ch)
ch.setLevel(logger.level)

TEST_INP = """
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
"""


def sweep(target_row, x, left=True):
    found_digits = True
    bound = x
    while found_digits:
        if bound < 0 or bound >= len(target_row):
            found_digits = False
            if left:
                bound = bound + 1
            else:
                bound = bound - 1
        elif not target_row[bound].isdigit():
            found_digits = False
            if left:
                bound = bound + 1
            else:
                bound = bound - 1
        else:
            if left:
                bound = bound - 1
            else:
                bound = bound + 1
    return bound


def parse_input(inp):
    inp = inp.strip().split("\n")
    schematic = []
    for line in inp:
        row = []
        for c in line:
            row.append(c)
        schematic.append(row)
    return schematic


def get_value(schematic, x, y):
    target_row = schematic[y]

    left_bound = sweep(target_row, x, left=True)
    right_bound = sweep(target_row, x, left=False)

    return "".join(target_row[left_bound : right_bound + 1])


def get_adjacent(schematic, x, y):
    value_set = set()
    adj_mods = [(-1, 1), (0, 1), (1, 1), (-1, 0), (1, 0), (-1, -1), (0, -1), (1, -1)]
    for m in adj_mods:
        value = get_value(schematic, x + m[0], y + m[1])

        if value:
            value_set.add(int(value))
    return value_set


def part_one():
    """solution for part one"""
    inp = get_input(2023, 3)
    # inp = TEST_INP
    schematic = parse_input(inp)
    # value_set = set()
    value_set = []

    for y in range(0, len(schematic)):
        for x in range(0, len(schematic[y])):
            # print(f"{x}, {y}")
            c = schematic[y][x]
            if not c.isdigit() and c != ".":
                # print(f"{x}, {y} - {c}")
                values = get_adjacent(schematic, x, y)
                value_set.extend(values)

    # print("Value Set:", value_set)
    print("Part One:", sum(value_set))


def part_two():
    """solution for part two"""
    inp = get_input(2023, 3)
    # inp = TEST_INP
    schematic = parse_input(inp)
    total = 0

    for y in range(0, len(schematic)):
        for x in range(0, len(schematic[y])):
            # print(f"{x}, {y}")
            c = schematic[y][x]
            if c == "*":
                values = list(get_adjacent(schematic, x, y))
                if len(values) == 2:
                    total += values[0] * values[1]

    # print("Value Set:", value_set)
    print("Part Two:", total)


if __name__ == "__main__":
    part_one()
    part_two()
