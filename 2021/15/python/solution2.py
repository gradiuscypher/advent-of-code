#!/usr/bin/env python3
# notes: 613 too low

from sys import argv
import networkx as nx
import numpy as np
from networkx.algorithms.matching import maximal_matching


def load_input(filename):
    grid = []

    with open(filename) as input:
        for line in input:
            grid.append([int(n) for n in line.strip()])

    return grid


def get_neighbors(point, grid):
    x, y = point
    nlist = []

    # # modification list
    mod_list = [
        (0, 1),  # north
        (0, -1),  # south
        (1, 0),  # east
        (-1, 0)  # west
    ]

    for m in mod_list:
        mx = x + m[0]
        my = y + m[1]

        if 0 <= mx < len(grid[y]) and 0 <= my < len(grid):
            nlist.append([mx, my])

    return nlist


def gen_adj_matrix(grid):
    adj = np.zeros((len(grid), len(grid)), dtype=int)

    for y in grid:
        for x in grid[y]:
            neighbors = get_neighbors((x, y), grid)

            for n in neighbors:
                adj[n[0], ]


if __name__ == '__main__':
    filename = argv[1]
    grid = load_input(filename)
    g = nx.Graph()

    for x in range(0, len(grid)):
        for y in range(0, len(grid)):
            neighbors = get_neighbors((x, y), grid)

            for n in neighbors:
                g.add_edge((x, y), (n[0], n[1]), weight=grid[n[1]][n[0]])

    max_dim = len(grid) - 1
    source = (0, 0)
    target = (9, 9)
    # sp = nx.dijkstra_path(g, source=start, target=target, weight='weight')
    sp = nx.single_source_dijkstra(g, source=source, target=target)
    # total = (nx.dijkstra_path_length(
    #     g, source=source, target=target, weight='weight'))

    print(sp)
    # print("len sp: ", len(sp))
    ptotal = 0
    for p in sp[1]:
        print("point:", grid[p[1]][p[0]])
        ptotal += (grid[p[1]][p[0]])
    # print("ptotal:", ptotal)
    # print('-------------')
    # print(total)
    # total += grid[6][2]
    # print(total)
