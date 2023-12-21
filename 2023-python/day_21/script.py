#!/usr/bin/env pypy3

G = [list(l) for l in open("input.txt").read().splitlines()]
H, W = len(G), len(G[0])

for y in range(H):
    for x in range(W):
        if G[y][x] == "S":
            start = y, x
            G[y][x] = "."


def walk(queue: [tuple]) -> set:
    seen = set()
    while queue:
        node = queue.pop(0)
        y, x = node
        for dy, dx in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            dy, dx = dy + y, dx + x
            new_node = dy, dx

            gy, gx = dy, dx
            while gy < 0:
                gy += H
            while gx < 0:
                gx += W
            gy, gx = gy % H, gx % W
            if G[gy][gx] == ".":
                seen.add(new_node)
    return seen


nodes = [(start)]
prev_len = 1
cycles = []
for i in range(131 * 4):
    new_nodes = walk(nodes)
    nodes = list(new_nodes)
    n = len(nodes)
    delta = n - prev_len
    prev_len = n

    cycles = [delta] + cycles
    if len(cycles) > 131:
        cycles.pop()

    if i in (350, 350 - 131, 350 - 131 - 131):
        print(i, n, delta, cycles)
