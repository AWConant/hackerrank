#!/usr/bin/python3

import sys

from itertools import *
from math import *
from collections import *
from queue import Queue
from heapq import heappush, heappop
from operator import itemgetter
from functools import reduce
from string import ascii_lowercase, ascii_uppercase

gi = lambda: int(input())
gis = lambda: list(map(int, input().split()))

i, j, k = gis()

count = 0
for x in range(i, j+1):
    if abs(x - int(''.join(list(reversed(str(x))))))%k == 0:
        count += 1
print(count)
