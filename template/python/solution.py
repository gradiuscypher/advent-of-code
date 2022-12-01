#!/usr/bin/env python3

import logging
from sys import argv


# logging so that I can throw debug strings around without feeling bad
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)


def load_input(filename):
    with open(filename) as input:
        for line in input:
            pass


if __name__ == '__main__':
    filename = argv[1]
    load_input(filename)
