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

n, d = gis()
a = set(gis())

ans = 0
for i in a:
    if i+d in a and i+d+d in a:
        ans += 1

print(ans)
