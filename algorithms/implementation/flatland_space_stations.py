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
uptolast = lambda x: range(len(x)-1)
inf = float('inf')

n, m = gis()
s = sorted(gis())

if n ==1:
    print(0)
else:
    best = -inf
    for i in uptolast(s):
        best = max(best, (s[i+1]-s[i])//2)
    print(max(best, s[0], n-1-s[-1]))
