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
d = gis()

in_order = sorted(d)

if d == in_order:
    print('yes')
else:
    diff = [i+1 for i in range(n) if d[i] != in_order[i]]
    if len(diff) == 2:
        print('yes\nswap', end=' ')
        print(*diff)
    else:
        lo, hi = 0, n-1
        while d[lo] == in_order[lo]:
            lo += 1
        while d[hi] == in_order[hi]:
            hi -= 1
        if list(reversed(d[lo:hi+1])) == in_order[lo:hi+1]:
            print('yes\nreverse', end=' ')
            print(lo+1, hi+1)
        else:
            print('no')
