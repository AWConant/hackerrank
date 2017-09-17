#!/usr/bin/python3

import sys

from itertools import *
from math import *
from collections import deque, defaultdict, OrderedDict
from queue import Queue
from heapq import heappush, heappop
from operator import itemgetter
from functools import reduce
from string import ascii_lowercase, ascii_uppercase

gi = lambda: int(input())
gis = lambda: list(map(int, input().split()))

n = gi()
s = [x[0] for x in groupby(gis())]
m = gi()
a = gis()

for aa in a:
    while len(s) > 0 and aa >= s[-1]:
        s.pop()
    print(len(s) + 1)
