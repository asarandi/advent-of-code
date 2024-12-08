#!/usr/bin/env pypy3

import itertools


def run(filename, seq):
    G = open(filename).read().splitlines()
    L, H, W = {}, len(G), len(G[0])

    distance = lambda a, b: abs(a[0] - b[0]) + abs(a[1] - b[1])
    in_bounds = lambda a: 0 <= a[0] < H and 0 <= a[1] < W
    multiply = lambda a, m: (a[0] * m, a[1] * m)
    add = lambda a, b: (a[0] + b[0], a[1] + b[1])

    for i in range(H * W):
        c = G[i // W][i % W]
        if c.isalnum():
            L[c] = L[c] if c in L else []
            L[c].append((i // W, i % W))

    uniq = {}
    for l in L.values():
        for a, b in itertools.combinations(l, 2):
            (ay, ax), (by, bx), dist = a, b, distance(a, b)
            vy, wy = min(ay, by) - abs(ay - by), max(ay, by) + abs(ay - by)
            vx, wx = min(ax, bx) - abs(ax - bx), max(ax, bx) + abs(ax - bx)
            (vy, vx) = (vy, vx) if distance((vy, vx), a) == dist else (vy, wx)
            step = (ay - vy, ax - vx)

            for i in seq:
                arr = [add(a, multiply(step, -i)), add(b, multiply(step, i))]
                kv = {k: v for k, v in zip(arr, ["#", "#"]) if in_bounds(k)}
                uniq.update(kv)
                if not kv:
                    break
    return len(uniq)


print(run("input", range(1, 2)), run("input", range(50)))
