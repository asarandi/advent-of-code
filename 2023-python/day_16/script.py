#!/usr/bin/env pypy3

G = open("input.txt").read().splitlines()
H, W = len(G), len(G[0])
U, R, D, L = (-1, 0), (0, 1), (1, 0), (0, -1)


def search(start: tuple) -> int:
    queue, seen, energized = [start], set(), set()

    while queue:
        node = queue.pop()
        (pos, dir_) = node
        ((y, x), (dy, dx)) = node

        if (y < 0) or (x < 0) or (H <= y) or (W <= x):
            continue
        if node in seen:
            continue

        seen.add(node)
        energized.add(pos)
        sym = G[y][x]

        if sym in "/\\":
            tab = {"/": {R: U, L: D, D: L, U: R}, "\\": {R: D, L: U, D: R, U: L}}
            (dy, dx) = tab[sym][dir_]
            queue.append(((y + dy, x + dx), (dy, dx)))
        elif sym in "-|":
            tab = {"-": (L, R), "|": (U, D)}
            if dir_ in tab[sym]:
                queue.append(((y + dy, x + dx), (dy, dx)))
            else:
                for dy, dx in tab[sym]:
                    queue.append(((y + dy, x + dx), (dy, dx)))
        else:
            queue.append(((y + dy, x + dx), (dy, dx)))

    return len(energized)


best = -1
for y in range(H):
    best = max(best, search(((y, 0), R)))
    best = max(best, search(((y, W - 1), L)))
for x in range(W):
    best = max(best, search(((0, x), D)))
    best = max(best, search(((H - 1, x), U)))

print(search(((0, 0), R)), best)
