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
a = [gs() for _ in range(n)]

buckets = defaultdict(list)

for a_i in a:
    buckets[len(a_i)].append(a_i)

for length in sorted(buckets):
    for value in sorted(buckets[length]):
        print(value)
