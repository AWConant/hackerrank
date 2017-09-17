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

# Credit Dave Abrahams
# (https://stackoverflow.com/questions/212358/binary-search-bisection-in-python)
def binary_search(a, x, lo=0, hi=None): # O(logn)
    from bisect import bisect_left
    hi = hi if hi is not None else len(a)
    pos = bisect_left(a, x, lo, hi)
    return (pos if pos != hi and a[pos] == x else -1)

for _ in range(gi()):
    m = gi()
    n = gi()
    c = gis()

    cs = sorted(c)

    for i, c_i in enumerate(cs):
        j = binary_search(cs, m-c_i)
        if i != j and j != -1:
            break

    idx1 = c.index(cs[i])
    idx2 = c.index(cs[j], idx1+1)
    print(*sorted([idx1+1, idx2+1]))
