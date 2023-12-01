#!/usr/bin/env python3
"""
solution for dayN
tags:
"""

import itertools
import logging
import sys
from helpers import get_input

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
ch.setFormatter(formatter)
logger.addHandler(ch)
ch.setLevel(logger.level)


def parse_input() -> list[int]:
    """split the input to a list of ints"""
    input_str = get_input(7)
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


def run_cpu(instructions: list[int], input_array: list[int] = []) -> int:
    """run the cpu instructions"""
    ic = 0
    output = 0

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
                instructions[arg1] = input_array.pop(0)
                ic += 2

            case 4:
                # output
                arg1 = fetch_data(modes, instructions, ic, 1)
                logger.debug("input arg: %s", arg1)
                logger.debug(instructions)
                logger.info("**OUTPUT**: %s", arg1)
                output = arg1
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

    return output


def validate():
    """validate the implementation"""
    # fmt: off
    tests = [
        [
            3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,
            1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99,
        ]
    ]
    # fmt: on

    for t in tests:
        logger.debug("test:\n%s", t)
        result = run_cpu(t)
        logger.debug("result:\n%s", result)
        logger.debug("-----\n")


def part_one(input_inst: list[int], test_mode: bool = False):
    """solution for part one"""
    if test_mode:
        # # fmt: off
        # sequences = [
        #     [4,3,2,1,0],
        #     [0,1,2,3,4],
        #     [1,0,4,3,2]
        # ]
        # instructions = [
        #     [3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0],
        #     [3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0],
        #     [3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0]
        # ]
        # # fmt: on

        # for test_index in range(0, 3):
        #     input_signal = 0
        #     for n in sequences[test_index]:
        #         input_signal = run_cpu(instructions[test_index], [n, input_signal])
        #         logger.debug(input_signal)
        #     print()
        print("testing")
    else:
        numbers = list(range(0, 5))
        permutations = list(itertools.permutations(numbers, 5))

        count = 1
        highest_value = 0
        for permutation in permutations:
            logger.info("Running test %s/%s", count, len(permutations))
            count += 1
            input_signal = 0
            for n in permutation:
                input_signal = run_cpu(input_inst, [n, input_signal])
            if input_signal > highest_value:
                highest_value = input_signal
            print()
        logger.info("Highest value: %s", highest_value)


def part_two():
    """solution for part two"""
    # fmt: off
    sequences = [
        [9,8,7,6,5],
    ]
    input_inst = [
        [3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5],
    ]
    # fmt: on

    for test_index in range(0, 1):
        input_list = [0] + sequences[test_index]
        output = run_cpu(input_inst[test_index], input_list)
        print("Final output:", output)


if __name__ == "__main__":
    instructions = parse_input()
    # part_one(input_inst=instructions)
    part_two()
