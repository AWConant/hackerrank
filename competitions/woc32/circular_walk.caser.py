from random import randrange

with open('circular_walk.random', 'w') as f:
    n = randrange(1, 10**7 + 1)
    s = randrange(0, n)
    t = randrange(0, n)
    p = randrange(1, n+1)
    r_0 = randrange(0, p)
    g = randrange(0, p)
    seed = randrange(0, p)

    f.write('%d %d %d\n%d %d %d %d' % (n, s, t, r_0, g, seed, p))
