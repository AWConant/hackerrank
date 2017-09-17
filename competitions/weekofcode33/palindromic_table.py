#!/usr/bin/python3

# enumerate defaultdict

import sys

from itertools import *
from math import *
from copy import copy, deepcopy
from collections import *
from queue import Queue
from heapq import heappush, heappop, heapify
from operator import *
from functools import reduce
from string import ascii_lowercase, ascii_uppercase

gi = lambda: int(input())
gis = lambda: list(map(int, input().split()))
gs = lambda: input()
skiplast = lambda x: range(len(x)-1)
inf = float('inf')
is_even = lambda x: x%2==0

n, m = gis()
grid = [gis() for _ in range(n)]

def pal_subrec(counts, a):
    if is_even(a):
        if all(is_even(count) for count in counts):
            return True
    else:
        allow_odd = True
        for count in counts:
            if not is_even(count):
                if not allow_odd:
                    return False
                else:
                    allow_odd = False
        return True

def brute_optimized(n, m, grid):
    best = 1
    top = left = bot = right = 0
    for (i_lo, j_lo), (i_hi, j_hi) in large_to_small(0, 0, n-1, m-1):
        a = (i_hi-i_lo+1)*(j_hi-j_lo+1)

        counts = [0]*10
        for i in range(i_lo, i_hi+1):
            for j in range(j_lo, j_hi+1):
                counts[grid[i][j]] += 1

        if counts[0] == a:
            continue

        if pal_subrec(counts, a) and a > best:
            return a, i_lo, j_lo, i_hi, j_hi
            
    return best, top, left, bot, right


def large_to_small(i1, j1, i2, j2):
    q = deque([ ((i1, j1), (i2, j2)) ])

    n = 1
    pq = [ (-1*(i2-i1+1)*(j2-j1+1), ((i1, j1), (i2, j2))) ]

    while q:
        (i1, j1), (i2, j2) = q.pop()

        if len(pq) == n:
            while pq:
                a, ret = heappop(pq)
                yield ret
            n *= 4

        if j1+1 <= j2:
            a = (j2-j1)*(i2-i1+1)
            new = ((i1, j1+1), (i2, j2)) 
            heappush(pq, (-a, new))
            q.appendleft(new)
        if j2-1 >= j1:
            a = (j2-j1)*(i2-i1+1)
            new = ((i1, j1), (i2, j2-1)) 
            heappush(pq, (-a, new))
            q.appendleft(new)
        if i1+1 <= i2:
            a = (j2-j1+1)*(i2-i1)
            new = ((i1+1, j1), (i2, j2)) 
            heappush(pq, (-a, new))
            q.appendleft(new)
        if i2-1 >= i1: 
            a = (j2-j1+1)*(i2-i1)
            new = ((i1, j1), (i2-1, j2)) 
            heappush(pq, (-a, new))
            q.appendleft(new)

b, *rest = brute_optimized(n, m, grid)
print(b)
print(*rest)

##################################################

#def rec_helper(i1, j1, i2, j2, grid):
#
#    print((i1, j1), (i2, j2))
#
#
#    if i1 == i2 and j1 == j2:
#        return 1
#
#    counts = [0]*10
#    for i in range(i1, i2+1):
#        for j in range(j1, j2+1):
#            print(i,j)
#            counts[grid[i][j]] += 1
#
#    a = (i2-i1+1)*(j2-j1+1)
#    if counts[0] != a and pal_subrec(counts, a):
#        return a
#
#    adj = []
#    if i1+1 < i2:
#        adj.append(rec_helper(i1+1, i2, j1, j2, grid))
#    if i2-1 >= i1: 
#        adj.append(rec_helper(i1, i2-1, j1, j2, grid))
#    if j1+1 < j2:
#        adj.append(rec_helper(i1, i2, j1+1, j2, grid))
#    if j2-1 >= j1:
#        adj.append(rec_helper(i1, i2, j1, j2-1, grid))
#
#    return max(adj)
#
#
#def rec(n, m, grid):
#    return rec_helper(0, 0, n-1, m-1, grid)
#

#def brute(n, m, grid):
#    best = 1
#    top = left = bot = right = 0
#    for i_lo, j_lo in product(range(n), range(m)):
#        for i_hi, j_hi in reversed(list(product(range(n), range(m)))):
#            if i_hi < i_lo or j_hi < j_lo:
#                continue
#
#            a = (i_hi-i_lo+1)*(j_hi-j_lo+1)
#
#            counts = [0]*10
#            for i in range(i_lo, i_hi+1):
#                for j in range(j_lo, j_hi+1):
#                    counts[grid[i][j]] += 1
#            if counts[0] == a:
#                continue
#
#            if pal_subrec(counts, a) and a > best:
#                best = a
#                top = i_lo
#                bot = i_hi
#                left = j_lo
#                right = j_hi
#
#    return best, top, left, bot, right
