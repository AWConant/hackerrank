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

def partition(a):
    if len(a) < 2:
        return a
    elif len(a) == 2:
        if a[0] > a[1]:
            ret = [a[1],a[0]]
        else:
            ret = a
        print(*ret)
        return ret

    p = a[0]
    left = partition(list(filter(lambda x: x < p, a)))
    right = partition(list(filter(lambda x: x > p, a)))
    equal = list(filter(lambda x: x == p, a))
    ret = left + equal + right
    print(*ret)
    return ret


n = gi()
a = gis()

partition(a)
