#!/usr/bin/env python3
"""
solution for day5
tags:
"""

import logging
import queue
from itertools import zip_longest
from multiprocessing import Process, Queue, Value
from helpers import get_input

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
ch = logging.StreamHandler()
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
ch.setFormatter(formatter)
logger.addHandler(ch)
ch.setLevel(logger.level)

IS_TESTING = True
TEST_INP = """
seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4
"""


def mapping_parser(name, mappings):
    """parses a mapping. lol this doesn't work for the real input"""
    source_list = []
    dest_list = []

    logger.debug("Starting individual mapping parse: %s", name)
    for line in mappings:
        split_line = line.split(" ")
        dest_start = int(split_line[0])
        source_start = int(split_line[1])
        range_len = int(split_line[2])
        logger.debug("Mapping parse lines split")
        logger.debug(
            "dest_start = %s | source_start = %s | range_len = %s",
            dest_start,
            source_start,
            range_len,
        )

        logger.debug("Starting mapping parse source list comprehension")
        source_list += [n + source_start for n in range(0, range_len)]
        logger.debug("Starting mapping parse dest list comprehension")
        dest_list += [n + dest_start for n in range(0, range_len)]

    return (source_list, dest_list)


def almanac_parser(inp):
    """parses the entire almanac, lol swapfile go brrrr"""
    logger.debug("Starting almanac parsing")
    split_alm = inp.split("\n\n")

    seeds = [int(n) for n in split_alm[0].split(":")[1].strip().split(" ")]

    mappings = {}

    for map_inp in split_alm[2:]:
        split_map = map_inp.split("\n")
        name = split_map[0].split(" ")[0]
        source_list, dest_list = mapping_parser(name, split_map[1:])

        mappings[name] = (source_list, dest_list)

    return seeds, mappings


def grouper(iterable, n, fillvalue=None):
    """stolen: https://stackoverflow.com/questions/434287/how-to-iterate-over-a-list-in-chunks"""
    args = [iter(iterable)] * n
    return zip_longest(*args, fillvalue=fillvalue)


def process_steps(seed, steps):
    """go from seed to location via steps"""
    logger.debug("Processing steps for seed: %s", seed)
    for step in steps:
        split_step = step.split("\n")
        step_name = split_step[0].split(" ")[0]

        for step_range in split_step[1:]:
            split_range = step_range.split(" ")
            dest_start = int(split_range[0])
            source_start = int(split_range[1])
            distance = int(split_range[2])

            # check if our seed is in any of the steps, if it is, generate the lookup
            if source_start <= seed <= source_start + distance:
                # seed = (seed - source_start + distance)
                seed = (seed - source_start) + dest_start
                logger.debug("Assigning new seed value for %s: %s", step_name, seed)
                break

    return seed


def parse_input(inp):
    """parses input into seeds and list of step strings"""
    split_input = inp.split("\n\n")
    seeds = [int(n) for n in split_input[0].split(":")[1].strip().split(" ")]
    steps = split_input[1:]
    return seeds, steps


def parse_seed_range(inp):
    """parses seed range for part two giving list of all seeds"""
    seed_list = []
    parsed_seeds = inp.split("\n\n")[0].split(":")[1].strip().split(" ")
    for start, length in grouper(parsed_seeds, 2):
        start = int(start)
        length = start + int(length)
        seed_list += range(start, length)
    return seed_list


def part_one(debug):
    """solution for part one"""
    inp = get_input(2023, 5)
    if debug:
        inp = TEST_INP
    inp = inp.strip()
    seeds, steps = parse_input(inp)

    low_result = None
    for seed in seeds:
        result = process_steps(seed, steps)
        if not low_result:
            low_result = result
        elif result < low_result:
            low_result = result

    print("Part One:", low_result)


