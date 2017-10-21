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
    n, k = gis()
    a = gis()

    dp = [[0 for _ in range(n)] for _ in range(k+1)]

    for j in range(n):
        dp[0][j] = 0

    for w in range(1, k+1):
        for j in range(n):
            if j == 0:
                if w >= a[j]:
                    dp[w][j] = dp[w - a[j]][j] + a[j]
            else:
                if w >= a[j]:
                    dp[w][j] = max(dp[w][j-1], dp[w - a[j]][j] + a[j])
                else:
                    dp[w][j] = dp[w][j-1]
    
    print(dp[k][n-1])