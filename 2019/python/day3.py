#!/usr/bin/env python3
"""
solution for day3
tags:
"""

from helpers import get_input
from shapely.geometry import LineString, Point
import matplotlib.pyplot as plt
from math import dist


def part_one(wires):
    """solution for part one"""
    # plot the lines
    # for wire in wires:
    #     for line in wire:
    #         print(line)
    #         plt.plot(*line.xy)

    # get the intersections
    intersections = find_intersections(wires)

    # get the shortest dist point
    lowest_point = Point(0, 0)
    lowest_dist = manhattan(intersections[0])

    for intersection in intersections:
        mandist = manhattan(intersection)
        if mandist <= lowest_dist:
            lowest_dist = mandist
            lowest_point = intersection

    print("lowpoint:", lowest_point, "lowdist:", lowest_dist)

    # show the plots
    # plt.show()


def part_two(wires):
    """solution for part two"""
    print("wires:", wires)

    # get the intersections
    intersections = find_intersections(wires)
    print(intersections)
    print()

    # count the number of steps for each intersection
    # count_intersect_steps(intersections[1], wires[0])
    # count_intersect_steps(intersections[1], wires[1])
    lowest_step_count = 1e10
    for intersection in intersections:
        intersection_steps = 0
        for wire in wires:
            intersection_steps += count_intersect_steps(intersection, wire)
        if intersection_steps < lowest_step_count:
            lowest_step_count = intersection_steps
    print("lowest intersection steps:", lowest_step_count)


def count_intersect_steps(int_point, wire):
    """count the steps to reach the intersect for the wire"""
    total_steps = 0
    for step in wire:
        if step.distance(int_point) < 1e-8:
            # print("strike:", step)
            # print("final add step:", step)
            # print("final step.xy", step.xy)
            step_dist = abs(
                (step.xy[0][0] + step.xy[1][0]) - (int_point.y + int_point.x)
            )
            # print("final step_dist:", step_dist)
            total_steps += step_dist
            break

        # print("add step:", step)
        # print("step.xy", step.xy)
        # print("steps:", step.xy[0][0], step.xy[1][0], step.xy[0][1], step.xy[1][1])
        step_dist = abs(
            (step.xy[0][0] + step.xy[1][0]) - (step.xy[0][1] + step.xy[1][1])
        )
        # print("step_dist:", step_dist)
        # print()
        total_steps += step_dist
    return total_steps


def build_wire(step_list: list[str]) -> list[LineString]:
    """builds a wire based on steps"""
    current_pos = (0, 0)
    segments: list[LineString] = []

    current_pos = (0, 0)
    for step in step_list:
        val = int(step[1:])
        new_pos = current_pos

        match step[0]:
            case "U":
                new_pos = current_pos[0], current_pos[1] + val
            case "D":
                new_pos = current_pos[0], current_pos[1] - val
            case "L":
                new_pos = current_pos[0] - val, current_pos[1]
            case "R":
                new_pos = current_pos[0] + val, current_pos[1]

        segments.append(LineString([current_pos, new_pos]))
        current_pos = new_pos

    return segments


def find_intersections(wire_list: list[list[LineString]]):
    """finds all intersections of the two wires"""
    all_inters = []

    for wire1 in wire_list[0]:
        for wire2 in wire_list[1]:
            inter = wire1.intersection(wire2)
            if inter:
                all_inters.append(inter)

    all_inters.remove(Point(0, 0))
    return all_inters


def manhattan(t_point):
    vec1 = [0, 0, t_point.x, 0]
    vec2 = [0, 0, 0, t_point.y]
    return sum(abs(val1 - val2) for val1, val2 in zip(vec1, vec2))


if __name__ == "__main__":
    test_input = [
        "R8,U5,L5,D3\nU7,R6,D4,L4",
        "R75,D30,R83,U83,L12,D49,R71,U7,L72\nU62,R66,U55,R34,D71,R55,D58,R83",
        "R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51\nU98,R91,D20,R16,D67,R40,U7,R15,U6,R7",
    ]

    # input_text = test_input[2]
    input_text = get_input(3)

    # build all the wires
    all_wires = []
    for line in input_text.split("\n"):
        steps = line.split(",")
        if len(steps) > 1:
            all_wires.append(build_wire(steps))

    # part_one(all_wires)
    part_two(all_wires)
