#!/usr/bin/python3


import sys # stdout
# enumerate
from itertools import * # chain from_iterable product
from math import * # sqrt floor ceil
from copy import copy, deepcopy
from collections import * # Counter defaultdict deque
from queue import Queue
from heapq import heappush, heappop, heapify
from operator import * # itemgetter
from functools import reduce
from string import ascii_lowercase, ascii_uppercase

gi = lambda: int(input())
gis = lambda: list(map(int, input().split()))
gs = lambda: input()
skiplast = lambda x: range(len(x)-1)
is_even = lambda x: x%2 == 0

inf = float('inf')

def get_neighbors(grid, row, col, n, m):
    neighbors = []
    if row+1 < n:
        neighbors.append((row+1, col))
    if row-1 >= 0:
        neighbors.append((row-1, col))

    if col+1 < m:
        neighbors.append((row, col+1))
    if col-1 >= 0:
        neighbors.append((row, col-1))

    if row+1 < n and col+1 < m:
        neighbors.append((row+1, col+1))
    if row+1 < n and col-1 >= 0:
        neighbors.append((row+1, col-1))

    if row-1 >= 0 and col+1 < m:
        neighbors.append((row-1, col+1))
    if row-1 >= 0 and col-1 >= 0:
        neighbors.append((row-1, col-1))

    return [(r, c) for r, c in neighbors if grid[r][c] != 0]


def build_graph_from_grid(grid, n, m):
    graph = defaultdict(list)

    for r, c in product(range(n), range(m)):
        if grid[r][c] == 0:
            continue

        for neighbor in get_neighbors(grid, r, c, n, m):
            graph[(r, c)].append(neighbor)

    return graph

def get_connected_comp_size(graph, start, visited):
    comp_size = 0

    queue = Queue()
    queue.put(start)

    while not queue.empty():
        node = queue.get()
        if node not in visited:
            visited.add(node)
            comp_size += 1
            for neighbor in graph[node]:
                queue.put(neighbor)

    return comp_size


def get_largest_connected_comp_size(grid, n, m):
    graph = build_graph_from_grid(grid, n, m)

    largest = -inf
    visited = set()
    for node in product(range(n), range(m)):
        if node not in visited:
            largest = max(largest, get_connected_comp_size(graph, node, visited))

    return largest


n = gi()
m = gi()

grid = [gis() for _ in range(n)]

print(get_largest_connected_comp_size(grid, n, m))
