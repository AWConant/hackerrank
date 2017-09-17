#!/usr/bin/python3


from random import *
import sys # stdout enumerate
from itertools import * # chain from_iterable product
from math import * # sqrt floor ceil gcd
from copy import copy, deepcopy
from collections import * # Counter defaultdict deque
from queue import Queue
from heapq import heappush, heappop, heapify
from operator import * # itemgetter
from functools import reduce
from string import ascii_lowercase, ascii_uppercase

gi = lambda: int(input())
gis = lambda: list(map(int, input().split()))
gs = lambda: input()
skiplast = lambda x: range(len(x)-1)
is_even = lambda x: x%2 == 0

inf = float('inf')

def naive(k, n, a):
    weights = dict()
    for lo in range(n):
        for hi in range(lo+1, n):
            if a[hi]-a[lo] > 0:
                weights[(lo, hi)] = a[hi]-a[lo]

    nodelist = list(weights.keys())

    g = defaultdict(set)
    for node1, node2 in product(nodelist, nodelist):
        if node1 == node2:
            continue

        x1, x2 = node1
        y1, y2 = node2

        if x1 <= y2 and y1 <= x2:
            g[node1].add(node2)
            g[node2].add(node1)

    def combo_distinct(combo, g):
        for i in range(len(combo)):
            for j in range(i+1, len(combo)):
                if combo[i] in g[combo[j]]:
                    return False
        return True

    best = 0
    for kk in range(k+1):
        for combo in combinations(nodelist, kk):
            if combo_distinct(combo, g):
                best = max(best, sum(weights[node] for node in combo))
    
    return best

def iterate_subranges(lo, hi):
    for i in range(lo, hi):
        for j in range(i+1, hi):
            yield i, j

def backtrack(n, a, k, first):
    if k == 0 or first >= n-1:
        return 0

    best = 0
    for buy, sell in iterate_subranges(first, n):
        profit = a[sell]-a[buy]
        if profit > 0:
            best = max(best, profit + backtrack(n, a, k-1, sell+1))

    return best

def fast(n, a, k):
    dp = [[0 for _ in range(n+1)] for _ in range(k+1)]

    for lo in range(1, k+1):
        for hi in range(1, n):
            best = -inf
            for m in range(hi):
                best = max(a[hi] - a[m] + dp[lo-1][m], best)

            dp[lo][hi] = max(dp[lo][hi-1], best)
    
    return dp[k][n-1]

def main():
    for _ in range(gi()):
        k = gi()
        n = gi()
        a = gis()

        #print(naive(k, n, a))
        #print(backtrack(n, a, k, 0))
        print(fast(n, a, k))

def strest():
    q = 100
    for _ in range(q):
        k = 9
        n = 30
        a = [randrange(0, 1001) for _ in range(n)]

        #print(backtrack(n, a, k, 0))
        print(fast(n, a, k))


#main()
strest()
