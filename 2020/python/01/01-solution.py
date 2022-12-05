#!/usr/bin/env python3

from sys import argv

filename = argv[1]

nlist = []

with open(filename) as input:
    for line in input:
        nlist.append(int(line))

# for n in nlist:
#     for n2 in nlist:
#         if n + n2 == 2020:
#             print(f"Found: {n}, {n2}")
#             print(f"mul: {n * n2}")

for n1 in nlist:
    for n2 in nlist:
        for n3 in nlist:
            if n1 + n2 + n3 == 2020:
                print(f"Mul: {n1*n2*n3}")
