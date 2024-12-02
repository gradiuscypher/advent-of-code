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
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
""".split("\n")


def part_one(data: list[str]):
    """solution for part one"""
    increasing = []
    decreasing = []

    # check all increasing/decreasing
    for line in data:
        reports = [int(i) for i in line.split()]
        if reports:
            is_decreasing = all(
                reports[i] > reports[i + 1] for i in range(0, len(reports) - 1)
            )
            is_increasing = all(
                reports[i] < reports[i + 1] for i in range(0, len(reports) - 1)
            )
            if is_increasing:
                increasing.append(reports)
            elif is_decreasing:
                decreasing.append(reports)

    # check the distances between the numbers
    valid = []
    for report in increasing:
        valid_increasing = all(
            (report[i + 1] - report[i] <= 3 and report[i + 1] - report[i] > 0)
            for i in range(0, len(report) - 1)
        )
        if valid_increasing:
            valid.append(report)
    for report in decreasing:
        valid_decreasing = all(
            (report[i] - report[i + 1] <= 3 and report[i] - report[i + 1] > 0)
            for i in range(0, len(report) - 1)
        )
        if valid_decreasing:
            valid.append(report)

    print("Part 1:", len(valid))


def part_two():
    """solution for part two"""


if __name__ == "__main__":
    data = get_input(2024, 2).split("\n")
    part_one(data)
