#!/usr/bin/env pypy3

steps = {"<": (0, -1), "^": (-1, 0), ">": (0, 1), "v": (1, 0)}
turns = {"<": "^", "^": ">", ">": "v", "v": "<"}
G, curr, cy, cx = {}, "?", None, None
data = open("input").read().splitlines()

for i in range(len(data)):
    for j in range(len(data[0])):
        if data[i][j] in steps.keys():
            curr, cy, cx = data[i][j], i, j
            G[(i, j)] = "."
        else:
            G[(i, j)] = data[i][j]


def run() -> (bool, set):
    n, seen, queue = 0, set(), [(curr, cy, cx)]
    while queue:
        (c, y, x) = queue.pop(0)
        n += 1
        if n > 10000:
            return True, seen
        seen.add((y, x))

        sy, sx = steps[c]
        sy, sx = sy + y, sx + x
        if (sy, sx) in G:
            if G[(sy, sx)] == ".":
                queue.append((c, sy, sx))
            else:
                queue.append((turns[c], y, x))
    return False, seen


_, seen = run()
print(len(seen))

num_loop = 0
for key in seen:
    if key == (cy, cx):
        continue
    if G[key] == ".":
        G[key] = "#"
        is_loop, _ = run()
        num_loop += int(is_loop)
        G[key] = "."

print(num_loop)
