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

for _ in range(gi()):
    n = gi()
    count = 0
    for d in str(n):
        try:
            if n % int(d) == 0:
                count += 1
        except:
            pass
    print(count)
