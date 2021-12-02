#!/usr/bin/env python3

import traceback
from sys import argv

filename = argv[1]

nlist = []
# ndict = {}

with open(filename) as input:
    for line in input:
        nlist.append(int(line))

# nprev = nlist[0]
# inc = 0
# for n in nlist[1:]:
#     if n > nprev:
#         print(f"{n} is bigger than {nprev}")
#         inc += 1
#     nprev = n

# print(inc)

# solution 2
index = 1
prev_total = nlist[0] + nlist[1] + nlist[2]
total = 0
inc = 0
for n in nlist[1:]:
    try:
        total = nlist[index] + nlist[index+1] + nlist[index+2]
        print(
            f"total: {(nlist[index], nlist[index+1], nlist[index+2])} {total} prev_total: {prev_total}")
        if total > prev_total:
            inc += 1
        print(f"==Index: {index} Len: {len(nlist)} Inc: {inc}")

        prev_total = total
        index += 1
    except:
        # print(f"Inc: {inc}")
        # print(traceback.format_exc())
        break
print(f"Inc: {inc}")
