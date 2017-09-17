#!/bin/python3

from itertools import groupby

def rotate(xs, k):
    return xs[k:] + xs[:k] 

def brute(s):
    if len(s) == 1:
        return 0
    st = tuple(s)
    try: return dp[st]
    except KeyError: pass

    lo = min(s)
    idxs = [i for i, ch in enumerate(s) if ch == lo]
    ans = float('inf')

    for idx in idxs:
        rest = brute(rotate(s, idx)[1:])
        if idx != 0:
            rest += 1
        ans = min(ans, rest)

    dp[st] = ans
    return ans

## IDEA: start at solution; rotate back to input
#def clever(xs):
#    if len(set(xs)) == 1:
#        return 0
#
#    # remove consecutive dupes
#    # NOTE: How do I know whether to leave wrapped dupes at the
#    # head or tail???
#    xs = [x[0] for x in groupby(xs)]
#        #if i == n:
#        #    continue
#
#    n = len(xs)
#    nxts = {k: (k+1)%n for k in range(n)}
#    prvs = {k: (k-1)%n for k in range(n)}
#
#    ch2idxs = {ch: set() for ch in range(26)}
#    for i, ch in enumerate(xs): ch2idxs[ch].add(i)
#
#    in_order = sorted(xs)
#
#    ans = 0
#    head = 0
#    for correct in enumerate(in_order):
#        if xs[head] != correct:
#            ans += 1
#            max_diff = 0
#            cands = []
#            for idx in ch2idxs[correct]:
#                nxt = xs[nxts[idx]]
#                this = xs[idx]
#                diff = nxt - this if nxt - this != 0 else float('inf')
#                if diff > max_diff:
#                    head = idx
#                    max_diff = diff
#                    cands = []
#                elif diff == max_diff:
#                    cands.append(idx)
#
#            for idx in cands:
#                nxt = xs[nxts[idx]]
#                prv = xs[prvs[idx]]
#                if prv - nxt == 0:
#                    head = idx
#                    break
#
#        orig_prev = prvs[head]
#        while xs[head] == xs[nxts[head]]:
#            head = nxts[head]
#
#        prvs[nxts[head]] = prvs[head]
#        nxts[prvs[head]] = nxts[head]
#        ch2idxs[correct].remove(head)
#        head = nxts[head]
#
#    return ans

def clever(xs):
    if len(set(xs)) == 1:
        return 0

    # NOTE: How do I know whether to leave wrapped dupes at the
    # head or tail???
    xs = [x[0] for x in groupby(xs)]
    #if xs[0] == xs[-1]: del xs[-1]

    n = len(xs)
    nxts = {k: (k+1)%n for k in range(n)}
    prvs = {k: (k-1)%n for k in range(n)}

    ch2idxs = {ch: list() for ch in range(26)}
    for i, ch in enumerate(xs): ch2idxs[ch].append(i)

    grouped = groupby(sorted(xs))
    order = (x[0] for i, x in enumerate(grouped))

    ans = 0
    head = 0
    for correct in order:
        idxs = ch2idxs[correct]
        for i, idx in enumerate(idxs):
            if i == len(idxs)-1:
                continue
            if idx == idxs[i+1]:
                prvs[nxts[idx]] = prvs[idx]
                nxts[prvs[idx]] = nxts[idx]

            
        idxs.sort(key=lambda idx:
                      (xs[nxts[idx]] - xs[idx], xs[prvs[idx]]))
        #print(correct, xs, idxs, nxts)
        for idx in idxs:
            if head != idx:
                print('setting head %d to idx %d' % (head, idx))
                head = idx
                ans += 1
            else:
                pass
                print('at', idx)

            prvs[nxts[head]] = prvs[head]
            nxts[prvs[head]] = nxts[head]
            head = nxts[head]
       
    return ans

from random import choice

def caser():
    chs = list(range(3))
    for n in range(1, 10):
        for _ in range(10000):
            yield [choice(chs) for _ in range(n)]

#dp = dict()
#getcase = caser()
#while True:
#    case = next(getcase)
#    clev = clever(case)
#    brut = brute(case)
#    if clev != brut:
#        print(case, clev, brut)
#        input()


for case in range(int(input())):
    dp = dict()
    line = input()
    #print([x[0] for x in groupby(line)])
    print(line)
    s = [ord(ch) - 97 for ch in line]
    #s = [ch for ch in line]
    #print(brute( [x[0] for x in groupby(s)] ))
    print(clever(s))


##############################################

#cur = idx
#while True:
#    diff = xs[nxts[cur]] - xs[cur]
#    if diff != min_diff:
#        break
#    cur = nxts[cur]

#
#def booth(s):
#    xs = 2*s
#    f = [-1] * len(xs)
#    k = 0
#    for j in range(1,len(xs)):
#        xsj = xs[j]
#        i = f[j-k-1]
#        while i != -1 and xsj != xs[k+i+1]:
#            if xsj < xs[k+i+1]:
#                k = j-i-1
#            i = f[i]
#        if xsj != xs[k+i+1]:
#            if xsj < xs[k]:
#                k = j
#            f[j-k] = -1
#        else:
#            f[j-k] = i+1
#    return k
#
#def solve(s):
#    in_order = sorted(s)
#    ans = 0
#    for i in range(len(s)):
#        if s[i] == in_order[i]:
#            #print("%2d: already correct" % i)
#            continue
#        k = booth(s[i:])
#        s = s[:i] + rotate(s[i:], k)
#        #print('%2d:' % i, s, k)
#        ans += 1
#    return ans
#
#
#class LLNode(object):
#    def __init__(self, data):
#        self.data = data
#        self.nxt = None
#        self.prv = None
#
#    def __repr__(self):
#        return str(self.data)
#
#def clever(s):
#    n = len(s)
#    head = prv = LLNode(s[0])
#    for i in range(1, n):
#        this = LLNode(s[i])
#        prv.nxt = this
#        prv = this
#    this.nxt = head
#
#    ch2refs = {ch: set() for ch in range(26)}
#    cur = head
#    for _ in range(n):
#        ch2refs[cur.data].add(cur)
#        cur = cur.nxt
#    assert cur == head
#
#    #for s in ch2refs.values():
#    #    for val in s:
#    #        print(val, val.nxt)
#
#    in_order = sorted(s)
#
#    ans = 0
#    for i, ch in enumerate(in_order):
#        if i == n:
#            continue
#        nxt = in_order[i+1]
#        if cur.data == ch:
#            cur.prv.nxt = cur.nxt
#            cur.nxt.prv = cur.prv
#            ch2refs[cur.data].remove(cur)
#
#        refs = ch2refs[ch]
#
#    
#    return ans
#
