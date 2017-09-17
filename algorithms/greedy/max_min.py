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

n = gi()
k = gi()
xs = sorted([gi() for _ in range(n)])

best = inf
for lo in range(n-k+1):
    best = min(best, abs(xs[lo] - xs[lo+k-1]))

print(best)
