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


# Find kth smallest element in a.
#
# Credit: KoderDojo
# http://www.koderdojo.com/blog/quickselect-algorithm-in-python
from random import randint
def quickselect(a, k): # O(n)ish
    def select(a, lo, hi, k):
        if hi == lo:
            return a[lo]

        pidx = randint(lo, hi)

        a[lo], a[pidx] = a[pidx], a[lo]

        i = lo
        for j in range(lo+1, hi+1):
            if a[j] < a[lo]:
                i += 1
                a[i], a[j] = a[j], a[i]

        a[i], a[lo] = a[lo], a[i]

        if k == i:
            return a[i]
        elif k < i:
            return select(a, lo, i-1, k)
        else:
            return select(a, i+1, hi, k)

    if a is None or len(a) < 1:
        return None

    if k < 0 or k > len(a) - 1:
        raise IndexError()

    return select(a, 0, len(a) - 1, k)

n = gi()
a = gis()
print(quickselect(a, n//2))
