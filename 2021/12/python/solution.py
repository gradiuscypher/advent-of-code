#!/usr/bin/env python3

from sys import argv


if __name__ == '__main__':
    filename = argv[1]

    with open(filename) as input:
        for line in input:
            sline = line.strip().split('-')
