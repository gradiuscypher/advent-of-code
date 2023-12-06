#!/usr/bin/env python3
"""
solution for dayN
tags:
"""
import logging
from math import sqrt
from helpers import get_input


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
ch = logging.StreamHandler()
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
ch.setFormatter(formatter)
logger.addHandler(ch)
ch.setLevel(logger.level)

TEST_INP = """
Time:      7  15   30
Distance:  9  40  200
""".strip()


def part_one():
    """solution for part one"""
    inp = TEST_INP
    inp = get_input(2023, 6)
    inp = inp.splitlines()
    time_list = [int(n) for n in inp[0].split(":")[1].strip().split()]
    dist_list = [int(n) for n in inp[1].split(":")[1].strip().split()]

    total = 1
    for t, d in zip(time_list, dist_list):
        best_holds = []
        for hold in range(0, t):
            curr_dist = (t - hold) * hold
            print("CUR DIS", curr_dist)
            if curr_dist > d:
                best_holds.append(curr_dist)

        total = total * len(best_holds)

    print("Part One:", total)


def part_two():
    """solution for part two
    t : time held = (m - r)
    r : time remaining = (m - t)
    m : max time = (t + r)
    d : distance = (t * r)
    """
    inp = TEST_INP
    # inp = get_input(2023, 6)
    inp = inp.splitlines()


if __name__ == "__main__":
    # part_one()
    part_two()
