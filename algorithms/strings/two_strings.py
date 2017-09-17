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

def solve():
    pass

for _ in range(gi()):
    a = gs()
    b = gs()

    print('YES' if len(set(a) & set(b)) > 0 else 'NO')
