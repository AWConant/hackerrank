#!/usr/bin/python3

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

n = gi()
a = gis()

while n > 0:
    print(n)
    minn = min(a)
    a = list(filter(lambda x: x != 0, [aa - minn for aa in a]))
    n = len(a)
