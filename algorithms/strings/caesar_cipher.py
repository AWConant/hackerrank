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

n = gi()
s = gs()
k = gi()

ans = []
for ch in s:
    if ch.isalpha():
        if ch.isupper():
            new = ascii_uppercase[(((ord(ch)-65)+k)%26)]
        else:
            new = ascii_lowercase[(((ord(ch)-97)+k)%26)]
    else:
        new = ch
    ans.append(new)
print(''.join(ans))
