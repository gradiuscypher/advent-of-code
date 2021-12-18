#!/usr/bin/env python3

import logging
import json
from sys import argv

deeplist = []


def parse_input(filename):
    input_list = []
    with open(filename) as inputfile:
        for line in inputfile:
            input_list.append(json.loads(line.strip()))

    return input_list


def depth(l, cd=0):
    global deeplist
    if isinstance(l, list) and cd >= 4 and len(deeplist) == 0:
        deeplist = l
    if isinstance(l, list):
        cd += 1
        print(cd)
        return 1 + max(depth(item, cd) for item in l)
    else:
        return 0


def add_all_input(input_list):
    seed1 = input_list.pop(0)
    seed2 = input_list.pop(0)
    result_list = [seed1, seed2]

    while input_list:
        current = input_list.pop(0)
        result_list = [result_list, current]
    return result_list


if __name__ == '__main__':
    filename = argv[1]
    l = parse_input(filename)
    r = add_all_input(l)
    print(r)
    test = json.loads("[[[[1,1],[2,2]],[3,3]],[4,4]]")
    print(r == test)
