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

m, n, R = gis()
mat = [gis() for _ in range(m)]

layers = []

seen = set()
for x in range(min(m, n)):
    if (x, x) in seen:
        break

    layer = []
    
    # top side except rightmost
    for c in range(x, n-x-1):
        layer.append(mat[x][c])
        seen.add( (x, c) )

    # right side except lowest
    for r in range(x, m-x-1):
        layer.append(mat[r][n-x-1])
        seen.add( (r, n-x-1) )

    # bottom side except leftmost
    for c in range(n-x-1, x, -1):
        layer.append(mat[m-x-1][c])
        seen.add( (m-x-1, c) )

    # left side except topmost
    for r in range(m-x-1, x, -1):
        layer.append(mat[r][x])
        seen.add( (r, x) )

    layers.append(layer)

rots = []
for layer in layers:
    doubled = layer*2
    k = R%len(layer)
    rots.append(doubled[k:k+len(layer)])

for x, rot in enumerate(rots):
    idx = 0

    # top side except rightmost
    for c in range(x, n-x-1):
        mat[x][c] = rot[idx]
        idx += 1

    # right side except lowest
    for r in range(x, m-x-1):
        mat[r][n-x-1] = rot[idx]
        idx += 1

    # bottom side except leftmost
    for c in range(n-x-1, x, -1):
        mat[m-x-1][c] = rot[idx]
        idx += 1

    # left side except topmost
    for r in range(m-x-1, x, -1):
        mat[r][x] = rot[idx]
        idx += 1

for row in mat:
    for i, v in enumerate(row):
        if i < len(row)-1:
            sys.stdout.write(str(v) + ' ')
        else:
            sys.stdout.write(str(v))
    sys.stdout.write('\n')

