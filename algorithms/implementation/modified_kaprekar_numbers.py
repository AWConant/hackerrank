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

p = gi()
q = gi()

ans = []
for n in range(p, q+1):
    d = len(str(n))
    r = str(n**2)[-d:]
    l = str(n**2)[:-d]
    r = '0' if r == '' else r
    l = '0' if l == '' else l
    if int(r) + int(l) == n:
        ans.append(n)

if len(ans) > 0:
    print(*ans)
else:
    print('INVALID RANGE')
