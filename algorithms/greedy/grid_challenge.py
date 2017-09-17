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

for _ in range(gi()):
    n = gi()
    grid = [sorted(list((gs()))) for _ in range(n)]
    for r, c in product(range(n-1), range(n)):
        if grid[r][c] > grid[r+1][c]:
            print('NO')
            break
    else:
        print('YES')

