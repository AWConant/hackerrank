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
is_even = lambda x: x%2 == 0
inf = float('inf')

# Python program to find articulation points in an undirected graph
#This code is contributed by Neelam Yadav
  
  
# Finding articulation points in graph (adjacency list)
#
# Credit: Adapted from code by Neelam Yadav
# http://www.geeksforgeeks.org/articulation-points-or-cut-vertices-in-a-graph/
def articulation_points(g, vertices): # O(V + E)
    time = 0
    def articulation_points_rec(u):
        nonlocal g, time, visited, ap, parent, low, disc

        children = 0
        visited[u] = True

        disc[u] = time
        low[u] = time
        time += 1

        for v in g[u]:
            if not visited[v]:
                parent[v] = u
                children += 1
                articulation_points_rec(v)

                low[u] = min(low[u], low[v])

                if parent[u] == -1 and children > 1:
                    ap[u] = True
                if parent[u] != -1 and low[v] >= disc[u]:
                    ap[u] = True   
            elif v != parent[u]: 
                low[u] = min(low[u], disc[v])

    visited = dict.fromkeys(vertices, False)
    disc = dict.fromkeys(vertices, float('inf'))
    low = dict.fromkeys(vertices, float('inf'))
    parent = dict.fromkeys(vertices, -1)
    ap = dict.fromkeys(vertices, False)

    for vertex in vertices:
        if not visited[vertex]:
            articulation_points_rec(vertex)

    return [k for k, v in ap.items() if v]
 
def connected_components(g, vs, bad): # O(V+E)
    def dfs_util_iter(start, visited):
        if start in bad:
            return [start]
        comp = []
        stack = [start]
        while stack:
            v = stack.pop()
            if v in visited:
                continue
            visited.add(v)
            comp.append(v)
            for u in g[v]:
                if u not in bad:
                    stack.append(u)
        return comp

    visited = set()
    comps = []
    for v in vs:
        if v not in visited:
            comp = dfs_util_iter(v, visited)
            comps.append(comp)
    return comps

def bfs(g, start, end, seen):
    q = deque([start])
    while q:
        cur = q.popleft()
        if cur in seen:
            continue
        if cur == end:
            return True
        seen.add(cur)
        q.extend(g[cur])

    return False

def main():
    n, m, q = gis()
    vertices = list(range(1, n+1))
    g = defaultdict(list)
    for _ in range(m):
        u, v = gis()
        g[u].append(v)
        g[v].append(u)

    aps = set(articulation_points(g, vertices))
    comps = connected_components(g, vertices, aps)

    vert2comp = dict()
    for i, comp in enumerate(comps):
        for v in comp:
            vert2comp[v] = i

    g_prime = defaultdict(set)
    for i, comp in enumerate(comps):
        for v in comp:
            for u in g[v]:
                neighbor_comp = vert2comp[u]
                if neighbor_comp != i:
                    g_prime[i].add(neighbor_comp)
                    g_prime[neighbor_comp].add(i)

    for _ in range(q):
        u, v, w = gis()

        u, v, w = vert2comp[u], vert2comp[v], vert2comp[w]

        seen = set()
        if bfs(g_prime, u, w, seen) and bfs(g_prime, v, w, seen):
            print('YES')
        else:
            print('NO')


main()
