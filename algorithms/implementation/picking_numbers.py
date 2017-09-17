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
gis = lambda: map(int, input().split())

n = gi()
a = gis()

c = [0]*100

for aa in a:
    c[aa] += 1

best = -1
for i, cc in enumerate(c[:-1]):
    best = max(best, cc + c[i+1])

print(best)
