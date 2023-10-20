#!/usr/bin/env python3
"""
solution for day1
"""


def get_input() -> list[int]:
    """
    get the input
    """
    input_list = []
    with open("input/day1") as inputfile:
        for line in inputfile:
            input_list.append(int(line))
    return input_list


def answer_one() -> int:
    """calculate answer one"""
    total_fuel = 0
    input_list = get_input()

    for mass in input_list:
        total_fuel += (mass // 3) - 2

    return total_fuel


def get_fuel_for_mass(mass: int) -> int:
    """get the fuel for the provided mass, taking into account the mass of the fuel"""
    total_fuel = (mass // 3) - 2

    if total_fuel <= 0:
        return 0

    return total_fuel + get_fuel_for_mass(total_fuel)


def answer_two() -> int:
    """answer for question two"""
    total_fuel = 0
    input_list = get_input()

    for mass in input_list:
        total_fuel += get_fuel_for_mass(mass)

    return total_fuel


if __name__ == "__main__":
    print(f"answer one: {answer_one()}")
    print(f"answer one: {answer_two()}")
