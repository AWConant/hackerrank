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

for _ in range(gi()):
    n, k = gis()
    a = gis()
    a = [1 if aa <= 0 else 0 for aa in a]
    if sum(a) < k:
        print('YES')
    else:
        print('NO')
