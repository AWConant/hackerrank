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

n = gi()
a = gis()
b = gis()

a = sorted([(v, i) for i, v in enumerate(a)])
b = sorted([(v, i) for i, v in enumerate(b)])

if a[0][1] != b[0][1]:
    print(a[0][0] + b[0][0])
else:
    print(min(a[1][0] + b[0][0], a[0][0] + b[1][0]))
