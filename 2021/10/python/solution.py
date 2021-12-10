#!/usr/bin/env python3

import statistics
from sys import argv

scores = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

closing = {
    '(': 1,
    '[': 2,
    '{': 3,
    '<': 4
}


def check_balance(input_line):
    brackets = []

    for bracket in input_line.strip():
        if bracket in ['(', '<', '[', '{']:
            brackets.append(bracket)

        else:
            if not brackets:
                return False

            c_bracket = brackets.pop()

            if c_bracket == '(' and bracket != ')':
                return (False, bracket)
            if c_bracket == '<' and bracket != '>':
                return (False, bracket)
            if c_bracket == '[' and bracket != ']':
                return (False, bracket)
            if c_bracket == '{' and bracket != '}':
                return (False, bracket)

    if brackets:
        return (False, brackets)
    return True


if __name__ == '__main__':
    filename = argv[1]
    part1 = False

    # part one
    if part1:
        with open(filename) as input:
            total = 0
            for line in input:
                result = check_balance(line)
                if len(result[1]) == 1:
                    total += scores[result[1]]
            print("part1:", total)

    # part two
    else:
        closing_scores = []

        with open(filename) as input:
            leftovers = []
            for line in input:
                result = check_balance(line)
                if len(result[1]) > 1:
                    leftovers.append(result[1])
        for brackets in leftovers:
            closing_string = ""
            closing_cost = 0

            while brackets:
                bracket = brackets.pop()

                if bracket == '(':
                    closing_string += ")"
                    closing_cost = (closing_cost * 5) + closing[bracket]
                if bracket == '<':
                    closing_string += ">"
                    closing_cost = (closing_cost * 5) + closing[bracket]
                if bracket == '[':
                    closing_string += "]"
                    closing_cost = (closing_cost * 5) + closing[bracket]
                if bracket == '{':
                    closing_string += "}"
                    closing_cost = (closing_cost * 5) + closing[bracket]

            closing_scores.append(closing_cost)
        print(f"part2: {statistics.median(closing_scores)}")
