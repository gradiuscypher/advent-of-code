#!/usr/bin/env python3

import traceback
from sys import argv

filename = argv[1]


def calculate_gamma(input_list):
    bin_str = ""
    index = 0

    for i in range(0, len(input_list[0])):
        zcount = 0
        ocount = 0

        for instr in input_list:
            if instr[i] == '0':
                zcount += 1
            elif instr[i] == '1':
                ocount += 1

        # find which one to add
        if zcount > ocount:
            bin_str += '0'
        else:
            bin_str += '1'
    return bin_str


def calculate_epsilon(input_list):
    bin_str = ""
    index = 0

    for i in range(0, len(input_list[0])):
        zcount = 0
        ocount = 0

        for instr in input_list:
            if instr[i] == '0':
                zcount += 1
            elif instr[i] == '1':
                ocount += 1

        # find which one to add
        if zcount > ocount:
            bin_str += '1'
        else:
            bin_str += '0'
    return bin_str


def o2_rating(input_list):
    index = 0
    while len(input_list) > 1:
        most_common = get_most_common(index, input_list)
        print(f"most common: {most_common}")
        input_list = [i for i in input_list if i[index] == most_common]
        print(input_list)
        index += 1
    if len(input_list) == 1:
        print(f"o2 rating: {input_list[0]}")

    return int(input_list[0], 2)


def co2_rating(input_list):
    index = 0
    while len(input_list) > 1:
        least_common = get_least_common(index, input_list)
        print(f"least common: {least_common}")
        input_list = [i for i in input_list if i[index] == least_common]
        print(input_list)
        index += 1
    if len(input_list) == 1:
        print(f"o2 rating: {input_list[0]}")

    return int(input_list[0], 2)


def get_most_common(index, input_list):
    bin_str = ""
    zcount = 0
    ocount = 0

    for instr in input_list:
        if instr[index] == '0':
            zcount += 1
        elif instr[index] == '1':
            ocount += 1

    # find which one to add
    if zcount > ocount:
        bin_str += '0'
    elif zcount < ocount:
        bin_str += '1'
    elif zcount == ocount:
        bin_str += '1'

    return bin_str


def get_least_common(index, input_list):
    bin_str = ""
    zcount = 0
    ocount = 0

    for instr in input_list:
        if instr[index] == '0':
            zcount += 1
        elif instr[index] == '1':
            ocount += 1

    # find which one to add
    if zcount > ocount:
        bin_str += '1'
    elif zcount < ocount:
        bin_str += '0'
    elif zcount == ocount:
        bin_str += '0'

    return bin_str


if __name__ == "__main__":
    with open(filename) as input_file:
        in_list = [l.strip() for l in input_file.readlines()]
        # gamma = (int(calculate_gamma(in_list), 2))
        # epsilon = (int(calculate_epsilon(in_list), 2))
        # print(gamma*epsilon)
        print(o2_rating(in_list))
        print(co2_rating(in_list))
        print(o2_rating(in_list)*co2_rating(in_list))
