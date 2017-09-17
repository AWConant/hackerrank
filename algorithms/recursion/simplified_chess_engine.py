#!/usr/bin/python3


import sys # stdout enumerate
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

GRID_DIM = 4

WHITE = 1
BLACK = 0

for _ in range(gi()):
    w, b, m = gis()
    grid = [[None]*GRID_DIM]*GRID_DIM

    for _ in range(w):
        piece, c, r = gs().split()
        r = GRID_DIM-int(r)
        c = ord(c)-65

        grid[r][c] = (piece, WHITE)

    for _ in range(b):
        piece, c, r = gs().split()
        r = GRID_DIM-int(r)
        c = ord(c)-65

        grid[r][c] = (piece, BLACK)



    for row in grid:
        print(*row)
