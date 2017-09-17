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

for _ in range(gi()):
    w = list(map(ord, list(gs())))

    i = len(w)-1
    while i > 0 and w[i-1] >= w[i]:
        i -= 1
    if i <= 0:
        print('no answer')
        continue

    j = len(w)-1
    while w[j] <= w[i-1]:
        j -= 1

    nex = list(w)
    nex[i-1], nex[j] = nex[j], nex[i-1]

    nex = nex[:i] + list(reversed(nex[i:]))

    print(''.join(list(map(chr, nex))))
