from collections import defaultdict, deque

n, s, t = map(int, input().split())
r_0, g, seed, p = map(int, input().split())

r = [r_0]
for i in range(1, n):
    r.append((r[i-1]*g + seed) % p)
#print(r)
print('r')

g = defaultdict(set)
for i, r_i in enumerate(r):
    g[i].add(i)
    for j in range(i+1, i+r_i+1):
        g[i].add(j%n)
    for j in range(i-1, i-r_i-1, -1):
        g[i].add(j%n)
#print(g)
print('g')
    
dist = -1
visited = set()
q = deque([(s, 0)])
while q:
    u, d = q.pop()
    if u in visited:
        continue
    visited.add(u)
    
    if u == t:
        dist = d
        break
    for v in g[u]:
        q.appendleft( (v, d+1) )
        
print(dist)
