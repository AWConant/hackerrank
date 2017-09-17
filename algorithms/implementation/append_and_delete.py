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

s = input()
t = input()
k = gi()

i = 0
while i < len(s) and i < len(t) and s[i] == t[i]:
    i += 1

min_ops = len(s) + len(t) - 2*i
if k < min_ops:
    print('No')
elif k == min_ops:
    print('Yes')
else:
    if k >= min_ops + 2*i or (k - min_ops) % 2 == 0:
        print('Yes')
    else:
        print('No')
