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

for _ in range(gi()):
    s = gs()

    ans = 0
    for left in range(len(s)//2):
        right = len(s)-left-1
        lo, hi = min(s[left], s[right]), max(s[left], s[right])
        ans += ord(hi) - ord(lo)
    print(ans)
