#!/usr/bin/python3

# enumerate defaultdict

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
rlen = lambda x: range(len(x))
inf = float('inf')
ninf = float('-inf')

n = gi()
a = gis()

x = [(v, i) for i, v in enumerate(a)]
x.sort()

best = inf
for i in range(len(x)-1):
    v, idx = x[i]
    if v == x[i+1][0]:
        best = min(best, x[i+1][1]-idx)

print(-1 if best == inf else best)
