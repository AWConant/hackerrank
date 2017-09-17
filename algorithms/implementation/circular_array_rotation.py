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

n, k, q = gis()
a = gis() * 2
rotated = a[n-k:n-k+n]
for qq in range(q):
    m = gi()
    #print(m, len(rotated), rotated)
    print(rotated[m])
    
