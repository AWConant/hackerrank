#!/bin/python3

from queue import Queue
from itertools import chain

def bfs(start, g, visited):
    count = 0
    q = Queue()
    q.put( (None, start) )
    while not q.empty():
        prev, node = q.get()
        if visited[node]: continue
        visited[node] = True
        count += 1
        if prev != None:
            g[prev].remove(node)
            g[node].remove(prev)
        for w in g[node]:
            q.put( (node, w) )
    return count

def main():
    n, m = map(int, input().split())
    nodes = range(1, n+1)
    g = {node: set() for node in nodes}
    for _ in range(m):
        u, v = map(int, input().split())
        g[u].add(v)
        g[v].add(u)

    friends = []
    visited = {node: False for node in nodes}
    for node in nodes:
        if visited[node]: continue
        count = bfs(node, g, visited) - 1
        if count > 0:
            friends.append(count)

    friends.sort(reverse=True)

    total = 0
    all_components = 0
    for count in friends:
        this = count*(count+1)*(count+2)//3
        others = all_components*count
        total += this + others
        all_components += count*(count+1)

    total += all_components*len(list(chain.from_iterable(g.values())))//2

    print(total)

for case in range(int(input())):
    main()
