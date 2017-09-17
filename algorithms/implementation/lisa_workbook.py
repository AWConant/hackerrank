#!/usr/bin/python3

# enumerate defaultdict

import sys

from itertools import *
from math import *
from collections import *
from queue import Queue
from heapq import heappush, heappop
from operator import *
from functools import reduce
from string import ascii_lowercase, ascii_uppercase

gi = lambda: int(input())
gis = lambda: list(map(int, input().split()))
gs = lambda: input()
rlen = lambda x: range(len(x))
inf = float('inf')

n, k = gis()
t = gis()

ans = 0
page_num = 1
for prob_count in t:
    page_count = ceil(prob_count/k)

    page_range = range(page_num, page_num + page_count)
    prob_range = range(1, prob_count+1)

    for i, page in enumerate(page_range):
        probs = prob_range[i*k:(i+1)*k]
        #print(page, probs, end=' ')
        if page in probs:
            ans += 1

    page_num += page_count

print(ans)
