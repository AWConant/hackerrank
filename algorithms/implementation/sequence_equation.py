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

n = gi()
pin = gis()
p = {x: i+1 for i, x in enumerate(pin)}
for i in range(1, n+1):
    print(p[p[i]])
