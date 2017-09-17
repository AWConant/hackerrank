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
    n = gi()
    a = gi()
    b = gi()

    poss = [set() for _ in range(n)]
    poss[0].add(0)
    for i in range(1, n):
        for prev in poss[i-1]:
            poss[i].add(prev+a)
            poss[i].add(prev+b)
    print(*sorted(list(poss[n-1])))
