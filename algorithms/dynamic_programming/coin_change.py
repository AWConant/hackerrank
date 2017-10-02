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

n, m = gis()
denom = [0] + gis()
dp = [[0 for _ in range(n+1)] for _ in range(m+1)]

for i in range(1, m+1):
    dp[i][0] = 1

for i in range(1, m+1):
    for j in range(1, n+1):
        dp[i][j] = dp[i-1][j]
        if j >= denom[i]:
            dp[i][j] += dp[i][j-denom[i]]

print(dp[m][n])
