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
w = sorted(gis())

ans = 0

i = 0
while i < n:
    ans += 1
    w_prime = w[i]
    while i+1 < n and w[i+1] <= w_prime+4:
        i += 1
    i += 1

print(ans)