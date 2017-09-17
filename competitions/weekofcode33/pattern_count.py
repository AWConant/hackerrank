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

    idxs = [i for i, ch in enumerate(s) if ch == '1']

    ans = 0
    for i in range(len(idxs)-1):
        lo, hi = idxs[i], idxs[i+1]
        
        inner = s[lo+1:hi]
        if len(inner) > 0 and all(ch == '0' for ch in inner):
            ans += 1

    print(ans)
