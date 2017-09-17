#!/usr/bin/python3

import sys # stdout
# enumerate
from itertools import * # chain from_iterable product
from math import * # sqrt floor ceil
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

def mat_mul(l, g):
    z = zip(*g)
    return [sum(mul(k,t) for k,t in i) for i in [zip(l,i) for i in z]]
 
def neighbors(r, c, n, m):
    if r-1>=0:
        yield r-1, c
    if c-1>=0:
        yield r,c-1
    if r+1<n:
        yield r+1, c
    if c+1<m:
        yield r, c+1
 
def main():
    OBS = '#'
    ALEF = 'A'
    MINE = '*'
    EXIT = '%'
    FREE = 'O'

    #l,g=[1,0,0,1,0,0], [[0,1],[1,1],[1,0],[1,0],[1,1],[0,1]]
    #print(mat_mul(l, g))

    n, m, k = gis()
    grid = [list(gs()) for _ in range(n)]
    tunnels = dict()
    for _ in range(k):
        i1, j1, i2, j2 = gis()
        i1 -= 1
        i2 -= 1
        j1 -= 1
        j2 -= 1
        tunnels[ (i1, j1) ] = (i2, j2)
        tunnels[ (i2, j2) ] = (i1, j1)

    g = defaultdict(list)
    exits = []
    for i, row in enumerate(grid):
        for j, v in enumerate(row):
            idx = (m*i)+j
            if v == OBS or v == MINE or v == EXIT:
                if v == EXIT:
                    exits.append(idx)
                continue

            if v == ALEF:
                alef = idx

            for i_n, j_n in neighbors(i, j, n, m):
                v_n = grid[i_n][j_n]
                if v_n == OBS:
                    continue


                if (i_n, j_n) in tunnels:
                    i_t, j_t = tunnels[ (i_n, j_n) ]
                    idx_t = (m*i_t)+j_t
                    g[idx].append(idx_t)
                else:
                    idx_n = (m*i_n)+j_n
                    g[idx].append(idx_n)

    #for k, v in g.items():
    #    print(k, v)

    mat = [[0 for _ in range(n*m)] for _ in range(m*n)]
    for u, vs in g.items():
        prob = 1/len(vs)
        for v in vs:
            mat[u][v] = prob

    x = [0 for _ in range(m*n)]
    x[alef] = 1

    print(x)
    #for row in mat:
    #    print(row)

    x = mat_mul(x, mat)
    prob = sum(x[exit] for exit in exits)
    new = None
    while new != 0:
        #print(prob)
        x = mat_mul(x, mat)
        new = sum(x[exit] for exit in exits)
        if new != 0:
            prob = new

    print(prob)
        
    
main()
