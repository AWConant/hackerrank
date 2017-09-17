#!/usr/bin/python3

# enumerate defaultdict

import sys

from itertools import *
from math import *
from copy import copy, deepcopy
from collections import *
from queue import Queue
from heapq import heappush, heappop
from operator import *
from functools import reduce
from string import ascii_lowercase, ascii_uppercase

gi = lambda: int(input())
gis = lambda: list(map(int, input().split()))
gs = lambda: input()
skiplast = lambda x: range(len(x)-1)
inf = float('inf')

n = gi()
a = gis()
a.sort()

ans = []
best = inf
for i in skiplast(a):
    diff = abs(a[i] - a[i+1])
    if diff == best:
        ans.append(a[i])
        ans.append(a[i+1])
    elif diff < best:
        best = diff
        ans = [a[i], a[i+1]]

print(*ans)
