#!/usr/bin/env python3

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
gs = lambda: input()

n = gi()
s = gs()

letters = [[None]*26 for _ in range(26)]
counts = [[0]*26 for _ in range(26)]

for ch in s:
    idx = ord(ch) - ord('a')
    for i in range(26):
        if letters[idx][i] != ch and counts[idx][i] != -1:
            letters[idx][i] = ch
            counts[idx][i] += 1
        else:
            counts[idx][i] = -1
        if letters[i][idx] != ch and counts[i][idx] != -1:
            letters[i][idx] = ch
            counts[i][idx] += 1
        else:
            counts[i][idx] = -1

best = float('-inf')
for i in range(26):
    for j in range(26):
        best = max(best, counts[i][j])

print(best if best > 1 else 0)
