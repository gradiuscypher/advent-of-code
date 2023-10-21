#!/usr/bin/env python3
"""
solution for dayN
"""

from helpers import get_input


def part_one():
    """solution for part one"""


def part_two():
    """solution for part two"""


def find_intersections(step_list: list[str]):
    """finds all intersections based on step list"""
    visited_points = []
    current_pos = (0, 0)

    for step in step_list:
        dir = step[0]
        val = int(step[1:])

        match step[0]:
            case "U":
                print("up", val)
            case "D":
                print("down", val)
            case "L":
                print("left", val)
            case "R":
                print("right", val)


if __name__ == "__main__":
    test_input = [
        "R8,U5,L5,D3",
        "U7,R6,D4,L4",
        "R75,D30,R83,U83,L12,D49,R71,U7,L72,U62,R66,U55,R34,D71,R55,D58,R83",
        "R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51,U98,R91,D20,R16,D67,R40,U7,R15,U6,R7",
    ]
    input_text = test_input[0]
    # input_text = get_input(3)
    for line in input_text.split("\n"):
        steps = line.split(",")
        if len(steps) > 1:
            find_intersections(steps)
