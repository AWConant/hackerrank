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
skiplast = lambda x: range(len(x)-1)
is_even = lambda x: x%2 == 0

inf = float('inf')

n = gi()
a = gis()
b = gis()

ca = Counter(a)
cb = Counter(b)

elements = set(a) | set(b)

ans = 0

for element in elements:
    ans += min(ca[element], cb[element])

if all(ca[element] == cb[element] for element in elements):
    print(ans-1)
else:
    print(ans+1)
