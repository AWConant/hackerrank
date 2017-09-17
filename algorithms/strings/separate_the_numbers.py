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

def solve(s):
    for i in range(len(s)//2):
        init = cur = int(s[:i+1])
        cand = str(cur)
        while len(cand) < len(s):
            cur += 1
            cand += str(cur)
        if s == cand:
            return init

    return None



q = gi()
for _ in range(q):
    s = gs()
    ans = solve(s)
    if ans is None:
        print('NO')
    else:
        print('YES', ans)
