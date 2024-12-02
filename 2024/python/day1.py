#!/usr/bin/env python3
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

EX_1 = """
3   4
4   3
2   5
1   3
3   9
3   3
"""


def part_one(input: list[str]):
    """solution for part one"""
    left, right = (
        [int(line.split("   ")[0]) for line in input if len(line) > 0],
        [int(line.split("   ")[1]) for line in input if len(line) > 0],
    )
    left.sort()
    right.sort()

    total = 0
    for i in range(0, len(left)):
        total += abs(left[i] - right[i])

    print("day1: ", total)


def part_two(input: list[str]):
    """
    solution for part two
    still day1 so we can brute force this
    """
    left, right = (
        [int(line.split("   ")[0]) for line in input if len(line) > 0],
        [int(line.split("   ")[1]) for line in input if len(line) > 0],
    )
    left.sort()
    right.sort()

    right_count = {}
    for n in right:
        if n in right_count:
            right_count[n] += 1
        else:
            right_count[n] = 1

    total = 0
    for n in left:
        if n in right_count:
            total += right_count[n] * n

    print("day1.2 ", total)


if __name__ == "__main__":
    day1_in = get_input(2024, 1).split("\n")
    # day1_in = EX_1.split("\n")
    # part_one(day1_in)
    part_two(day1_in)
