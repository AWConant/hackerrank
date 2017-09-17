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


def solve(a, n):
    in_order = sorted(a)
    idx_of = dict((value, idx) for idx, value in enumerate(a))

    ans = 0
    for i, (actual, correct) in enumerate(zip(a, in_order)):
        if actual != correct:
            ans += 1

            a[idx_of[correct]] = actual
            idx_of[actual] = idx_of[correct]

    return ans


n = gi()
a = gis()
print(min(solve(list(a), n), solve(list(reversed(a)), n)))
