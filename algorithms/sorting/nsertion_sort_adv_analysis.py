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

# Fenwick tree
# Credit: Raju Varshney

def getsum(tree,i):
    s = 0
    while i > 0:
        s += tree[i]
        i -= i & (-i)

    return s
 
def updatebit(tree, n, i):
    while i <= n:
        tree[i] += 1
        i += i & (-i)
 
###########################

def main():
    for _ in range(gi()):
        n = gi()
        a = gis()

        inv = 0
        largest = max(a)
        tree = [0]*(largest+1)

        for a_i in reversed(a):
            inv += getsum(tree, a_i-1)
            updatebit(tree, largest, a_i)

        print(inv)

main()
