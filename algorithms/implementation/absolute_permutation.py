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

for _ in range(gi()):
    n, k = gis()

    ans = []
    pool = set(range(1, n+1))
    for i in range(1, n+1):
        try:
            v = min(x for x in (i-k, i+k) if x in pool)
        except:
            break
        pool.remove(v)
        ans.append(v)
    else:
        print(*ans)
        continue
    print(-1)

