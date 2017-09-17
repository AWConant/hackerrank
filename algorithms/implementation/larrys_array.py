#!/usr/bin/python3

# enumerate defaultdict

import sys

from itertools import *
from math import *
from copy import copy, deepcopy
from collections import *
from queue import Queue
from heapq import heappush, heappop
from operator import *
from functools import reduce
from string import ascii_lowercase, ascii_uppercase

gi = lambda: int(input())
gis = lambda: list(map(int, input().split()))
gs = lambda: input()
skiplast = lambda x: range(len(x)-1)
inf = float('inf')

for _ in range(gi()):
    n = gi()
    a = gis()

    inv = 0
    for i in range(n):
        for j in range(i+1, n):
            if a[j] < a[i]:
                inv += 1

    print('YES' if inv%2==0 else 'NO')
