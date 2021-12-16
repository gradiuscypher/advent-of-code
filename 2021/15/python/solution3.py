#!/usr/bin/env python3
# note: 1468 too low

import networkx as nx
import numpy as np
from numpy.lib.npyio import load
from pprint import pprint
from sys import argv

filename = argv[1]
grid = np.genfromtxt(filename, delimiter=1, dtype=int)

# print(grid)
# print(grid + 1)

# concat grids with plus 1,etc on both axis
grid = np.concatenate((grid, grid + 1, grid + 2, grid + 3, grid + 4), axis=0)
grid = np.concatenate((grid, grid + 1, grid + 2, grid + 3, grid + 4), axis=1)

grid[grid > 9] -= 9
# print(grid)

g = nx.DiGraph()

# iterate through neighbors
for x, y in np.ndindex(grid.shape):
    if x > 0:
        g.add_edge((x - 1, y), (x, y), weight=grid[(x, y)])

    if x < grid.shape[0] - 1:
        g.add_edge((x + 1, y), (x, y), weight=grid[(x, y)])

    if y > 0:
        g.add_edge((x, y - 1), (x, y), weight=grid[(x, y)])

    if y < grid.shape[1] - 1:
        g.add_edge((x, y + 1), (x, y), weight=grid[(x, y)])


print(nx.dijkstra_path_length(g, (0, 0), (grid.shape[0] - 1, grid.shape[1] - 1)))
