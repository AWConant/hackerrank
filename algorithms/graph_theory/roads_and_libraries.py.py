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

def dfs(g, start, seen):
    stack = [start]
    comp_size = 0
    while stack:
        u = stack.pop()
        if u not in seen:
            seen.add(u)
            comp_size += 1
            stack.extend(g[u])
    return comp_size


for _ in range(gi()):
    n, m, clib, croad = gis()

    g = defaultdict(list)
    for _ in range(m):
        u, v = gis()
        g[u].append(v)
        g[v].append(u)

    if clib < croad:
        print(n*clib)
        continue

    sizes = []
    seen = set()
    for i in range(1, n+1):
        if i not in seen:
            sizes.append(dfs(g, i, seen))

    ans = 0
    for size in sizes:
        ans += clib + croad*(size-1)

    print(ans)
