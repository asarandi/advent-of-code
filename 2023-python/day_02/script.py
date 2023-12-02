#!/usr/bin/env python3
import re, math

p1, p2 = 0, 0
lim = {"red": 12, "green": 13, "blue": 14}
for l in open("input.txt").read().splitlines():
    g = int(re.match(r"^Game (\d+)", l).group(1))
    d = {k: 0 for k in lim}
    for v, k in map(str.split, re.findall(r"(\d+ \w+)", l)):
        d[k] = int(v) if int(v) > d[k] else d[k]
    p1 += g if all(map(lambda k: d[k] <= lim[k], d)) else 0
    p2 += math.prod(d.values())
print(p1, p2)
