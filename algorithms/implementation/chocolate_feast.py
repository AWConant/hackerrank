#!/usr/bin/python3

# enumerate defaultdict

import sys

from itertools import *
from math import *
from collections import *
from queue import Queue
from heapq import heappush, heappop
from operator import *
from functools import reduce
from string import ascii_lowercase, ascii_uppercase

gi = lambda: int(input())
gis = lambda: list(map(int, input().split()))
gs = lambda: input()
rlen = lambda x: range(len(x))
inf = float('inf')

for _ in range(gi()):
    n, c, m = gis()

    ans = w = n//c
    while w >= m:
        ans += w//m
        w = (w//m + w%m)

    print(ans)
