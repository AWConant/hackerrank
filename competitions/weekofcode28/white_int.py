#!/bin/python3

def reverse(b, n):
    return sum(1 << (n-1-i) for i in range(n) if b >> i&1)

def get_bit(b, i):
    return (b >> i) & 1

def remove_bit(x, n, i):
    mask = 2**(i+1) - 1
    bits = x & ~mask
    x &= ~(1<<i)
    x &= ~(1<<n-1)
    return (bits >> 1) | (x & mask)

def white(b, n, k, dp):
    try: return dp[(b, k)]
    except KeyError: pass

    if k == 1:
        summ = 0
        lo = 0; hi = n - 1
        while lo <= hi:
            v = max(get_bit(b, lo), get_bit(b, hi)) 
            if lo != hi: v *= 2
            summ += v
            lo += 1; hi -= 1
        ev = summ/n
    else:
        ev = 0
        lo = 0; hi = n - 1
        while lo <= hi:
            lo_ev = white(remove_bit(b, n, lo), n-1, k-1, dp)
            if get_bit(b, lo) == 1: lo_ev += 1
            if lo == hi:
                ev += lo_ev
            else:
                hi_ev = white(remove_bit(b, n, hi), n-1, k-1, dp)
                if get_bit(b, hi) == 1: hi_ev += 1
                ev += 2*max(lo_ev, hi_ev)
            lo += 1; hi -= 1
        ev /= n

    dp[(b, k)] = dp[(reverse(b, n), k)] = ev
    return ev

def main():
    n, k = map(int, input().split())
    b = 0
    for i, ball in enumerate(input()):
        if ball == 'W':
            b |= 2**i

    dp = dict()

    print(white(b, n, k, dp))

if __name__ == '__main__':
    main()
