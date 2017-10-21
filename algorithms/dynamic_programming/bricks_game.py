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

inf = float('inf')

for _ in range(gi()):
    n = gi()
    b = list(reversed(gis()))

    pfsum = list(accumulate(b))

    dp = pfsum[:3]
    for i in range(3, n):
        dp.append(max(pfsum[i] - dp[i-1],
                      pfsum[i] - dp[i-2],
                      pfsum[i] - dp[i-3]))

    print(dp[n-1])