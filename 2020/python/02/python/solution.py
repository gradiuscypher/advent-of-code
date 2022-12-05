#!/usr/bin/env python3

from sys import argv


def validate_policy(policy, input):
    psplit = policy.split(' ')
    pmin = int(psplit[0].split('-')[0])
    pmax = int(psplit[0].split('-')[1])
    ptarget = psplit[1]

    count = input.count(ptarget)
    return pmin <= count <= pmax


def validate_new_policy(policy, str_input):
    psplit = policy.split(' ')
    pos_one_idx = int(psplit[0].split('-')[0])
    pos_two_idx = int(psplit[0].split('-')[1])
    ptarget = psplit[1]

    check_list = [str_input[pos_one_idx-1] ==
                  ptarget, str_input[pos_two_idx-1] == ptarget]

    return check_list.count(True) == 1


if __name__ == '__main__':
    filename = argv[1]

    part2 = True

    with open(filename) as input:
        success_count = 0
        for line in input:
            policy, input = [s.strip() for s in line.split(':')]

            if part2:
                if validate_new_policy(policy, input):
                    success_count += 1
            else:
                if validate_policy(policy, input):
                    success_count += 1

    print(f"answer: {success_count}")
