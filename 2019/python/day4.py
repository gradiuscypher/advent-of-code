#!/usr/bin/env python3
"""
solution for day4
ref: https://stackoverflow.com/questions/6785226/pass-multiple-parameters-to-concurrent-futures-executor-map
ref: https://realpython.com/intro-to-python-threading/#using-a-threadpoolexecutor
tags: concurrency, threads, range
"""

import concurrent.futures
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
    arr.append(value)


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
    except KeyboardInterrupt:
        sys.exit(1)
