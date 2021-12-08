#!/usr/bin/env python3

"""[notes]
1 is the only 2 segments
2 is 5 segments
3 is 5 segments (this is the one 5 segment that shares two segments with 1)
4 is the only 4 segments
5 is 5 segments (just one different than 6)
6 is 6 segments (and is one segment diff from 5)
7 is the only 3 segments
8 is the only 7 segments (this might not be useful because its all segments?)
9 is 6 segments (once we find 6, we can test the diff between 9 and 0 for the 6, whichever one has a match with 4 that isn't in 0 is the 9)
0 is 6 segments (same tbh)

order of solving:
- find 1, 4, 7, 8
- find 9 via a 6segment that has a match with 4
- find 3 via 5 segment that uses both of 1's segments
- find 6 via the 6segment thats one diff from 5 (which is a 5seg)
- find 5 via the 5segment thats one different than 6
- find 0 by remaining 6segment
- find 2 via remaing 5segment

line one of input file:
bgcfda gecbda abdgf aedfbg eda efcbd ae agfe bdefagc fbeda | ae egdafb ea fcdeb ==

manual attempt to validate logic
ae      == 1
eda     == 7
agfe    == 4
abdgf   == 5
efcbd   == 2
fbeda   == 3
bgcfda  == 6
gecbda  == 0
aedfbg  == 9
bdefagc == 8
"""

from pprint import pprint
import re
from sys import argv


if __name__ == '__main__':
    filename = argv[1]

    with open(filename) as input:
        final_val = 0
        for line in input:
            solve_dict = {}
            num_dict = {}
            output_val = line.split('|')[1].split()
            pattern_val = line.split('|')[0].split()

            # find one
            r = re.compile('..$')
            solve_dict[''.join(
                sorted(list(filter(r.match, pattern_val))[0]))] = 1
            num_dict[1] = ''.join(
                sorted(list(filter(r.match, pattern_val))[0]))

            # find four
            r = re.compile('....$')
            solve_dict[''.join(
                sorted(list(filter(r.match, pattern_val))[0]))] = 4
            num_dict[4] = ''.join(
                sorted(list(filter(r.match, pattern_val))[0]))

            # find seven
            r = re.compile('...$')
            solve_dict[''.join(
                sorted(list(filter(r.match, pattern_val))[0]))] = 7
            num_dict[7] = ''.join(
                sorted(list(filter(r.match, pattern_val))[0]))

            # find eight
            r = re.compile('.......$')
            solve_dict[''.join(
                sorted(list(filter(r.match, pattern_val))[0]))] = 8
            num_dict[8] = ''.join(
                sorted(list(filter(r.match, pattern_val))[0]))

            # find 9 via a 6segment that has a match with 4
            r = re.compile('......$')
            six_segments = list(filter(r.match, pattern_val))
            for s in six_segments:
                if 0 not in [c in s for c in num_dict[4]]:
                    solve_dict[''.join(sorted(s))] = 9
                    num_dict[9] = s
                    six_segments.remove(s)

            # find 3 via 5segment that uses both of 1 segements
            r = re.compile('.....$')
            five_segments = list(filter(r.match, pattern_val))
            for s in five_segments:
                if 0 not in [c in s for c in num_dict[1]]:
                    solve_dict[''.join(sorted(s))] = 3
                    num_dict[3] = s
                    five_segments.remove(s)

            # find 5,6 via the 5segment thats one diff from the 6seg
            for s in six_segments:
                for f in five_segments:
                    if 0 not in [c in s for c in f]:
                        solve_dict[''.join(sorted(f))] = 5
                        num_dict[5] = f
                        five_segments.remove(f)

                        solve_dict[''.join(sorted(s))] = 6
                        num_dict[6] = s
                        six_segments.remove(s)

            # 0 is the remaining 6 segment
            sorted_six = ''.join(sorted(six_segments[0]))
            solve_dict[sorted_six] = 0

            # 2 is the remaining 5 segment
            sorted_five = ''.join(sorted(five_segments[0]))
            solve_dict[sorted_five] = 2

            o_string = ""
            for o in output_val:
                sorted_o = ''.join(sorted(o))
                o_string += str(solve_dict[sorted_o])

            o_num = int(o_string)
            print(output_val)
            print(o_num)
            print(solve_dict)
            print()
            final_val += o_num
    print(final_val)
