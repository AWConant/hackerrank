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

def get_neighbors(rods):
    for i in range(4):
        if not rods[i]:
            continue

        for j in range(4):
            if j == i:
                continue

            if len(rods[j]) == 0 or rods[j][-1] > rods[i][-1]:
                yield i,j
            

n = gi()
rods = [[], [], [], []]
for i, d in enumerate(gis(), start=1):
    rods[d-1].append(i)
start = tuple([tuple(sorted(rod, reverse=True)) for rod in rods])

END = (tuple(reversed(range(1, n+1))), tuple(), tuple(), tuple())
visited = set([start])
q = deque([(start, 0)])
while q:
    node, dist = q.popleft()
    if node == END:
        break

    for i,j in get_neighbors(node):
        neighbor = [list(rod) for rod in node]
        neighbor[j].append(neighbor[i].pop())
        neighbor[1:] = sorted(neighbor[1:], key=lambda x: x[-1] if x else 0)
        neighbor = tuple(tuple(rod) for rod in neighbor)

        if neighbor not in visited:
            visited.add(neighbor)
            q.append( (neighbor, dist+1) )

print(dist)
