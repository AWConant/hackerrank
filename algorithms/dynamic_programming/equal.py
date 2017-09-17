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

def cutdown(c, k):
    ops = (c[i] - lowest)//k
    c[i] -= ops*k
    return ops

for _ in range(gi()):
    n = gi()
    c = gis()

    lowest = min(c)

    ans = 0
    for i in range(len(c)):
        while c[i]-5 >= lowest:
            c[i] -= 5
            ans += 1
        while c[i]-2 >= lowest:
            c[i] -= 2
            ans += 1
        while c[i]-1 >= lowest:
            c[i] -= 1
            ans += 1

    print(ans)
