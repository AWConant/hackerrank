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

n, d = gis()
a = gis()

a_d = sorted(a[:d])

ans = 0
for i in range(d, n):
    if d%2 == 0:
        median = (a_d[d//2-1] + a_d[d//2])/2
    else:
        median = a_d[d//2]

    if a[i] >= 2*median:
        ans += 1

    if a_d[d-1] == a[i-d]:
        a_d.pop()
    else:
        lo, hi = 0, d
        while hi-lo > 1:
            med_idx = (lo+hi)//2
            if a_d[med_idx] <= a[i-d]:
                lo = med_idx
            else:
                hi = med_idx
        a_d.pop(med_idx-1)

    lo, hi = 0, len(a_d)
    while hi-lo > 1:
        med_idx = (lo+hi)//2
        if a_d[med_idx] <= a[i]:
            lo = med_idx
        else:
            hi = med_idx
    a_d.insert(med_idx, a[i])

print(ans)
