#!/usr/bin/python3

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

dr, mr, yr = gis()
dd, md, yd = gis()

if yr < yd or (yr == yd and mr < md) or (yr == yd and mr == md and dr <= dd):
    print(0)
elif yr == yd and mr == md and dr > dd:
    print(15*(dr-dd))
elif yr == yd and mr > md:
    print(500*(mr-md))
else:
    print(10000)
