#!/usr/bin/env pypy3

import copy


G = [list(l) for l in open("input.txt").read().splitlines()]
H, W = len(G), len(G[0])

start = 0, G[0].index(".")
stop = H - 1, G[H - 1].index(".")

tab = {"^": (-1, 0), ">": (0, 1), "v": (1, 0), "<": (0, -1)}

nodes = {}
distance = {}
for y in range(H):
    for x in range(W):
        if G[y][x] in ".v^><":
            nodes[y, x] = []
            for dy, dx in tab.values():
                dy, dx = dy + y, dx + x
                if (0 <= dy < H) and (0 <= dx < W) and (G[dy][dx] in ".><v^"):
                    nodes[y, x].append((dy, dx))
                    distance[((y, x), (dy, dx))] = 1

print("before", len(nodes), len(distance))

done = False
while not done:
    done = True

    nodes_copy = copy.deepcopy(nodes)
    skip = set()
    for k, v in nodes_copy.items():
        if k in skip:
            continue
        if len(v) == 2:
            a, b = v
            skip.add(a)
            skip.add(b)

            n = distance[(k, a)] + distance[(k, b)]
            distance[(a, b)] = n
            distance[(b, a)] = n
            nodes[a].remove(k)
            nodes[a].append(b)
            nodes[b].remove(k)
            nodes[b].append(a)
            del distance[(k, a)]
            del distance[(a, k)]
            del distance[(k, b)]
            del distance[(b, k)]
            del nodes[k]

            done = False


print("after", len(nodes), len(distance))


seen = set()
best = 0
stack = [(0, (start,))]
while stack:
    dist, path = stack.pop()
    node = path[-1]
    if node == stop:
        if dist > best:
            best = dist
            print("best", best)
    for neighbor in nodes[node]:
        if neighbor in path:
            continue
        new_distance = dist + distance[(node, neighbor)]
        stack.append((new_distance, tuple(list(path) + [neighbor])))
