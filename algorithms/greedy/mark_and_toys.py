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

n, k = gis()
p = sorted(gis())

total = 0
idx = 0
while total + p[idx] <= k:
    total += p[idx]
    idx += 1
print(idx)
