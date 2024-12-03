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


def check_is_decreasing(reports: list[int]):
    return [reports[i] > reports[i + 1] for i in range(0, len(reports) - 1)]


def check_is_increasing(reports: list[int]):
    return [reports[i] < reports[i + 1] for i in range(0, len(reports) - 1)]


def check_valid_increasing(report):
    return all(
        (report[i + 1] - report[i] <= 3 and report[i + 1] - report[i] > 0)
        for i in range(0, len(report) - 1)
    )


def check_valid_decreasing(report):
    return all(
        (report[i] - report[i + 1] <= 3 and report[i] - report[i + 1] > 0)
        for i in range(0, len(report) - 1)
    )


def remove_false_value(check_list, value_list):
    first_false = check_list.index(False)
    del value_list[first_false]
    return value_list


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


def part_two(data: list[str]):
    """solution for part two"""
    increasing = []
    decreasing = []
    increasing_changed = []
    decreasing_changed = []

    # check all increasing/decreasing
    for line in data:
        reports = [int(i) for i in line.split()]
        if reports:
            is_decreasing = check_is_decreasing(reports)
            # this means there were no false, so it automatically passes
            false_count = sum(1 for check in is_decreasing if not check)
            if false_count == 0:
                decreasing.append(reports)

            # check if removing the value at the same index of the single False helps make it valid
            elif false_count == 1:
                new_list = remove_false_value(is_decreasing, reports)
                is_new_decreasing = check_is_decreasing(new_list)
                false_count = sum(1 for check in is_new_decreasing if not check)

                if false_count == 0:
                    decreasing_changed.append(new_list)

            is_increasing = check_is_increasing(reports)
            false_count = sum(1 for check in is_increasing if not check)

            # this means there were no false, so it automatically passes
            if false_count == 0:
                increasing.append(reports)

            # check if removing the value at the same index of the single False helps make it valid
            elif false_count == 1:
                new_list = remove_false_value(is_increasing, reports)
                is_new_increasing = check_is_increasing(new_list)
                false_count = sum(1 for check in is_new_increasing if not check)

                if false_count == 0:
                    increasing_changed.append(new_list)

    # check the distances between the numbers
    valid = []
    for report in increasing:
        valid_increasing = [
            (report[i + 1] - report[i] <= 3 and report[i + 1] - report[i] > 0)
            for i in range(0, len(report) - 1)
        ]
        false_count = sum(1 for check in valid_increasing if not check)
        if false_count == 0:
            valid.append(report)

        elif false_count == 1:
            new_list = remove_false_value(valid_increasing, report)
            if check_valid_increasing(new_list):
                valid.append(new_list)

    for report in increasing_changed:
        valid_increasing = [
            (report[i + 1] - report[i] <= 3 and report[i + 1] - report[i] > 0)
            for i in range(0, len(report) - 1)
        ]
        false_count = sum(1 for check in valid_increasing if not check)
        if false_count == 0:
            valid.append(report)

    for report in decreasing:
        valid_decreasing = [
            (report[i] - report[i + 1] <= 3 and report[i] - report[i + 1] > 0)
            for i in range(0, len(report) - 1)
        ]
        false_count = sum(1 for check in valid_decreasing if not check)
        if false_count == 0:
            valid.append(report)
        elif false_count == 1:
            new_list = remove_false_value(valid_decreasing, report)
            if check_valid_decreasing(new_list):
                valid.append(new_list)

    for report in decreasing_changed:
        valid_decreasing = [
            (report[i] - report[i + 1] <= 3 and report[i] - report[i + 1] > 0)
            for i in range(0, len(report) - 1)
        ]
        false_count = sum(1 for check in valid_decreasing if not check)
        if false_count == 0:
            valid.append(report)

    print("Part 2:", len(valid))


if __name__ == "__main__":
    """
    468 too low
    476 ????
    510 too high
    516 too high
    """
    data = get_input(2024, 2).split("\n")
    # part_one(data)
    part_two(EX_1)
    part_two(data)
