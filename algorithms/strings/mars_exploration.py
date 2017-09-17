#!/usr/bin/env python3

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
gs = lambda: input()

s = gs()

ans = 0
for i, ch in enumerate(s):
    if i%3 == 1:
        if ch != 'O':
            ans += 1
    else:
        if ch != 'S':
            ans += 1

print(ans)

