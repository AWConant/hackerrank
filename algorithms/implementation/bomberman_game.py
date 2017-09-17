#!/usr/bin/python3

# enumerate defaultdict

import sys

from itertools import *
from math import *
from copy import copy, deepcopy
from collections import *
from queue import Queue
from heapq import heappush, heappop
from operator import *
from functools import reduce
from string import ascii_lowercase, ascii_uppercase

gi = lambda: int(input())
gis = lambda: list(map(int, input().split()))
gs = lambda: input()
skiplast = lambda x: range(len(x)-1)
inf = float('inf')

def print_grid(grid):
    for row in grid:
        for n in row:
            if n == 0:
                sys.stdout.write('.')
            else:
                sys.stdout.write('O')
        sys.stdout.write('\n')

def prep(s):
    return list(map(int, s.replace('.', '0').replace('O', '3')))

def get_adj(i, j, r, c):
    return [(ii, jj) for ii, jj in ((i+1,j),(i,j+1),(i-1,j),(i,j-1)) if 0 <= ii < r and 0 <= jj < c]

def main():
    r, c, n = gis()
    grid = [prep(gs()) for _ in range(r)]

    if n%2 == 0:
        grid = [[1]*c for _ in range(r)]
    else:
        adj = {(i,j): get_adj(i, j, r, c) for (i, j) in product(range(r), range(c))}

        for t in range(1, (4+n%4 if n > 4 else n)+1):
            if t%2 == 0:
                for i, j in product(range(r), range(c)):
                    if grid[i][j] == 0:
                        grid[i][j] = t+3

            to_destroy = []
            for i, j in product(range(r), range(c)):
                if grid[i][j] == t:
                    to_destroy.append( (i, j) )
                    to_destroy.extend(adj[(i, j)])

            for i, j in to_destroy:
                grid[i][j] = 0

    print_grid(grid)

main()
