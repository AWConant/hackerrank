#!/usr/bin/python3

# enumerate defaultdict

import sys

from itertools import *
from math import *
from collections import *
from queue import Queue
from heapq import heappush, heappop
from operator import *
from functools import reduce
from string import ascii_lowercase, ascii_uppercase
from copy import copy, deepcopy

gi = lambda: int(input())
gis = lambda: list(map(int, input().split()))
gs = lambda: input()
uptolast = lambda x: range(len(x)-1)
inf = float('inf')

n = gi()

m = [list(map(int, list(gs()))) for _ in range(n)]
ans = deepcopy(m)

for i in range(1, len(m)-1):
    for j in range(1, len(m[i])-1):
        if (m[i][j] > m[i][j+1] and m[i][j] > m[i][j-1] and m[i][j] > m[i+1][j] and m[i][j] > m[i-1][j]):
            ans[i][j] = 'X'

for row in ans:
    print(''.join(list(map(str, row))))
