#!/bin/bash poetry --version
"""
solution for dayN
tags:
"""

import logging
from helpers import get_input

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
ch = logging.StreamHandler()
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
ch.setFormatter(formatter)
logger.addHandler(ch)
ch.setLevel(logger.level)


def part_one():
    """solution for part one"""


def part_two():
    """solution for part two"""


if __name__ == "__main__":
    pass
