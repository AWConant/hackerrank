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

q = gi()
t = 'hackerrank'
for _ in range(q):
    s = gs()
    j = 0
    for i, ch in enumerate(s):
        if ch == t[j]:
            j += 1
            if j == len(t)-1:
                break
    else:
        print('NO')
        continue
    print('YES')
