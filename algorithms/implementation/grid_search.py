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
uptolast = lambda x: range(len(x)-1)
inf = float('inf')

for _ in range(gi()):
    R, C = gis()
    G = [list(input()) for _ in range(R)]

    r, c = gis()
    P = [list(input()) for _ in range(r)]

    done = False
    for i, j in product(range(R-r+1), range(C-c+1)):
        if G[i][j] == P[0][0]:
            for ii, jj in product(range(r), range(c)):
                if G[i+ii][j+jj] != P[ii][jj]:
                    break
            else:
                print('YES')
                break
    else:
        print('NO')

