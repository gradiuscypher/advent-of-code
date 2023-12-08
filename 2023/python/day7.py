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


def parse_hands(inp):
    """parse hand strings into lists of chars"""
    hand_list = []

    for line in inp.split("\n"):
        hand_list.append((line.split()[0], line.split()[1]))

    return hand_list


def get_hand_type(hand_str):
    """gets the hand type"""

    # five of a kind - 7
    if len(set(hand_str)) == 1:
        return 7

    if len(set(hand_str)) == 2:
        # four of a kind - 6
        if hand_str.count(hand_str[0]) == 1 or hand_str.count(hand_str[0]) == 4:
            return 6
        # full house - 5
        return 5

    # three of a kind - 4
    if len(set(hand_str)) == 3:
        if 3 in [hand_str.count(c) for c in hand_str]:
            return 4

    # two pair - 3
    if [hand_str.count(c) for c in hand_str].count(2) == 4:
        return 3

    # one pair - 2
    if [hand_str.count(c) for c in hand_str].count(1) == 3:
        return 2

    # high card - 1
    if len(set(hand_str)) == 5:
        return 1

    return 0


def sort_hands(hand_list):
    """compares hands and returns them in order low to high"""
    value_dict = {"T": "10", "J": "11", "Q": "12", "K": "13", "A": "14"}

    hand_values = {}

    # TODO: this sort doesn't work
    for h in hand_list:
        num_hand = [value_dict[c] if not c.isdigit() else c for c in h]
        hand_values[h] = int("".join(num_hand))

    return [c[0] for c in sorted(hand_values.items(), key=lambda x:x[1])]


def part_one():
    """solution for part one
    253530450 - too low
    """
    inp = TEST_INP
    # inp = get_input(2023, 7)
    inp = inp.strip()
    hands = parse_hands(inp)

    ranked = []
    hand_lookup = {}
    values = {}

    # sort the hands to their values
    for h, b in hands:
        hand_lookup[h] = b
        hand_value = get_hand_type(h)

        if hand_value in values.keys():
            values[get_hand_type(h)].append(h)
        else:
            values[get_hand_type(h)] = [h]
    values = dict(sorted(values.items()))

    for k in values:
        # sort_list = sorted(values[k], reverse=True)
        sort_list = (sort_hands(values[k]))
        ranked.extend(sort_list)

    print("Ranked:", ranked)
    total = 0
    for i, r in enumerate(ranked):
        total += (i + 1) * int(hand_lookup[r])

    print("Part One:", total)


def part_two():
    """solution for part two"""


if __name__ == "__main__":
    part_one()
