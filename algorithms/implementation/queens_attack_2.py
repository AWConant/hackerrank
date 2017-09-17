#!/usr/bin/python3

import sys

from itertools import *
from math import *
from collections import *
from queue import Queue
from heapq import heappush, heappop
from operator import *
from functools import reduce
from string import ascii_lowercase, ascii_uppercase

gi = lambda: int(input())
gis = lambda: list(map(int, input().split()))
gs = lambda: input()

n, k = gis()
rq, cq = gis()
obs = set([tuple(gis()) for _ in range(k)])

ans = -8

for i in range(1, n+1):
    obs.add( (0, i) )
    obs.add( (i, 0) )
    obs.add( (n+1, i) )
    obs.add( (i, n+1) )

obs.add( (0, 0) )
obs.add( (n+1, n+1) )
obs.add( (0, n+1) )
obs.add( (n+1, 0) )

# up
r, c = rq, cq
while (r, c) not in obs:
    ans += 1
    r += 1

# left
r, c = rq, cq
while (r, c) not in obs:
    ans += 1
    c -= 1

# right
r, c = rq, cq
while (r, c) not in obs:
    ans += 1
    c += 1

# down
r, c = rq, cq
while (r, c) not in obs:
    ans += 1
    r -= 1

# nw
r, c = rq, cq
while (r, c) not in obs:
    ans += 1
    r += 1
    c -= 1

# ne
r, c = rq, cq
while (r, c) not in obs:
    ans += 1
    r += 1
    c += 1

# sw
r, c = rq, cq
while (r, c) not in obs:
    ans += 1
    r -= 1
    c -= 1

# se
r, c = rq, cq
while (r, c) not in obs:
    ans += 1
    r -= 1
    c += 1

print(ans)
