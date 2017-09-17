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
inf = float('inf')

def substring_idxs(s):
    for i in range(len(s)):
        for j in range(i, len(s)):
            yield i, j

for _ in range(gi()):
    s = gs()

    counts = dict()
    for i in range(len(s)):
        counts[(0,i)] = Counter(s[:i+1])

    anagram_counts = Counter()
    for i,j in substring_idxs(s):
        if i == j:
            c = counts[(0,i)]
        else:
            c = counts[(0,j)] - counts[(0,i)]
        anagram_counts[frozenset(c.items())] += 1

    print(sum(count*(count-1)//2 for count in anagram_counts.values()))
