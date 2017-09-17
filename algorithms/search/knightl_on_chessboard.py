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

def get_neighbors(r, c, a, b, n):
    if r+a < n:
        if c+b < n:
            yield r+a, c+b
        if c-b >= 0:
            yield r+a, c-b
    if r-a >= 0:
        if c+b < n:
            yield r-a, c+b
        if c-b >= 0:
            yield r-a, c-b
    if r+b < n:
        if c+a < n:
            yield r+b, c+a
        if c-a >= 0:
            yield r+b, c-a
    if r-b >= 0:
        if c+a < n:
            yield r-b, c+a
        if c-a >= 0:
            yield r-b, c-a

def bfs(a, b, n):
    seen = set()
    END = (n-1, n-1)
    q = deque([((0,0), 0)])
    while q:
        cur, d = q.popleft()
        r, c = cur
        if cur == END:
            return d
        if cur not in seen:
            seen.add(cur)
            for neighbor in get_neighbors(r, c, a, b, n):
                q.append( (neighbor, d+1) )
    return -1

n = gi()

dp = dict()
for a in range(1, n):
    for b in range(1, n):
        pair = (min(a, b), max(a, b))
        if pair not in dp:
            a, b = pair
            dp[pair] = bfs(a, b, n)
        print(dp[pair], end=' ')
    print()
