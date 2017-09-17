from math import sqrt
from itertools import product
from collections import defaultdict, Counter

idx_combos = [
    [2, 3, 6, 31, 31, 31, 45, 46, 50, 52, 52, 54],
    [11, 12, 29, 31, 35, 37, 43, 44, 44, 53, 57, 67],
    [9, 15, 26, 31, 31, 33, 34, 34, 37, 41, 60, 63],
    [12, 15, 23, 45, 47, 48, 52, 54, 57, 65, 65, 65],
    [18, 21, 22, 26, 45, 46, 51, 53, 58, 65, 65, 65],
    [4, 8, 13, 25, 27, 28, 37, 43, 45, 49, 51, 65],
    [4, 28, 28, 33, 40, 40, 41, 45, 54, 54, 55, 66],
    [4, 6, 10, 19, 30, 33, 41, 43, 47, 59, 59, 59],
    [9, 10, 21, 21, 24, 25, 30, 38, 41, 44, 48, 62],
    [18, 18, 28, 30, 31, 40, 42, 44, 48, 49, 61, 66],
    [1, 4, 19, 26, 30, 32, 33, 43, 47, 59, 59, 59],
    [9, 16, 16, 31, 31, 33, 34, 34, 37, 56, 56, 63],
    [11, 12, 29, 31, 35, 37, 43, 44, 44, 57, 60, 64],
    [3, 14, 21, 21, 36, 36, 37, 37, 44, 54, 62, 66],
    [2, 3, 6, 7, 8, 20, 25, 26, 34, 39, 43, 62],
    [0, 3, 4, 8, 10, 17, 20, 25, 34, 43, 56, 62],
    [3, 4, 11, 21, 22, 34, 34, 34, 35, 42, 47, 54],
    [5, 13, 16, 22, 30, 31, 31, 31, 45, 46, 52, 54],
]

dists = set()
point2dist = dict()
dist2points = defaultdict(set)
for r, c in product(range(-12, 13), range(-12, 13)):
    d = sqrt(r**2 + c**2)
    if not d.is_integer():
        point2dist[(r,c)] = d
        dist2points[d].add((r,c))
        dists.add(d)
dists = sorted(list(dists))

dist_combos = [[dists[idx] for idx in combo] for combo in idx_combos]

ri, ci = map(int, input().split())
pi = (ri, ci)
di = sqrt(ri**2 + ci**2)

for combo in dist_combos:
    if di in combo:
        points = []
        for d, count in Counter(combo).items():
            cop = set(dist2points[d])
            if pi in cop:
                cop.remove(pi)
                count -= 1
                points.append(pi)
            for i in range(count):
                points.append(cop.pop())

        if pi in points:
            for point in points:
                if pi != point:
                    print(*point)
            break
else:
    assert False
