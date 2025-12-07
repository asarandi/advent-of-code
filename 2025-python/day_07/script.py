#!/usr/bin/env python3

import functools

lines = [list(l) for l in open("input").read().splitlines()]
h, w = len(lines), len(lines[0])

ans, start = 0, None
for y in range(h - 1):
    yd = y + 1
    for x in range(w):
        xl, xr = x - 1, x + 1
        if lines[y][x] == "S":
            start = (y, x)
            lines[yd][x] = "|"
        elif lines[y][x] == "|":
            is_split = False
            if lines[yd][x] == "^":
                if lines[yd][xl] == ".":
                    lines[yd][xl] = "|"
                    is_split = True
                if lines[yd][xr] == ".":
                    lines[yd][xr] = "|"
                    is_split = True
            else:
                lines[yd][x] = "|"
            ans += is_split
print(ans)


@functools.cache
def recurse(y, x) -> int:
    if h == y + 1:
        return 1
    if lines[y + 1][x] == "^":
        return recurse(y + 1, x - 1) + recurse(y + 1, x + 1)
    else:
        return recurse(y + 1, x)


print(recurse(*start))
