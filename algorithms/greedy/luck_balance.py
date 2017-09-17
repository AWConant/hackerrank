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

n, k = gis()

imp, unimp = [], []
for _ in range(n):
    l, t = gis()
    if t == 1:
        imp.append(l)
    else:
        unimp.append(l)

imp.sort(reverse=True)
lose_imp, win_imp = imp[:k], imp[k:]

print(sum(lose_imp) - sum(win_imp) + sum(unimp))
