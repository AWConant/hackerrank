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

t = gi()

for _ in range(t):
    n = gi()
    h = 1
    for i in range(n):
        if i%2==0:
            h *= 2
        else:
            h += 1
    print(h)
