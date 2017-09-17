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

n, k = gis()
a = gis()

m = [0] * k
for aa in a:
    m[aa%k] += 1

total = 0 if m[0] == 0 else 1

for i in range(1, k//2 + 1):
    if i == k-i:
        if m[i] > 0:
            total += 1
    else:
        total += max(m[i], m[k-i])

print(total)
