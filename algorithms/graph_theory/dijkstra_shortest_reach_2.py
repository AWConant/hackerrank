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

def dijkstra(g, w, n, s):
    dist = [inf for _ in range(n)]
    dist[s] = 0

    pq = []

    for v in range(n):
        heappush(pq, (dist[v], v))

    while pq:
        dist_u, u = heappop(pq)
        for v in g[u]:
            alt = dist_u + w[(u, v)]
            if alt < dist[v]:
                dist[v] = alt
                heappush(pq, (alt, v)) 

    return dist

def main():
    for _ in range(gi()):
        n, m = input().split()
        n = int(n)
        m = int(m)

        g = defaultdict(list)
        w = dict()
        for _ in range(m):
            x, y, r = input().split()
            x = int(x)-1
            y = int(y)-1
            r = int(r)
            if (x, y) not in w:
                w[(x, y)] = w[(y, x)] = r
                g[x].append(y)
                g[y].append(x)
            elif w[(x, y)] > r:
                w[(x, y)] = w[(y, x)] = r

        s = gi()-1
        dist = dijkstra(g, w, n, s)
        dist = [v if v != inf else -1 for i, v in enumerate(dist) if i != s]
        print(*dist)

main()
