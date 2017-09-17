#!/usr/bin/python3


import sys # stdout enumerate
from itertools import * # chain from_iterable product
from math import * # sqrt floor ceil gcd
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

def naive(n, ps, k):
    prices = []
    for i, p in enumerate(ps, start=1):
        prices.extend([p]*i)
    prices.sort()

    ans = 0
    for price in prices:
        if k >= price:
            ans += 1
            k -= price
        else:
            break

    return ans

def clever(n, ps, k):
    prices = sorted([(p, ct) for ct, p in enumerate(ps, start=1)])

    ans = 0
    for p, ct in prices:
        if k >= p*ct:
            ans += ct
            k -= p*ct
        elif k >= p:
            for _ in range(ct):
                if k >= p:
                    ans += 1
                    k -= p
                else:
                    return ans

    return ans

n = gi()
ps = gis()
k = gi()

print(clever(n, ps, k))
