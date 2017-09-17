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

n = gi()
a = gis()

e = a[-1]

for i in range(n-2, -1, -1):
    if a[i] > e:
        a[i+1] = a[i]
        print(*a)
    else:
        a[i+1] = e
        print(*a)
        break
else:
    a[0] = e
    print(*a)
