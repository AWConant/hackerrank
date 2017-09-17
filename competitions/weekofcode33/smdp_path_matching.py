#!/usr/bin/python3

import sys # stdout
from itertools import * # chain from_iterable product
from math import * # sqrt floor ceil
from collections import * # Counter defaultdict deque
from queue import Queue
from string import ascii_lowercase, ascii_uppercase

gi = lambda: int(input())
gis = lambda: list(map(int, input().split()))
gs = lambda: input()

###########################################


# KMP substring algorithm
#
# Derived from m00nlight's code here:
# https://gist.github.com/m00nlight/daa6786cc503fde12a77
def get_table(pattern):
    table = [0]
    
    for i in range(1, len(pattern)):
        j = table[i-1]
        while j > 0 and pattern[j] != pattern[i]:
            j = table[j-1]
        table.append(j+1 if pattern[j] == pattern[i] else j)
    return table
        
def search(s, p):
    partial, count, j = get_table(p), 0, 0
    
    for i in range(len(s)):
        while j > 0 and s[i] != p[j]:
            j = partial[j-1]
        if s[i] == p[j]:
            j += 1
        if j == len(p): 
            count += 1
            j = 0
        
    return count


############################################

def naive(g, s, p, u, v):
    def bfs(graph, start, end):
        seen = set()
        parent = dict()
        queue = deque([start])
        while queue:
            node = queue.popleft()
            seen.add(node)

            if node == end:
                path = [end]
                while path[-1] != start:
                    path.append(parent[path[-1]])
                path.reverse()
                return path

            for adjacent in graph[node]:
                if adjacent not in seen:
                    parent[adjacent] = node
                    queue.append(adjacent)

    path = bfs(g, u, v)
    s_prime = ''.join(s[i-1] for i in path)
    return s_prime, s_prime.count(p), path

######################################

# This section derived from Nitish Kumar's code at
# http://www.geeksforgeeks.org/lca-n-ary-tree-constant-query-o1/

LEVEL = 19
MAXN = 10**5

def smdp_dfs(g, n): ###
    sm_parent = [[-1 for _ in range(LEVEL)] for _ in range(MAXN+1)]
    depth = [None for _ in range(MAXN+1)]
    depth[0] = 0

    stack = [(1, 0)]
    while stack:
        cur, prev = stack.pop()
        depth[cur] = depth[prev]+1
        sm_parent[cur][0] = prev
        for child in g[cur]:
            if child != prev:
                stack.append( (child, cur) )

    return depth, sm_parent

 
def precompute_sparse_matrix(n, sm_parent):
    for node in range(1, n+1):
        for i in range(1, LEVEL):
            if sm_parent[node][i-1] != -1:
                sm_parent[node][i] = sm_parent[sm_parent[node][i-1]][i-1]
 
def get_lca(u, v, depth, sm_parent):
    if depth[v] < depth[u]:
        u, v = v, u

    diff = depth[v] - depth[u]

    for i in range(LEVEL):
        if (diff>>i)&1:
            v = sm_parent[v][i]

    if u == v:
        return u

    for i in reversed(range(LEVEL-1)):
        if sm_parent[u][i] != sm_parent[v][i]:
            u = sm_parent[u][i]
            v = sm_parent[v][i]

    return sm_parent[u][0]

######################################

def iterate_path(u, v, lca, parent):
    u_to_lca = [u]
    while u_to_lca[-1] != lca:
        u_to_lca.append(parent[u_to_lca[-1]][0])
    u_to_lca.pop()

    v_to_lca = [v]
    while v_to_lca[-1] != lca:
        v_to_lca.append(parent[v_to_lca[-1]][0])

    return chain(u_to_lca, reversed(v_to_lca))
 
def get_parent_pointers(g):
    parent_of = dict() 

    queue = deque([ (1, None) ])
    while queue:
        cur, prev = queue.popleft()
        for child in g[cur]:
            if child != prev:
                parent_of[child] = cur
                queue.append( (child, cur) )

    return parent_of

def main():
    n, q = gis()
    s = gs()
    p = gs()

    vertices = list(range(1, n+1))
    g = defaultdict(list)

    for _ in range(n-1):
        u, v = gis()
        g[u].append(v)
        g[v].append(u)

    #parent = get_parent_pointers(g)
    depth, sm_parent = smdp_dfs(g, n)
    precompute_sparse_matrix(n, sm_parent)

    for _ in range(q):
        u, v = gis()
        lca = get_lca(u, v, depth, sm_parent)
        s_prime = ''.join(s[i-1] for i in iterate_path(u, v, lca, sm_parent))

        print(search(s_prime, p))

def test():
    from random import randrange, choice, shuffle

    mini_alpha = 'ab'
    alpha = ascii_lowercase

    get = lambda m: randrange(1, m+1)

    n = 50000
    q = 30000

    s = ''.join(choice(alpha) for _ in range(n))
    p = choice(s)

    vertices = list(range(1, n+1))
    g = defaultdict(list)
    root = 1

    # read edges and build graph
    grow_root = choice(vertices)
    roots = [grow_root]
    endpoints = list(vertices)
    endpoints.remove(grow_root)
    shuffle(endpoints)
    for _ in range(n-1):
        u, v = choice(roots), endpoints.pop()
        roots.append(v)
        g[u].append(v)
        g[v].append(u)

    parent = get_parent_pointers(g)
    depth, sm_parent = smdp_dfs(g, n)
    precompute_sparse_matrix(n, sm_parent)

    bad = 0
    for kase in range(q):
        u, v = randrange(1, n+1), randrange(1, n+1)
        lca = get_lca(u, v, depth, sm_parent)

        s_prime = ''.join(s[i-1] for i in iterate_path(u, v, lca, sm_parent))

        naive_s_prime, naive_ans, naive_path = naive(g, s, p, u, v)

        if s_prime != naive_s_prime:
            print(u, v, lca, s_prime, naive_s_prime)
            bad += 1

    print('mismatches:', bad)



#test()
main()

