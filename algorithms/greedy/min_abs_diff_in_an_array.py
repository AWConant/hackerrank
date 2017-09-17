#!/usr/bin/python3


import sys # stdout
# enumerate
from itertools import * # chain from_iterable product
from math import * # sqrt floor ceil
from copy import copy, deepcopy
from collections import * # Counter defaultdict deque
from queue import Queue
from heapq import heappush, heappop, heapify
from operator import * # itemgetter
from functools import reduce
from string import ascii_lowercase, ascii_uppercase

gi = lambda: int(input())
gis = lambda: list(map(int, input().split()))
gs = lambda: input()
skiplast = lambda x: range(len(x)-1)
is_even = lambda x: x%2 == 0

inf = float('inf')

n = gi()
#a = sorted([a_i if a_i >= 0 else -a_i for a_i in gis()])
a = sorted(gis())

best = inf
for i in skiplast(a):
    best = min(best, abs(a[i]-a[i+1]))

print(best)
