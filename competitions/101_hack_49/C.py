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

def get_parent_pointers(g, root):
    parent_of = {root: None}

    new_g = defaultdict(list)
    queue = deque([ (root, None) ])
    while queue:
        cur, prev = queue.popleft()
        for child in g[cur]:
            if child != prev:
                parent_of[child] = cur
                queue.append( (child, cur) )
                new_g[cur].append(child)

    return parent_of, new_g

n = gi()
c = gis()

g = defaultdict(list)
w = defaultdict(dict)

for _ in range(n-1):
    u, v, we = gis()
    g[u].append(v)
    g[v].append(u)
    w[u][v] = we
    w[v][u] = we

parent_of, new_g = get_parent_pointers(g, 1)
leaves = [node for node in range(n) if len(new_g[node]) == 0]

print(parent_of)

child_count = defaultdict(int)
for leaf in leaves:
    child_count[leaf] = 0

q = deque(leaves)
while q:
    u = q.popleft()
    child_count[parent_of[u]] += child_count[u]+1
    q.append(parent_of[u])

print(child_count)
