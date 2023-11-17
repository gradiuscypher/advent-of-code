#!/usr/bin/env python3
"""
solution for day6
tags: graph, shortest path
"""

import logging
import networkx as nx
from helpers import get_input

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
ch = logging.StreamHandler()
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
ch.setFormatter(formatter)
logger.addHandler(ch)
ch.setLevel(logger.level)


def part_one():
    """solution for part one"""
    input_nodes = get_input(6)
    has_node = []
    g = nx.Graph()
    for line in input_nodes.split("\n"):
        nodes = line.split(")")
        if len(nodes) == 2:
            for node in nodes:
                if node not in has_node:
                    has_node.append(node)
                    g.add_node(node)
                g.add_edge(nodes[0], nodes[1])

    shortest_paths = dict(nx.all_pairs_shortest_path_length(g))
    total = 0
    for node in has_node:
        total += shortest_paths[node]["COM"]
    print(f"Total for part one: {total}")


def part_two(inmap=None):
    """solution for part two"""
    if not inmap:
        inmap = get_input(6)

    has_node = []
    g = nx.Graph()
    for line in inmap.split("\n"):
        nodes = line.split(")")
        if len(nodes) == 2:
            nodes = [node.strip() for node in nodes]
            for node in nodes:
                if node not in has_node:
                    has_node.append(node)
                    g.add_node(node)
                g.add_edge(nodes[0], nodes[1])
    shortest_paths = dict(nx.all_pairs_shortest_path_length(g))
    total = shortest_paths["SAN"]["YOU"] - 2
    print(f"Total for part two: {total}")


if __name__ == "__main__":
    # part_one()

    test_input = """
    COM)B
    B)C
    C)D
    D)E
    E)F
    B)G
    G)H
    D)I
    E)J
    J)K
    K)L
    K)YOU
    I)SAN
    """

    part_two()
