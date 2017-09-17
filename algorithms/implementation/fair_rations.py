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

gi = lambda: int(input())
gis = lambda: list(map(int, input().split()))
gs = lambda: input()
uptolast = lambda x: range(len(x)-1)
inf = float('inf')

n = gi()
b = gis()

ans = 0
for i in uptolast(b):
    if b[i]%2!=0:
        b[i+1] += 1
        ans += 2

if b[-1]%2==0:
    print(ans)
else:
    print('NO')
