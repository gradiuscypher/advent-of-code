#!/usr/bin/env python3
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

TEST_INP = """
Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
"""


def parse_cards(inp):
    inp = inp.strip().split("\n")
    all_cards = {}

    for card_line in inp:
        card_split = card_line.split("|")
        card_id = int(card_split[0].split(":")[0].split("Card")[1].strip())
        winning_nums = set(
            [int(n) for n in card_split[1].strip().split(" ") if n.isdigit()]
        )
        our_nums = set(
            [
                int(n)
                for n in card_split[0].split(":")[1].strip().split(" ")
                if n.isdigit()
            ]
        )
        all_cards[card_id] = [winning_nums, our_nums]

    return all_cards


def count_wins(card):
    return len(card[1].intersection(card[0]))


def calculate_value(card_line):
    card_split = card_line.split("|")
    winning_nums = set(
        [int(n) for n in card_split[1].strip().split(" ") if n.isdigit()]
    )
    our_nums = set(
        [int(n) for n in card_split[0].split(":")[1].strip().split(" ") if n.isdigit()]
    )
    win_count = len(our_nums.intersection(winning_nums))
    if win_count > 0:
        return 2 ** (win_count - 1)
    else:
        return 0


def part_one():
    """solution for part one"""
    inp = get_input(2023, 4)
    # inp = TEST_INP
    inp = inp.strip().split("\n")

    total = 0
    for line in inp:
        total += calculate_value(line)
    print("Part One:", total)


def part_two():
    """solution for part two"""
    inp = get_input(2023, 4)
    inp = TEST_INP
    all_cards = parse_cards(inp)
    card_stack = list(all_cards.keys())

    total = 0
    while card_stack:
        c = card_stack.pop(0)
        print("Cards remaining:", len(card_stack))
        total += 1
        win_count = count_wins(all_cards[c])

        if win_count > 0:
            for n in range(c + 1, c + win_count + 1):
                card_stack.append(n)

    print("Part Two:", total)


if __name__ == "__main__":
    # part_one()
    part_two()
