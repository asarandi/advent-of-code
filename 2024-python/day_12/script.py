#!/usr/bin/env python3

f = "input"
G, data = {}, open(f).read().splitlines()
for i, line in enumerate(data):
    for j, val in enumerate(line):
        G[(i, j)] = val

add = lambda a, b: (a[0] + b[0], a[1] + b[1])
URDL = [(-1, 0), (0, 1), (1, 0), (0, -1)]
DIAG = [(-1, 1), (1, 1), (1, -1), (-1, -1)]


def get_region(plot: tuple) -> set:
    queue, seen, perim = [plot], set(), 0
    while queue:
        node = queue.pop(0)
        if node in seen:
            continue
        seen.add(node)
        for step in URDL:
            new_node = add(step, node)
            if new_node in G and G[new_node] == G[node]:
                queue.append(new_node)
            else:
                perim += 1
    return seen, perim


def count_corners(region: set) -> int:
    res = 0
    for plot in region:
        for i in range(4):
            a = add(plot, URDL[i])
            b = add(plot, URDL[(i + 1) % 4])
            c = add(plot, DIAG[i])
            res += 1 if (a not in region) and (b not in region) else 0
            res += 1 if (a in region) and (b in region) and (c not in region) else 0
    return res


a, b, seen = 0, 0, set()
for key in G.keys():
    if key not in seen:
        region, perim = get_region(key)
        seen |= region
        corners = count_corners(region)
        a += len(region) * perim
        b += len(region) * corners

print(a, b)
