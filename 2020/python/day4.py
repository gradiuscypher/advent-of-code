#!/usr/bin/env python3
"""
solution for day4
tags: parsing, regex
"""

import logging
import re
from helpers import get_input

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
ch = logging.StreamHandler()
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
ch.setFormatter(formatter)
logger.addHandler(ch)
ch.setLevel(logger.level)

TEST_INPUT = """
ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in
"""

def parse_passport(pass_inp, as_dict=False):
    """parse passport input"""
    inp = pass_inp.strip().split("\n\n")

    passports = []
    if as_dict:
        for p in inp:
            pd = {}
            p = p.replace("\n", " ")
            c_pass = [c.strip() for c in p.split(" ")]
            for c in c_pass:
                csplit = c.split(":")
                pd[csplit[0]] = csplit[1]

            passports.append(pd)

    else:
        for p in inp:
            p = p.replace("\n", " ")
            c_pass = [c.strip() for c in p.split(" ")]
            passports.append(c_pass)

    return passports


def part_one():
    """solution for part one"""
    # inp = TEST_INPUT
    inp = get_input(2020, 4)
    passports = parse_passport(inp)
    required_fields = ["byr:", "iyr:", "eyr:", "hgt:", "hcl:", "ecl:", "pid:"]

    # validate the passports
    valid_count = 0
    for p in passports:
        p_string = " ".join(p)

        is_valid = True
        for f in required_fields:
            if f not in p_string:
                is_valid = False

        if is_valid:
            valid_count += 1

    print("Part One:", valid_count)


def validate_passport(passport):
    """Validate the passport"""
    # validate that it has all required fields
    required_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    for f in required_fields:
        if f not in passport.keys():
            return False

    # validate byr
    byr = int(passport["byr"])
    if not 1920 <= byr <= 2002:
        return False

    # validate iyr
    iyr = int(passport["iyr"])
    if not 2010 <= iyr <= 2020:
        return False

    # validate eyr
    eyr = int(passport["eyr"])
    if not 2020 <= eyr <= 2030:
        return False

    # validate hgt
    hgt = passport["hgt"]
    if "cm" in hgt:
        hgt = int(hgt.split("cm")[0])
        if not 150 <= hgt <= 193:
            return False
    elif "in" in hgt:
        hgt = int(hgt.split("in")[0])
        if not 59 <= hgt <= 76:
            return False
    else:
        return False

    # validate hcl
    hcl = passport["hcl"]
    hcl_re = re.compile("^#[A-Fa-f0-9]{6}$")

    if not re.search(hcl_re, hcl):
        return False

    # validate ecl
    ecl = passport["ecl"]
    if ecl not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
        return False

    # validate pid
    pid = passport["pid"]
    pid_re = re.compile(r"^\d{9}$")

    if not re.search(pid_re, pid):
        return False

    # return true if all these passed
    return True

def part_two():
    """solution for part two"""
    inp = get_input(2020, 4)
    passports = parse_passport(inp, as_dict=True)

    total = 0
    for p in passports:
        if validate_passport(p):
            total += 1

    print("Part Two:", total)

if __name__ == "__main__":
    part_one()
    part_two()
