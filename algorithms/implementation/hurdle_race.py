#!/usr/bin/python3

import sys

from itertools import *
from math import *
from collections import deque, defaultdict, OrderedDict
from queue import Queue
from heapq import heappush, heappop
from operator import itemgetter
from functools import reduce
from string import ascii_lowercase, ascii_uppercase

gi = lambda: int(input())
gis = lambda: list(map(int, input().split()))

n, k = gis()
h = gis()

print(max(0, max(h) - k))
