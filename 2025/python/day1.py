#!/usr/bin/env -S uv run
"""
solution for dayN
tags:
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

EX1 = """
L68
L30
R48
L5
R60
L55
L1
L99
R14
L82
"""

EX2 = """
L68
L30
R48
L5
R60
L55
L1
L99
R14
L82
"""

EX_TEST = """
R1000
"""


def part_one(user_input):
    """solution for part one"""
    # dial always starts at 50
    chal_input = user_input
    # chal_input = EX1
    dial_nums = list(range(0, 100))
    dial_index = 50
    total_zeros = 0
    for line in chal_input.split():
        direction = line[0]
        magnitude = int(line[1:])

        match direction:
            case "L":
                dial_index -= magnitude
            case "R":
                dial_index += magnitude
        dial_value = dial_nums[dial_index % len(dial_nums)]
        if dial_value == 0:
            total_zeros += 1
    print(total_zeros)


def part_two(user_input):
    """
    solution for part two
    wrong:
    5840
    7009 too high
    6541 too low
    """

    EX_TEST = """
    R50
    R100
    L250
    L50
    L120
    """

    # dial always starts at 50
    chal_input = user_input
    # chal_input = EX_TEST
    dial_nums = list(range(0, 100))
    dial_index = 50
    total_zeros = 0
    for line in chal_input.split():
        starting_zero = dial_index == 0
        direction = line[0]
        magnitude = int(line[1:])

        match direction:
            case "L":
                dial_index -= magnitude
            case "R":
                dial_index += magnitude

        dial_value = dial_nums[dial_index % len(dial_nums)]
        dial_over = dial_index / 100
        dial_index = dial_value
        zero_mod = 0
        print(direction, magnitude, dial_index, starting_zero, dial_over)

        if dial_value == 0:
            zero_mod += 1

        if dial_over < 0:
            zero_mod = int(abs(dial_over) + 1)
            if starting_zero:
                zero_mod -= 1

        elif dial_over >= 1:
            zero_mod = int(dial_over)

        print("zeromod:", zero_mod, "is_zero:", dial_value == 0)
        total_zeros += zero_mod

    print("total:", total_zeros)


if __name__ == "__main__":
    user_input = get_input(2025, 1)
    # part_one(user_input)
    part_two(user_input)
