#!/usr/bin/python3

# enumerate defaultdict

import sys

from random import randrange
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

# Connected components in _undirected_ graph
def connected_components(g, vs): # O(V+E)
    visited = set()
    comps = []
    for v in vs:
        if v not in visited:
            comps.append(dfs_util_iter(g, v, visited))
    return comps

def dfs_util_iter(g, start, visited):
    comp = []
    stack = [start]
    while stack:
        v = stack.pop()
        if v in visited:
            continue
        visited.add(v)
        comp.append(v)
        stack.extend(g[v])
    return comp

# Longest palindromic subsequence
#
# Returns length of longest palindromic subsequence in s.
# Credit: Tushar Roy
# adapted from https://github.com/mission-peace/interview/blob/master/src/com/interview/dynamic/LongestPalindromicSubsequence.java
def longest_palindromic_subsequence(s): # O(n^2)
    dp = [[1]*len(s) for _ in range(len(s))]

    for size in range(2, len(s)+1):
        for i in range(len(s)-size+1):

            j = i + size - 1
            if size == 2 and s[i] == s[j]:
                dp[i][j] = 2
            elif s[i] == s[j]:
                dp[i][j] = dp[i+1][j-1] + 2
            else:
                dp[i][j] = max(dp[i+1][j], dp[i][j-1])

    return dp[0][len(s)-1]

def main():
    n, k, m = gis()
    #n = randrange(1, 10**5 + 1)
    #k = randrange(1, 10**6 + 1)
    #m = randrange(1, 10**3 + 1)

    g = defaultdict(list)
    for _ in range(k):
        x, y = gis()
        #x = randrange(1, n+1)
        #y = randrange(1, n+1)

        g[x].append(y)
        g[y].append(x)

    s = gis()
    #s = [randrange(1, n+1) for _ in range(m)]

    
    comp = dict()
    for i, component in enumerate(connected_components(g, list(range(1, n+1)))):
        for v in component:
            comp[v] = i
    print(connected_components(g, list(range(1, n+1))))

    print(longest_palindromic_subsequence([comp[x] for x in s]))

main()