def part_two(debug):
    """solution for part two"""
    inp = get_input(2023, 5)
    if debug:
        inp = TEST_INP
    inp = inp.strip()
    seeds = parse_seed_range(inp)
    _, steps = parse_input(inp)

    remaining = len(seeds)
    low_result = None
    for seed in seeds:
        remaining -= 1
        logger.info("Remaining seeds: %s", remaining)
        result = process_steps(seed, steps)
        if not low_result:
            low_result = result
        elif result < low_result:
            low_result = result

    print("Part Two:", low_result)


def part_two_mp_worker(seed_queue: Queue, steps, low_result):
    """multiprocess worker for part two"""
    while True:
        try:
            seed = seed_queue.get_nowait()
        except queue.Empty:
            print("Queue empty:", low_result.value)
            return low_result.value

        result = process_steps(seed, steps)
        if low_result.value == -1:
            low_result.value = result
        elif result < low_result.value:
            low_result.value = result


def part_two_mp(debug):
    """part two with multiprocessing"""
    inp = get_input(2023, 5)
    if debug:
        inp = TEST_INP
    inp = inp.strip()
    print("Parsing seed range")
    seeds = parse_seed_range(inp)
    print("Seed range complete")
    _, steps = parse_input(inp)

    seed_queue = Queue()
    for seed in seeds:
        seed_queue.put(seed)

    # create the processes
    processes = []
    values = []
    for _ in range(8):
        r_value = Value("i", -1)
        p = Process(
            target=part_two_mp_worker,
            args=(seed_queue, steps, r_value),
        )
        processes.append(p)
        values.append(r_value)
        p.start()

    for p in processes:
        print(p.join())

    low_value = None
    for v in values:
        if not low_value and v.value != -1:
            low_value = v.value

        elif low_value and v.value < low_value and v.value != -1:
            low_value = v.value

    print("Part 2:", low_value)


def part_two_simple(inp):
    """stop doing math"""
    inp = get_input(2023, 5)
    inp = inp.strip()
    inp = [line.strip("\n") for line in inp.split("\n")]
    seeds = [*map(int, inp[0].split(": ")[1].split())]
    maps = [
        [[*map(int, n.split())] for n in i.split("\n")[1:]]
        for i in "\n".join(inp[2:]).split("\n\n")
    ]
    for m in maps:
        print(m)

    locs = []
    seed_pairs = [
        (seeds[i], seeds[i] + seeds[i + 1] - 1) for i in range(0, len(seeds), 2)
    ]
    print("SEED PARIS:", seed_pairs)
    for pair in seed_pairs:
        pairs_left = [pair]
        result = []

        for m in maps:
            print("Current map:", m)
            while pairs_left:
                c_pair = pairs_left.pop()
                print("c_pair:", c_pair)
                print("PAIRS LEFT:", pairs_left)
                for dest, src, m_range in m:
                    if c_pair[1] < src or src + m_range <= c_pair[0]:
                        continue
                    elif src <= c_pair[0] <= c_pair[1] < src + m_range:
                        offset = c_pair[0] - src
                        result.append(
                            (dest + offset, dest + offset + c_pair[1] - c_pair[0])
                        )
                        break
                    elif c_pair[0] < src <= c_pair[1] < src + m_range:
                        offset = c_pair[1] - src
                        result.append((dest, dest + offset))
                        pairs_left.append((c_pair[0], src - 1))
                        break
                    elif src <= c_pair[0] < src + m_range <= c_pair[1]:
                        offset = c_pair[0] - src
                        result.append((dest + offset, dest + m_range - 1))
                        pairs_left.append((src + m_range, c_pair[1]))
                        break
                    elif c_pair[0] < src <= src + m_range <= c_pair[1]:
                        result.append((dest, dest + m_range - 1))
                        pairs_left.append((c_pair[0], src - 1))
                        pairs_left.append((src + m_range, c_pair[1]))
                        break
                else:
                    result.append(c_pair)
            pairs_left = result
            result = []
        locs.extend(pairs_left)

    # print(locations)
    print("Part Two:", min(i[0] for i in locs))


if __name__ == "__main__":
    # part_one(debug=False)
    # part_two(False)
    # part_two_mp(False)
    part_two_simple(TEST_INP)
