#!/usr/bin/env python3

import shapes


def run(file_name: str, part_one: bool) -> int:
    data = [list(l) for l in open(file_name).read().splitlines()]
    H, W = len(data), len(data[0])

    def match(i: int, j: int, s: [[]]) -> int:
        h, w = len(s), len(s[0])
        if not ((i + h <= H) and (j + w <= W)):
            return 0
        for y in range(h):
            for x in range(w):
                if s[y][x] != "." and data[i + y][j + x] != s[y][x]:
                    return 0
        return 1

    res = 0
    for i in range(H * W):
        for s in shapes.xmas if part_one else shapes.mas:
            res += match(i // W, i % W, s)
    return res


print(run("input", True), run("input", False))
