#!/usr/bin/env python3

import math

ll = open("input.txt").read().splitlines()
steps, ll = ll[0], ll[2:]

maze = {}
for i, l in enumerate(ll):
    k, v = l.split(" = ")
    l, r = v[1:4], v[6:9]
    maze[k] = (l, r)

get_step = lambda p, i: maze[p][0] if steps[i] == "L" else maze[p][1]

p, ct = "AAA", 0
while not p == "ZZZ":
    p = get_step(p, ct % len(steps))
    ct += 1
print(ct)

positions = list(filter(lambda k: k[-1] == "A", maze.keys()))
ct = [0] * len(positions)
for i, p in enumerate(positions):
    while not p[-1] == "Z":
        p = get_step(p, ct[i] % len(steps))
        ct[i] += 1

print(math.lcm(*ct))
