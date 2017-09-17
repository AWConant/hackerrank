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

PORTKEY = '*'
START = 'M'
TREE = 'X'

def get_neighbors(grid, r, c, n, m):
    if r+1 < n and grid[r+1][c] != TREE:
        yield r+1, c
    if r-1 >= 0 and grid[r-1][c] != TREE:
        yield r-1, c
    if c+1 < m and grid[r][c+1] != TREE:
        yield r, c+1
    if c-1 >= 0 and grid[r][c-1] != TREE:
        yield r, c-1

def build_graph(grid, n, m):
    graph = dict()

    for row, col in product(range(n), range(m)):
        if grid[row][col] != TREE:
            graph[(row, col)] = list(get_neighbors(grid, row, col, n, m))

    return graph

def get_wand_wave_count(graph, start, end):
    visited = set()

    queue = Queue()
    queue.put( (start, 0) )

    while not queue.empty():
        node, distance = queue.get()

        if node == end:
            return distance

        visited.add(node)
        neighbors = [neighbor for neighbor in graph[node] if neighbor not in visited]

        if len(neighbors) > 1:
            distance += 1

        for neighbor in neighbors:
            queue.put( (neighbor, distance) )

    raise Exception("Didn't find a path.")

def get_end_coord(grid, n, m):
    for row, col in product(range(n), range(m)):
        if grid[row][col] == PORTKEY:
            return row, col

    raise Exception("Didn't find a portkey.")

def get_start_coord(grid, n, m):
    for row, col in product(range(n), range(m)):
        if grid[row][col] == START:
            return row, col

    raise Exception("Didn't find a start.")

def get_guess_result(grid, n, m, k):
    graph = build_graph(grid, n, m)
    start = get_start_coord(grid, n, m)
    end = get_end_coord(grid, n, m)

    wave_count = get_wand_wave_count(graph, start, end)
    if k == wave_count:
        return 'Impressed'
    else:
        return 'Oops!'

for _ in range(gi()):
    n, m = gis()
    grid = [list(gs()) for _ in range(n)]
    k = gi()

    print(get_guess_result(grid, n, m, k))
