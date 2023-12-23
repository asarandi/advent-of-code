#!/usr/bin/env pypy3

G = [list(l) for l in open("input.txt").read().splitlines()]
H, W = len(G), len(G[0])

start = 0, G[0].index(".")
stop = H - 1, G[H - 1].index(".")

tab = {"^": (-1, 0), ">": (0, 1), "v": (1, 0), "<": (0, -1)}
best = 0
stack = [(start,)]
while stack:
    path = stack.pop()
    node = path[-1]
    if node == stop:
        if len(path) - 1 > best:
            best = len(path) - 1
            print("best", best)
    ny, nx = node
    ch = G[ny][nx]
    if ch in tab:
        y, x = tab[ch]
        y, x = y + ny, x + nx
        new_node = y, x
        if new_node not in path:
            stack.append(tuple(list(path) + [new_node]))
        continue
    for y, x in tab.values():
        y, x = y + ny, x + nx
        new_node = y, x
        if (0 <= y < H) and (0 <= x < W) and (G[y][x] in ".><v^"):
            if new_node not in path:
                stack.append(tuple(list(path) + [new_node]))
