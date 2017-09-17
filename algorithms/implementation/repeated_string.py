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

s = gs()
n = gi()

repeated = s.count('a')*(n//len(s))
final = s[:n%len(s)].count('a')
print(repeated + final)
