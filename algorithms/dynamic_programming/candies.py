#!/usr/bin/python3


import sys # stdout enumerate
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
rating = [gi() for _ in range(n)]

asc = [None]*n
asc[0] = 1
for i in range(1, n):
    if rating[i] > rating[i-1]:
        asc[i] = asc[i-1]+1
    else:
        asc[i] = 1

des = [None]*n
des[-1] = 1
for i in range(n-2, -1, -1):
    if rating[i] > rating[i+1]:
        des[i] = des[i+1]+1
    else:
        des[i] = 1

print(sum(max(a, d) for a, d in zip(asc, des)))
