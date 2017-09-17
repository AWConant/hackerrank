#!/bin/python3

def white(b, n, k, sumb, dp):
    try: return dp[(b, k)]
    except KeyError: pass

    if sumb == n:
        ev = float(k)
    elif sumb == 0:
        ev = 0.0
    elif k == 1:
        summ = 0
        lo = 0; hi = n - 1
        while lo <= hi:
            v = max(b[lo], b[hi])
            if lo != hi: v *= 2
            summ += v
            lo += 1; hi -= 1
        ev = summ/n
    else:
        ev = 0
        lo = 0; hi = n - 1
        while lo <= hi:
            lo_ev = white(b[:lo] + b[lo+1:], n-1, k-1, sumb - b[lo], dp)
            if b[lo] == 1: lo_ev += 1
            if lo == hi:
                ev += lo_ev
            else:
                hi_ev = white(b[:hi] + b[hi+1:], n-1, k-1, sumb - b[hi], dp)
                if b[hi] == 1: hi_ev += 1
                ev += 2*max(lo_ev, hi_ev)
            lo += 1; hi -= 1
        ev /= n

    dp[(b, k)] = dp[(tuple(reversed(b)), k)] = ev
    return ev

def main():
    n, k = map(int, input().split())
    b = tuple([1 if ball == 'W' else 0 for ball in input()])

    dp = dict()

    print(white(b, n, k, sum(b), dp))

main()
