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


n = gi()
counts = [list() for _ in range(100)]

mid = n//2
for i in range(n):
    a, s = gs().split()
    counts[int(a)].append(s if i >= mid else '-')

ans = []
for i, ls in enumerate(counts):
    ans.extend(ls)

print(*ans)
