#!/usr/bin/env python3

import heapq


def get_input(f: str) -> tuple:
    start, end, maze = None, None, {}
    for i, l in enumerate(open(f).read().splitlines()):
        for j, c in enumerate(l):
            start = (i, j) if c == "S" else start
            end = (i, j) if c == "E" else end
            maze[(i, j)] = "." if c in ("S", "E") else c
    return start, end, maze


def search(input_: tuple) -> tuple:
    add = lambda a, b: (a[0] + b[0], a[1] + b[1])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    (start, end, maze) = input_
    queue = [(0, 0, start, [start])]
    best_score, best_path, seen = 9999999, set(), {}
    while queue:
        node = heapq.heappop(queue)
        (g, dir_, pos, path) = node

        key = (dir_, pos)
        if (key in seen) and (seen[key] < g):
            continue
        seen[key] = g

        if pos == end and g <= best_score:
            best_score = g
            best_path |= set(path)

        moves = []
        if (ch := add(directions[dir_], pos)) in maze and maze[ch] != "#":
            moves.append((g + 1, dir_, ch, path + [ch]))

        for direction in [(dir_ + 3) % 4, (dir_ + 1) % 4]:
            moves.append((g + 1000, direction, pos, path))

        for new_node in moves:
            heapq.heappush(queue, new_node)

    return best_score, len(best_path)


print(*search(get_input("input")))
