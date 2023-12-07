#!/usr/bin/env python3
"""
solution for day7
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


TEST_INP = """
32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483
"""


def part_one():
    """solution for part one"""


def part_two():
    """solution for part two"""


if __name__ == "__main__":
    pass
