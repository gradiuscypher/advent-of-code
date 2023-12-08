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

HAND_LOOKUP = {
    7: "Five of a Kind",
    6: "Four of a Kind",
    5: "Full House",
    4: "Three of a Kind",
    3: "Two Pair",
    2: "One Pair",
    1: "High Card",
}


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


def is_bigger(h1, h2, p2=False):
    """is it bigger"""

    value_dict = {"T": 10, "J": 11, "Q": 12, "K": 13, "A": 14}
    if p2:
        value_dict = {"T": 10, "J": 0, "Q": 12, "K": 13, "A": 14}

    h1 = [int(c) if c.isdigit() else value_dict[c] for c in h1]
    h2 = [int(c) if c.isdigit() else value_dict[c] for c in h2]

    for i, c in enumerate(h1):
        if c > h2[i]:
            return True
        if h2[i] > c:
            return False
    return False


def sort_hands(hand_list):
    """compares hands and returns them in order low to high"""
    sorted_list = hand_list[:1]

    for h1 in hand_list[1:]:
        has_sorted = False

        for i, h2 in enumerate(sorted_list):
            if is_bigger(h1, h2):
                sorted_list.insert(i, h1)
                print(h1, "IS BIGGER", h2)
                has_sorted = True
                break

        if not has_sorted:
            sorted_list.append(h1)
            print(h1, "TO THE END")

    return sorted_list


def part_one():
    """solution for part one
    253530450 - too low
    254076898 - too high
    """
    # inp = TEST_INP
    inp = get_input(2023, 7)
    inp = inp.strip()
    hands = parse_hands(inp)

    ranked = []
    hand_lookup = {}
    values = {}

    # sort the hands to their values
    for h, b in hands:
        hand_lookup[h] = b
        hand_value = get_hand_type(h)
        if HAND_LOOKUP[hand_value] == "Five of a Kind":
            print("FK:", h)

        if hand_value in values.keys():
            values[get_hand_type(h)].append(h)
        else:
            values[get_hand_type(h)] = [h]
    values = dict(sorted(values.items()))

    for k in values:
        # sort_list = sorted(values[k], reverse=True)
        sort_list = sort_hands(values[k])
        sort_list.reverse()

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
