#!/usr/bin/env python3

G = [list(l) for l in open("input.txt").read().splitlines()]
H, W = len(G), len(G[0])

start, points = None, set()
for y in range(H):
    for x in range(W):
        points.add((y, x))
        if G[y][x] == "S":
            start = (y, x)
            G[y][x] = "J"  # FIXME: depends on input


# dfs because we want to move only in one direction (bfs would move in 2)
# needed for matplotlib.path.Path, tuples must be sequential, like drawing

stack, path, seen = [start], [], set()
while stack:
    node = stack.pop(0)
    if node in seen:
        continue
    seen.add(node)
    path.append(node)
    y, x = node
    for sy, sx in {
        "|": [(-1, 0), (1, 0)],
        "-": [(0, 1), (0, -1)],
        "L": [(-1, 0), (0, 1)],
        "J": [(-1, 0), (0, -1)],
        "7": [(1, 0), (0, -1)],
        "F": [(1, 0), (0, 1)],
    }[G[y][x]]:
        sy, sx = sy + y, sx + x
        stack = [(sy, sx)] + stack

import matplotlib

path = matplotlib.path.Path(path)
print(len(seen) // 2, sum(path.contains_points(list(points ^ seen))))
