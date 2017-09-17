#!/usr/bin/python3

import sys
from itertools import * # product chain from_iterable
from copy import copy, deepcopy

gis = lambda: list(map(int, input().split()))
gs = lambda: input()
inf = float('inf')

def print_grid(g):
    for row in g:
        for ch in row:
            sys.stdout.write(str(ch))
        sys.stdout.write('\n')

def prep(s):
    return list(map(int, s.replace('B', '0').replace('G', '1')))

def get_area(p, g, n, m):
    i, j = p

    u = i-1
    d = i+1
    l = j-1
    r = j+1

    a = 1
    g[i][j] = 2

    reset = [p]

    while True:
        u_ok = u >= 0 and g[u][j] == 1 
        d_ok = d < n and g[d][j]  == 1 
        l_ok = l >= 0 and g[i][l] == 1 
        r_ok = r < m and g[i][r]  == 1 
        if not (u_ok and d_ok and l_ok and r_ok):
            break

        reset.append((u, j))
        reset.append((d, j))
        reset.append((i, l))
        reset.append((i, r))

        g[u][j] = g[d][j] = g[i][l] = g[i][r] = 2
        a += 4

        u -= 1
        d += 1
        l -= 1
        r += 1

    return a, reset

def main():
    n, m = gis()
    g = [prep(gs()) for _ in range(n)]
    orig = deepcopy(g)

    best = -inf

    for (i1, j1), (i2, j2) in product(product(range(n), range(m)), product(range(n), range(m))):
        if (i1, j1) == (i2, j2) or 0 in (g[i1][j1], g[i2][j2]):
            continue

        a1, res1 = get_area((i1, j1), g, n, m)
        a2, res2 = get_area((i2, j2), g, n, m)
        new_area = a1*a2
        if new_area > best:
            best = new_area

        for i, j in chain(res1, res2):
            g[i][j] = 1

    print(best)


main()
