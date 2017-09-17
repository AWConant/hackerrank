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

n = gi()
c = gis()

i = total = 0
while i < n-1:
    if i == n-2 or c[i+2]:
        i += 1
    else:
        i += 2
    total += 1

print(total)
