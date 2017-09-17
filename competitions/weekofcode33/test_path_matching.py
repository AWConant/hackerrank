

def test():
    from random import randrange, choice, shuffle

    mini_alpha = 'ab'
    alpha = ascii_lowercase

    MAXN = 50000

    get = lambda m: randrange(1, m+1)
    n, q = get(MAXN), get(MAXN)

    n = 50000 # DEBUG
    q = 30000

    s = ''.join(choice(alpha) for _ in range(n))
    p = choice(s)

    vertices = list(range(1, n+1))
    g = defaultdict(list)
    root = 1

    # read edges and build graph
    grow_root = choice(vertices)
    roots = [grow_root]
    endpoints = list(vertices)
    endpoints.remove(grow_root)
    shuffle(endpoints)
    for _ in range(n-1):
        u, v = choice(roots), endpoints.pop()
        roots.append(v)
        g[u].append(v)
        g[v].append(u)

    # Set up O(1) path LCA lookups
    LOG2N = cache_log_values(n, MAXN)
    parent_of = get_parent_pointers(g, root)
    euler, level, fai = dfs_util(g, vertices, root, parent_of)
    depths = [level[x] for x in euler]
    st = build_sparse_table(depths)

    bad = 0
    for kase in range(q):
        u, v = get(n), get(n)
        lca = get_lca(u, v, fai, euler, st, depths, LOG2N)
        path = deque(list(iterate_path(u, v, lca, parent_of)))
        s_prime = ''.join(s[i-1] for i in path)
        naive_s_prime, naive_path = naive(g, s, p, u, v)
        naive_ans = search(naive_s_prime, p)
        ans = search(s_prime, p)
        if ans != naive_ans:
            print(u, v, ans, naive_ans, s_prime, naive_s_prime)
            bad += 1
    print('mismatches:', bad)

################################################################
