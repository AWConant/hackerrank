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
    if len(s)%2 != 0:
        return -1
    s1, s2 = s[:len(s)//2], s[len(s)//2:]
    c1, c2 = Counter(s1), Counter(s2)
    return sum((c1 - c2).values())

for _ in range(gi()):
    s = gs()
    print(solve(s))
