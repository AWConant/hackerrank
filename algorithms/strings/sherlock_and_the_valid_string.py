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
    c = Counter(s)
    u = Counter(c.values())
    if len(u.keys()) == 1:
        return 'YES'
    elif len(u.keys()) > 2:
        return 'NO'
    else:
        if max(u.keys()) == min(u.keys())+1 and u[max(u.keys())] == 1:
            return 'YES'
        elif min(u.values()) == 1:
            return 'YES'
        else:
            return 'NO'

s = gs()
print(solve(s))
