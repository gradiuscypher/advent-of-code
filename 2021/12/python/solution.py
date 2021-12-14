#!/usr/bin/env python3

"""
Notes:
# Breadth First Search Approach?

"""

from sys import argv


def load_input(filename):
    data_list = []
    with open(filename) as inputfile:
        for line in inputfile:
            data_list.append(line.strip().split('-'))
    return data_list


if __name__ == '__main__':
    filename = argv[1]

    load_input(filename)
