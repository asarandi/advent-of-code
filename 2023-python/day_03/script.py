#!/usr/bin/env python3

import math


def getnum(s: str, i: int) -> int:
    l, r = i, i
    while (0 <= l - 1) and (s[l - 1].isdigit()):
        l -= 1
    while (r + 1 < W) and (s[r + 1].isdigit()):
        r += 1
    return int(s[l : r + 1])


p1, p2 = 0, 0
adj = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
G = open("input.txt").read().splitlines()
H, W = len(G), len(G[0])
for y in range(H):
    for x in range(W):
        sym = G[y][x]
        if sym in ".0123456789":
            continue
        nums = set()
        for i, j in adj:
            i, j = i + y, j + x
            if G[i][j].isdigit():
                nums.add(getnum(G[i], j))
        p1 += sum(nums)
        p2 += math.prod(nums) if len(nums) == 2 and sym == "*" else 0
print(p1, p2)
