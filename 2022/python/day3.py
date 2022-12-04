#!/usr/bin/env python3

def calculate_value(input: str) -> int:
    print(input)
    if input[0].islower():
        return ord(input[0]) - 96
    else:
        return ord(input[0]) - 38


def part1(input: list):
    total = 0
    for line in input:
        first = set(line[0:len(line) // 2])
        second = set(line[len(line) // 2:len(line)])
        intersect = first.intersection(second)
        total += calculate_value(intersect.pop()[0])
    print(f"Part1: {total}")


def part2(input: list):
    total = 0


if __name__ == "__main__":
    input_name = "input/day3_example.txt"
    with open(input_name) as input:
        lines = input.readlines()
        part1(lines)
        part2(lines)
