#!/usr/bin/python3

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

n, m = gis()
ps = [int(gs(), base=2) for _ in range(n)]

best = -1
count = -1

for i, j in product(range(n), range(n)):
    if i == j:
        continue

    un = bin(ps[i]|ps[j]).count('1')
    if un == best:
        count += 1
    elif un > best:
        best = un
        count = 1

print(best)
print(count//2)
