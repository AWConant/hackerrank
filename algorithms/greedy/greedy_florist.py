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
c = sorted(gis(), reverse=True)

buylists = [list() for _ in range(k)]

ans = 0

for i, c_i in enumerate(c):
    buylists[i%k].append(c_i)

for buylist in buylists:
    for i, c_i in enumerate(buylist, start=1):
        ans += c_i*i

print(ans)
