#!/usr/bin/python3

from itertools import * # chain from_iterable product
from math import * # sqrt floor ceil
from collections import * # Counter defaultdict deque
from queue import Queue
from string import ascii_lowercase, ascii_uppercase
import re

gi = lambda: int(input())
gis = lambda: list(map(int, input().split()))
gs = lambda: input()

inf = float('inf')

###############################################################

LEVEL = 18

def cache_log_values(n, MAXN):
    P2 = [1]
    for i in range(1, LEVEL):
        P2.append( P2[i-1]*2 )

    LOG2N = [None]
    val, idx = 1, 0
    for i in range(1, (MAXN*2)+1):
        if val != i:
            LOG2N.append(idx-1)
        else:
            val *= 2
            LOG2N.append(idx)
            idx += 1

    return P2, LOG2N

def build_sparse_table(depths, P2):
    n = len(depths)
    st = [[None for _ in range(LEVEL)] for _ in range(n+1)]

    for i in range(1, n):
        st[i-1][0] = i-1 if depths[i] > depths[i-1] else i

    for l in range(1, LEVEL):
        for i in range(n):
            if st[i][l-1] is not None and st[i+P2[l-1]][l-1] is not None:
                if depths[st[i][l-1]] > depths[st[i+P2[l-1]][l-1]]:
                    st[i][l] = st[i+P2[l-1]][l-1]
                else:
                    st[i][l] = st[i][l-1]
            else:
                break

    return st

def query(l, r, st, depths, P2, LOG2N):
    if l == r:
        return l

    dx = LOG2N[r-l]
    if depths[st[l][dx]] > depths[st[r-P2[dx]][dx]]:
        return st[r-P2[dx]][dx]
    else:
        return st[l][dx]

def get_lca(u, v, fai, euler, st, depths, P2, LOG2N):
    if u == v:
        return u

    if fai[u] > fai[v]:
        u, v = v, u

    return euler[query(fai[u], fai[v], st, depths, P2, LOG2N)];

def dfs_util(g, vertices, root, parent_of):
    euler = []
    level = dict()
    fai = dict.fromkeys(vertices, -1)

    ptr = 0
    seen = set()
    stack = [(root, 0)]
    while stack:
        cur, dep = stack.pop()

        seen.add(cur)

        if fai[cur] == -1:
            fai[cur] = ptr

        level[cur] = dep
        euler.append(cur)
        ptr += 1

        for x in g[cur]:
            if x != parent_of[cur] and x not in seen:
                stack.append( (x, dep+1) )
                break
        else:
            if cur == root:
                break
            stack.append( (parent_of[cur], dep-1) )

    return euler, level, fai

###############################################################

def get_parent_pointers(g, root):
    parent_of = {root: None}

    queue = deque([ (root, None) ])
    while queue:
        cur, prev = queue.popleft()
        for child in g[cur]:
            if child != prev:
                parent_of[child] = cur
                queue.append( (child, cur) )

    return parent_of

def iterate_path(u, v, lca, parent_of):
    u_to_lca = [u]
    while u_to_lca[-1] != lca:
        u_to_lca.append(parent_of[u_to_lca[-1]])
    u_to_lca.pop()

    v_to_lca = [v]
    while v_to_lca[-1] != lca:
        v_to_lca.append(parent_of[v_to_lca[-1]])

    return chain(u_to_lca, reversed(v_to_lca))

###############################################################

def main():
    MAXN = 10**5

    n, q = gis()
    s = gs()
    p = gs()

    vertices = list(range(1, n+1))
    g = defaultdict(list)
    root = 1

    # read edges and build graph
    for _ in range(n-1):
        u, v = gis()
        g[u].append(v)
        g[v].append(u)

    # Set up O(1) path LCA lookups
    P2, LOG2N = cache_log_values(n, MAXN)
    parent_of = get_parent_pointers(g, root)
    euler, level, fai = dfs_util(g, vertices, root, parent_of)
    depths = [level[x] for x in euler]
    st = build_sparse_table(depths, P2)
    
    for _ in range(q):
        u, v = gis()
        lca = get_lca(u, v, fai, euler, st, depths, P2, LOG2N)
        s_prime = ''.join(s[i-1] for i in iterate_path(u, v, lca, parent_of))
        print(sum(1 for _ in re.finditer('(?=%s)' % p, s_prime)))

main()
