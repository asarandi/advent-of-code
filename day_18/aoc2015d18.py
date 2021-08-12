#!/usr/bin/env python3

from copy import deepcopy

with open("input.txt", "r") as fp:
    data = [list(x) for x in fp.read().splitlines()]
    fp.close()


def conway(lst: [], flip: bool) -> int:
    res = 0
    pos = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    always = {
        (0, 0),
        (0, len(lst[0]) - 1),
        (len(lst) - 1, 0),
        (len(lst) - 1, len(lst[0]) - 1),
    }
    for t in range(100):
        for k in always:
            y, x = k
            lst[y][x] = "#" if flip else lst[y][x]
        clone, res = deepcopy(lst), 0
        for i in range(len(lst)):
            for j in range(len(lst[i])):
                n = 0
                for k in pos:
                    y, x = k[0] + i, k[1] + j
                    if not (y >= 0 and y < len(lst)):
                        continue
                    if not (x >= 0 and x < len(lst[i])):
                        continue
                    n = n + 1 if lst[y][x] == "#" else n
                if lst[i][j] == "#":
                    clone[i][j] = "#" if n == 2 or n == 3 else "."
                else:
                    clone[i][j] = "#" if n == 3 else "."
                if (i, j) in always:
                    clone[i][j] = "#" if flip else clone[i][j]
                res = res + 1 if clone[i][j] == "#" else res
        lst = clone
    return res


print("aoc2015d18p01:", conway(deepcopy(data), False))
print("aoc2015d18p02:", conway(deepcopy(data), True))
