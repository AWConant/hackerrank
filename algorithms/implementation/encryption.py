#!/usr/bin/python3

# enumerate defaultdict

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

s = gs().replace(' ', '')
L = len(s)
row = round(sqrt(L))
col = row if row >= sqrt(L) else row + 1
for i in range(col):
    for j in range(i, L, col):
        sys.stdout.write(s[j])
    sys.stdout.write(' ')
sys.stdout.write('\n')
