#!/usr/bin/env python3
"""
solution for dayN
tags:
"""

import logging
from pprint import pprint
from helpers import get_input

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
ch = logging.StreamHandler()
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
ch.setFormatter(formatter)
logger.addHandler(ch)
ch.setLevel(logger.level)

TEST_INPUT = """
Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
"""


def game_parser(game_inp):
    games = {}

    for line in game_inp:
        game_id = line.split(":")[0].split(" ")[1]
        rounds = [r.strip() for r in line.split(":")[1].split(";")]

        round_list = []
        for r in rounds:
            round_dict = {}
            cubes = [c.strip() for c in r.split(",")]
            for c in cubes:
                csplit = c.split()
                round_dict[csplit[1]] = csplit[0]
            round_list.append(round_dict)
        games[game_id] = round_list

    return games


def part_one():
    """solution for part one"""
    inp = get_input(2023, 2).strip().split("\n")
    # inp = TEST_INPUT.strip().split("\n")
    games = game_parser(inp)
    max_lookup = {"red": 12, "green": 13, "blue": 14}

    good_games = {}
    bad_games = {}

    for game in games.items():
        failed_game = False
        for r in game[1]:
            for c in r.items():
                if int(c[1]) > max_lookup[c[0]]:
                    # print("BAD VALUE: ", c[0], c[1])
                    failed_game = True

        if not failed_game:
            # print("GOOD GAME:")
            # print(game[1])
            # print()
            good_games[game[0]] = game[1]
        else:
            # print("BAD GAME:")
            # print(game[1])
            # print()
            bad_games[game[0]] = game[1]

    # pprint(good_games)
    # print("--------")
    # pprint(bad_games)

    total = 0
    for g in good_games.items():
        total += int(g[0])
    print("Total:", total)


def part_two():
    """solution for part two"""
    inp = get_input(2023, 2).strip().split("\n")
    # inp = TEST_INPUT.strip().split("\n")
    games = game_parser(inp)

    game_dict = {}

    for game in games.items():
        low_dict = {"red": 0, "green": 0, "blue": 0}
        game_id = game[0]
        game_rounds = game[1]

        for r in game_rounds:
            for c in r.items():
                color_name = c[0]
                color_count = int(c[1])
                if low_dict[color_name] < color_count:
                    low_dict[color_name] = color_count
        game_dict[game_id] = low_dict

    total = 0
    for g in game_dict.items():
        gval = 1
        game_id = g[0]
        game_values = g[1]

        for v in game_values.items():
            gval = gval * int(v[1])
        total += gval

    print(total)


if __name__ == "__main__":
    # part_one()
    part_two()
