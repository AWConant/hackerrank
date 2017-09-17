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

for _ in range(gi()):
    n, k = gis()
    a = sorted(gis())
    b = sorted(gis(), reverse=True)

    for a_i, b_i in zip(a, b):
        if a_i + b_i < k:
            print('NO')
            break
    else:
        print('YES')
