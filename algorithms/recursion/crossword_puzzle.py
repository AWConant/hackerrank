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

ACROSS = 0
DOWN = 1

def validate_word_placement(placement, blank_grid):
    for word, ((r, c), direction) in placement:
        if direction == DOWN:
            for ch, rr in zip(word, range(r, r+len(word))):
                if blank_grid[rr][c] != '-' and blank_grid[rr][c] != ch:
                    return None
                blank_grid[rr][c] = ch
        else:
            for ch, cc in zip(word, range(c, c+len(word))):
                if blank_grid[r][cc] != '-' and blank_grid[r][cc] != ch:
                    return None
                blank_grid[r][cc] = ch
    
    return blank_grid

grid = [list(gs()) for _ in range(10)]
words = gs().split(';')

starts = defaultdict(list)
for r, c in product(range(10), range(10)):
    if grid[r][c] == '-':
        for word in words:
            if r+len(word) <= 10 and all(grid[rr][c] == '-' for rr in range(r, r+len(word))):
                starts[word].append( ((r, c), DOWN) )
            if c+len(word) <= 10 and all(grid[r][cc] == '-' for cc in range(c, c+len(word))):
                starts[word].append( ((r, c), ACROSS) )

paired = [zip(repeat(word), points) for word, points in starts.items()]
for placement in product(*paired):
    ans = validate_word_placement(placement, deepcopy(grid))
    if ans is not None:
        break

for row in ans:
    print(*row, sep='')
