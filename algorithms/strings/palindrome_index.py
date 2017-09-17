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
    s= gs()

    for i in range(len(s)//2):
        j = len(s)-i-1
        if s[i] != s[j]:
            break
    else:
        print(-1)
        continue

    without_i = s[:i] + s[i+1:]
    if without_i == ''.join(list(reversed(without_i))):
        print(i)
    else:
        print(j)
