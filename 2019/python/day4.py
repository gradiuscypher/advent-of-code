#!/usr/bin/env python3
"""
solution for day4
ref: https://stackoverflow.com/questions/6785226/pass-multiple-parameters-to-concurrent-futures-executor-map
ref: https://realpython.com/intro-to-python-threading/#using-a-threadpoolexecutor
tags: concurrency, threads, range
"""

import concurrent.futures
import math
import sys
from itertools import repeat


def is_input_valid(value: int, arr) -> None:
    """
    reports if input is valid -
    * It is a six-digit number.
    * The value is within the range given in your puzzle input.
    * Two adjacent digits are the same (like 22 in 122345).
    * Going from left to right, the digits never decrease; they only ever increase or stay the same (like 111123 or 135679).
    """
    # check if it's a 6 digit number
    # TODO: looks like the range will always be 6 digits, so I don't need to validate this atm

    # check if it's within range
    # TODO: looks like the range will always be in range, so I don't need to validate this atm

    # turn int to list of digits, this is magic
    # src: https://stackoverflow.com/questions/21270320/turn-a-single-number-into-single-digits-python
    nlist = [
        (value // (10**i)) % 10 for i in range(math.ceil(math.log(value, 10)), -1, -1)
    ][bool(math.log(value, 10) % 1) :]

    # check for adjacent digits
    # first check the set len to see if we can fastfail numbers without dupes
    if len(set(nlist)) == len(nlist):
        return

    # next, check that the duplicate digits are adjacent
    # since they're always increasing, this list has to be > 0 for us to meet the dupe requirement
    # ref: https://stackoverflow.com/questions/11236006/identify-duplicate-values-in-a-list-in-python
    dupe_list = [i for i, x in enumerate(nlist) if nlist.count(x) > 1]
    if not len(dupe_list) > 0:
        return

    # check if digits never decrease
    # validate that they don't decrease
    if not all(nlist[i] <= nlist[i + 1] for i in range(0, len(nlist) - 1)):
        return

    # part2: validate that the doubles doesn't repeat more than twice
    for i in dupe_list:
        if nlist.count(nlist[i]) == 2:
            arr.append(value)
            return


def part_one():
    """solution for part one"""


def part_two():
    """solution for part two"""


if __name__ == "__main__":
    out_list = []
    value_range = range(248345, 746315)

    print("Starting check ...")
    try:
        with concurrent.futures.ThreadPoolExecutor(max_workers=32) as executor:
            executor.map(is_input_valid, value_range, repeat(out_list))

        print(len(out_list))

    except KeyboardInterrupt:
        sys.exit(1)
