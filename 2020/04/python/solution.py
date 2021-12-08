#!/usr/bin/env python3

from copy import deepcopy
from sys import argv

required_fields = set([
    'byr',
    'iyr',
    'eyr',
    'hgt',
    'hcl',
    'ecl',
    'pid',
])


def parse_input(filename):
    passport_list = []

    new_passport = ""
    with open(filename) as input_file:
        for line in input_file:
            # this is an empty line, add the current parsing passport to the list
            if len(line) <= 2:
                passport_list.append(new_passport.strip().split(' '))
                new_passport = ""
            else:
                new_passport += line.replace('\n', ' ')

    return passport_list


def validate_passport(passport_list):
    valid_passports = 0

    for passport in passport_list:
        valid_fields = 0

        fields = set([f.split(':')[0] for f in passport])

        missing_fields = required_fields - fields

        if len(missing_fields) == 0:
            valid_passports += 1
        # else:
        #     print(passport, missing_fields, len(fields))

    return valid_passports


if __name__ == '__main__':
    filename = argv[1]

    passport_list = parse_input(filename)
    print(validate_passport(passport_list))
