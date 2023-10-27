#!/usr/bin/env python3
"""
solution for day5
tags: log,
"""

import logging
import sys
from helpers import get_input

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
ch = logging.StreamHandler()
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
ch.setFormatter(formatter)
logger.addHandler(ch)
ch.setLevel(logger.level)


def parse_input() -> list[int]:
    """split the input to a list of ints"""
    input_str = get_input(5)
    return list(map(int, input_str.split(",")))


def fetch_data(modes, instructions, ic, mode_index) -> int:
    """fetches data with respect to current mode"""
    result = None
    logger.debug("modes: %s", modes)
    arr_addr = instructions[ic + mode_index]
    if len(modes) > 0:
        mode = modes.pop()
        logger.debug("cur mode: %s", mode)
        if mode == "0":
            result = instructions[instructions[ic + mode_index]]
        elif mode == "1":
            result = instructions[ic + mode_index]
        else:
            logger.error("Unknown mode: %s", mode)
    else:
        logger.debug("No mode array, defaulting to position mode: %s", arr_addr)
        result = instructions[arr_addr]

    if result is not None:
        logger.debug(
            "arg index: %s | addr: %s | value: %s", mode_index, arr_addr, result
        )
        return result

    logger.error("An error occurred while fetching data: %s", repr(result))
    sys.exit(1)


def run_cpu(instructions: list[int]) -> list[int]:
    """run the cpu instructions"""
    ic = 0

    while ic < len(instructions):
        # turn int to list of digits, this is magic
        # src: https://stackoverflow.com/questions/21270320/turn-a-single-number-into-single-digits-python
        logger.debug("current ic: %s", ic)
        logger.debug("oc str: %s", str(instructions[ic])[-2:])
        oc = int(str(instructions[ic])[-2:])
        logger.debug("oc: %s", oc)

        # pop from modes to get each parameter mode
        modes = list(str(instructions[ic])[0:-2])

        match oc:
            case 1:
                # addition
                arg1 = fetch_data(modes, instructions, ic, 1)
                arg2 = fetch_data(modes, instructions, ic, 2)
                # the arg you write to is always just the address
                arg3 = instructions[ic + 3]

                logger.debug("running addition: %s %s %s", arg1, arg2, arg3)
                instructions[arg3] = arg1 + arg2
                ic += 4

            case 2:
                # multiplication
                arg1 = fetch_data(modes, instructions, ic, 1)
                arg2 = fetch_data(modes, instructions, ic, 2)
                # the arg you write to is always just the address
                arg3 = instructions[ic + 3]

                logger.debug("running multiplication %s %s %s", arg1, arg2, arg3)
                instructions[arg3] = arg1 * arg2
                ic += 4

            case 3:
                # input
                # note: we'll just fake input since we only have to provide the int 1

                # the arg you write to is always just the address
                arg1 = instructions[ic + 1]

                logger.debug("input arg: %s", arg1)
                instructions[arg1] = 5
                ic += 2

            case 4:
                # output
                arg1 = fetch_data(modes, instructions, ic, 1)
                logger.debug("input arg: %s", arg1)
                logger.debug(instructions)
                logger.info("**OUTPUT**: %s", arg1)
                ic += 2

            case 5:
                # jump if true
                arg1 = fetch_data(modes, instructions, ic, 1)
                arg2 = fetch_data(modes, instructions, ic, 2)
                if arg1 != 0:
                    ic = arg2
                else:
                    ic += 3

            case 6:
                # jump if false
                arg1 = fetch_data(modes, instructions, ic, 1)
                arg2 = fetch_data(modes, instructions, ic, 2)
                if arg1 == 0:
                    ic = arg2
                else:
                    ic += 3

            case 7:
                # less than
                arg1 = fetch_data(modes, instructions, ic, 1)
                arg2 = fetch_data(modes, instructions, ic, 2)
                # the arg you write to is always just the address
                arg3 = instructions[ic + 3]
                if arg1 < arg2:
                    instructions[arg3] = 1
                else:
                    instructions[arg3] = 0
                ic += 4

            case 8:
                # less than
                arg1 = fetch_data(modes, instructions, ic, 1)
                arg2 = fetch_data(modes, instructions, ic, 2)
                # the arg you write to is always just the address
                arg3 = instructions[ic + 3]
                if arg1 == arg2:
                    instructions[arg3] = 1
                else:
                    instructions[arg3] = 0
                ic += 4

            case 99:
                logger.info("End of program, stopping")
                break
            case _:
                logger.error("Unknown opcode: %s", oc)
                break

        logger.debug("----------\n")

    return instructions


def validate():
    """validate the implementation"""
    # tests = [[1002, 4, 3, 4, 33], [3, 3, 99, 1337], [4, 3, 99, 1337]]
    # tests = [
    #     [3, 9, 8, 9, 10, 9, 4, 9, 99, -1, 8],
    #     [3, 9, 7, 9, 10, 9, 4, 9, 99, -1, 8],
    #     [3, 3, 1108, -1, 8, 3, 4, 3, 99],
    #     [3, 3, 1107, -1, 8, 3, 4, 3, 99],
    #     [3, 12, 6, 12, 15, 1, 13, 14, 13, 4, 13, 99, -1, 0, 1, 9],
    #     [3, 3, 1105, -1, 9, 1101, 0, 0, 12, 4, 12, 99, 1],
    # ]
    tests = [
        [
            3,
            21,
            1008,
            21,
            8,
            20,
            1005,
            20,
            22,
            107,
            8,
            21,
            20,
            1006,
            20,
            31,
            1106,
            0,
            36,
            98,
            0,
            0,
            1002,
            21,
            125,
            20,
            4,
            20,
            1105,
            1,
            46,
            104,
            999,
            1105,
            1,
            46,
            1101,
            1000,
            1,
            20,
            4,
            20,
            1105,
            1,
            46,
            98,
            99,
        ]
    ]

    for t in tests:
        logger.debug("test:\n%s", t)
        result = run_cpu(t)
        logger.debug("result:\n%s", result)
        logger.debug("-----\n")


def part_one():
    """solution for part one"""
    instructions = parse_input()
    logger.debug(instructions)
    result = run_cpu(instructions)
    logger.debug(result)


def part_two():
    """solution for part two"""
    instructions = parse_input()
    logger.debug(instructions)
    result = run_cpu(instructions)
    logger.debug(result)


if __name__ == "__main__":
    # validate()
    # part_one()
    part_two()
