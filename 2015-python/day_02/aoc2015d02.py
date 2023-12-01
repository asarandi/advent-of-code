#!/usr/bin/env python3

with open("input.txt", "r") as fp:
    data = fp.read().splitlines()
    fp.close

data = [sorted([int(x) for x in line.split("x")]) for line in data]
paper, ribbon = 0, 0
for lwh in data:
    l, w, h = lwh[0], lwh[1], lwh[2]
    paper += l * w + 2 * l * w + 2 * w * h + 2 * h * l
    ribbon += 2 * l + 2 * w + l * w * h

print("aoc2015d02p01:", paper)
print("aoc2015d02p02:", ribbon)
