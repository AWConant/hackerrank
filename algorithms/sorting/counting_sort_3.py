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
skiplast = lambda x: range(len(x)-1)
inf = float('inf')

counts = [0]*100

n = gi()
for _ in range(n):
    a, _ = gs().split()
    counts[int(a)] += 1

ans = []
total = 0
for i in range(100):
    total += counts[i]
    ans.append(total)

print(*ans)
