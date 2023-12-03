#!/usr/bin/env python3
"""
solution for day5
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

TEST_INP = """
BFFFBBFRRR
FFFBBBFRRR
BBFFBBFRLL
"""


def part_one():
    """solution for part one"""
    # inp = get_input(2020, 5)
    inp = TEST_INP
    inp = inp.strip().split("\n")

    for seat in inp:
        current_range = [0, 127]
        for c in seat:
            match c:
                case "F":
                    pass
                case "B":
                    pass
                case "R":
                    pass
                case "L":
                    pass


def part_two():
    """solution for part two"""


if __name__ == "__main__":
    part_one()
