#!/usr/bin/env python3
"""
solution for day2
tags:
"""
import copy
import threading
from helpers import get_input


def parse_input() -> list[int]:
    """split the input to a list of ints"""
    input_str = get_input(2)
    return list(map(int, input_str.split(",")))


def run_cpu(instructions: list[int]) -> list[int]:
    """run the cpu instructions"""
    ic = 0

    while ic < len(instructions):
        oc = instructions[ic]
        # print(ic, oc, instructions)

        match oc:
            case 1:
                arg1 = instructions[ic + 1]
                arg2 = instructions[ic + 2]
                arg3 = instructions[ic + 3]

                instructions[arg3] = instructions[arg1] + instructions[arg2]
                ic += 4
            case 2:
                arg1 = instructions[ic + 1]
                arg2 = instructions[ic + 2]
                arg3 = instructions[ic + 3]

                instructions[arg3] = instructions[arg1] * instructions[arg2]
                ic += 4
            case 99:
                # print("Stopping")
                break
            case _:
                # print("Unknown opcode, halting")
                break

    return instructions


def validate():
    """validate the implementation"""
    tests = [
        ([1, 0, 0, 0, 99], [2, 0, 0, 0, 99]),
        ([2, 3, 0, 3, 99], [2, 3, 0, 6, 99]),
        ([2, 4, 4, 5, 99, 0], [2, 4, 4, 5, 99, 9801]),
        ([1, 1, 1, 4, 99, 5, 6, 0, 99], [30, 1, 1, 4, 2, 5, 6, 0, 99]),
    ]

    for t in tests:
        result = run_cpu(t[0])
        print(result == t[1])


def part_one():
    """solution for part one"""
    input_list = parse_input()
    # per the instructions
    input_list[1] = 12
    input_list[2] = 2
    result = run_cpu(input_list)
    print(f"Answer One: {result}")


def solver_thread(memory: list[int], noun: int, verb: int):
    """a function for threading a solver"""
    memory = copy.deepcopy(memory)
    memory[1] = noun
    memory[2] = verb

    result = run_cpu(memory)[0]
    if result == 19690720:
        print(f"Found match: 100 * {noun} + {verb}: {100 * noun + verb}")


def part_two():
    """solution for part two"""
    memory = parse_input()

    for x in range(0, 99):
        for y in range(0, 99):
            t = threading.Thread(target=solver_thread, args=(memory, x, y))
            t.start()


if __name__ == "__main__":
    part_two()
