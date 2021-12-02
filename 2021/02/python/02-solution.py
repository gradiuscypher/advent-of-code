#!/usr/bin/env python3

import traceback
from sys import argv

filename = argv[1]


def solution1():
    h = 0
    v = 0

    with open(filename) as input:
        for line in input:
            if "forward" in line:
                h += int(line.split()[1])
            elif "up" in line:
                v -= int(line.split()[1])
            elif "down" in line:
                v += int(line.split()[1])
    print(h * v)


def solution2():
    aim = 0
    h = 0
    v = 0

    with open(filename) as input:
        for line in input:
            if "forward" in line:
                h += int(line.split()[1])
                v += aim * int(line.split()[1])
            elif "up" in line:
                aim -= int(line.split()[1])
            elif "down" in line:
                aim += int(line.split()[1])
    print(h * v)


if __name__ == "__main__":
    solution2()
