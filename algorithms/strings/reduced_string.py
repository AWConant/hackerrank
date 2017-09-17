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
skiplast = lambda x: range(len(x)-1)
inf = float('inf')

s = gs()
deletes = -1
while deletes != 0:
    old = s
    i = 0
    s = ''
    deletes = 0
    while i < len(old)-1:
        if old[i] == old[i+1]:
            i += 2
            deletes += 1
        else:
            s += old[i]
            i += 1

print(s if s != '' else 'Empty String')
