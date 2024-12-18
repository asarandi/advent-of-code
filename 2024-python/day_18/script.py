#!/usr/bin/env python3


def get_input(f: str, limit: int) -> list:
    res = []
    for index, l in enumerate(open("input").read().splitlines()):
        x, y = map(lambda i: int(i), l.split(","))
        res += [(x, y)]
        if index == limit - 1:
            break
    return res


def traverse(obstacles: list) -> int:
    obstacles = set(obstacles)
    W, H = 71, 71
    goal = (W - 1, H - 1)
    add = lambda a, b: (a[0] + b[0], a[1] + b[1])
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    in_bounds = lambda a: 0 <= a[0] < W and 0 <= a[1] < H

    queue, seen = [((0, 0), [(0, 0)])], {}
    while queue:
        node, path = queue.pop(0)
        if node == goal:
            return len(set(path))

        if node in seen:
            continue
        seen[node] = True

        for i in range(4):
            new_node = add(directions[i], node)
            if new_node in obstacles:
                continue
            if in_bounds(new_node):
                queue.append((new_node, path + [new_node]))
    return None


left, right = 0, 3450 - 1
while left <= right:
    mid = (left + right) // 2
    input_ = get_input("input", mid + 1)
    a, b = traverse(input_[:-1]), traverse(input_)
    if a and b:
        left = mid + 1
    elif (not a) and (not b):
        right = mid - 1
    elif a and (not b):
        print(input_[-1])
        break
