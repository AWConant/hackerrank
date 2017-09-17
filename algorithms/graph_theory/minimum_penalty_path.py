#!/usr/bin/env python3

import sys

from itertools import *
from math import *
from collections import *
from queue import Queue
from heapq import heappush, heappop
from operator import itemgetter
from functools import reduce
from string import ascii_lowercase, ascii_uppercase

gi = lambda: int(input())
gis = lambda: list(map(int, input().split()))
gs = lambda: input()
inf = float('inf')

MAX_COST = 1024

n, m = gis()

g = defaultdict(dict)
for _ in range(m):
    u, v, c = gis()
    try:
        g[u][v] = g[v][u] = min(c, g[u][v])
    except KeyError:
        g[u][v] = g[v][u] = c

start, end = gis()

visited = defaultdict(set)
visited[start].add(0)

q = deque([(start, 0)])
while q:
    node, cost = q.popleft()
    for neighbor in g[node].keys():
        new_cost = cost | g[node][neighbor]
        if new_cost not in visited[neighbor]:
            visited[neighbor].add(new_cost)
            q.append( (neighbor, new_cost) )

for cost in range(MAX_COST):
    if cost in visited[end]:
        print(cost)
        break
else:
    print(-1)
