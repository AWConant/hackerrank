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
uptolast = lambda x: range(len(x)-1)
inf = float('inf')

def solve(n, b):
    for i, c in enumerate(b):
        adjs = filter(lambda x: 0 <= x < n, [i+1, i-1])
        if c != '_' and not any(b[adj] == c for adj in adjs):
            break
    else:
        return 'YES'


    if not any(ch == '_' for ch in b):
        return 'NO'

    for k, v in Counter(b).items():
        if k != '_' and v == 1:
            return 'NO'

    return 'YES'


for _ in range(gi()):
    n = gi()
    b = gs()
    print(solve(n, b))
