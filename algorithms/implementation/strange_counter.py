#!/usr/bin/python3

# enumerate defaultdict

import sys

from itertools import *
from math import *
from copy import copy, deepcopy
from collections import *
from queue import Queue
from heapq import heappush, heappop
from operator import *
from functools import reduce
from string import ascii_lowercase, ascii_uppercase

gi = lambda: int(input())
gis = lambda: list(map(int, input().split()))
gs = lambda: input()
uptolast = lambda x: range(len(x)-1)
inf = float('inf')

t = gi()
V = 3
while T > V:
    t -= V
    V *= 2
print(V-t+1)
