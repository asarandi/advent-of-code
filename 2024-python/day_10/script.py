#!/usr/bin/env python3


def run(filename: str, part_one: bool) -> int:
    data = open(filename).read().splitlines()
    H, W = len(data), len(data[0])
    G = {(y, x): int(data[y][x]) for y in range(H) for x in range(W)}

    def search(start):
        ct, queue, seen = 0, [start], set()
        while queue:
            node = queue.pop(0)
            if node in seen and part_one:
                continue
            seen.add(node)
            ct += 1 if G[node] == 9 else 0
            add = lambda a, b: (a[0] + b[0], a[1] + b[1])
            for step in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                step = add(step, node)
                if step in G and G[step] == G[node] + 1:
                    queue.append(step)
        return ct

    return sum([search(k) for k, v in G.items() if v == 0])


print(run("input", True), run("input", False))
