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

n, k = gis()
xs = sorted(gis())

ans = 0
lo, hi = 0, 1
while hi < n:
    diff = xs[hi]-xs[lo]
    if diff == k:
        ans += 1
        hi += 1
    elif diff > k:
        lo += 1
    else:
        hi += 1

print(ans)
