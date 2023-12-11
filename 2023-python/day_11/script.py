#!/usr/bin/env python3

from itertools import combinations as comb

G = [list(l) for l in open("input.txt").read().splitlines()]
H, W = len(G), len(G[0])
rows = ["#" not in G[y] for y in range(H)]
cols = ["#" not in [G[y][x] for y in range(H)] for x in range(W)]
galaxies = [(y, x) for y in range(H) for x in range(W) if G[y][x] == "#"]


def manhattan(pair: tuple, penalty: int) -> int:
    ((ay, ax), (by, bx)) = pair
    ct = sum(rows[min(ay, by) : max(ay, by)])
    ct += sum(cols[min(ax, bx) : max(ax, bx)])
    return abs(ay - by) + abs(ax - bx) + ct * (penalty - 1)


print(*[sum([manhattan(p, k) for p in comb(galaxies, 2)]) for k in (2, 1000000)])
