#!/usr/bin/env python3

from sys import argv


def find_shortest_move(numbers):
    part2 = True
    max_val = max(numbers)

    total = 0

    rlist = []

    for n in range(0, max_val+1):
        # for n in range(2, 3):
        for number in numbers:
            dist = abs(n - number)
            total += (dist**2 + dist)/2

        rlist.append(total)
        # print(n, total)
        total = 0

    min_rlist = min(rlist)
    print(rlist.index(min_rlist), min_rlist)


if __name__ == '__main__':
    filename = argv[1]

    with open(filename) as input:
        numbers = [int(n) for n in input.read().strip().split(',')]
        find_shortest_move(numbers)
