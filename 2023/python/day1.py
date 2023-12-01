#!/usr/bin/env python3
"""
solution for day1
tags: wtf, substring
"""

import logging
import re
from helpers import get_input

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
ch = logging.StreamHandler()
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
ch.setFormatter(formatter)
logger.addHandler(ch)
ch.setLevel(logger.level)


def find_char(s, ch):
    return [i for i, ltr in enumerate(s) if ltr == ch]


def find_substr(whole_str, sub_str):
    return [m.start() for m in re.finditer(sub_str, whole_str)]


def part_one():
    """solution for part one"""
    inp = get_input(2023, 1).strip().split("\n")

    total = 0
    count = 0
    for line in inp:
        count += 1
        nums = [c for c in line if c.isdigit()]
        # if not "".join(nums) == line:
        #     print("wat", line, nums)
        if len(nums) < 2:
            # print(f"s: {nums}")
            val = int(f"{nums[0]}{nums[0]}")
            total += val
            print(val)
        else:
            # print(f"r: {nums}")
            val = int(f"{nums[0]}{nums[-1]}")
            total += val
            print(val)

    print(total, count)


def part_two():
    """
    solution for part two
    """
    total = 0
    num_strs = [
        "zero",
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
    ]

    inp = [
        "two1nine",
        "eightwothree",
        "abcone2threexyz",
        "xtwone3four",
        "4nineeightseven2",
        "zoneight234",
        "7pqrstsixteen",
        "eightkmdxmccv4vrvjlpgcqthree787q",
        "449three45three",
    ]
    inp = get_input(2023, 1).strip().split("\n")

    for line in inp:
        lowest = None
        lo_ind = 9999
        highest = None
        hi_ind = 0

        for s in num_strs:
            if s in line:
                locs = find_substr(line, s)
                val = num_strs.index(s)

                for loc in locs:
                    if not lowest:
                        lowest = val
                        lo_ind = loc
                    if not highest:
                        highest = val
                        hi_ind = loc

                    if loc < lo_ind:
                        lowest = val
                        lo_ind = loc
                    elif loc > hi_ind:
                        highest = val
                        hi_ind = loc

        for c in line:
            if c.isdigit():
                locs = find_char(line, c)
                for loc in locs:
                    if not lowest:
                        lowest = c
                        lo_ind = loc
                    if not highest:
                        highest = c
                        hi_ind = loc

                    if loc < lo_ind:
                        lowest = c
                        lo_ind = loc
                    elif loc > hi_ind:
                        highest = c
                        hi_ind = loc
        line_val = int(f"{lowest}{highest}")
        total += line_val
    print("total:", total)


if __name__ == "__main__":
    # part_one()
    part_two()
