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
ls = sorted(gis(), reverse=True)

for i in range(n-2):
    s1, s2, s3 = ls[i], ls[i+1], ls[i+2]
    if s1 + s2 > s3 and s1 + s3 > s2 and s2 + s3 > s1:
        print(ls[i+2], ls[i+1], ls[i])
        break
else:
    print(-1)
