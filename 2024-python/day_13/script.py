#!/usr/bin/env python3

import re, z3


def solve(a, b, prize) -> tuple:
    i, j = z3.Ints("i, j")
    s = z3.Solver()
    s.add((a[0] * i) + (b[0] * j) == prize[0])
    s.add((a[1] * i) + (b[1] * j) == prize[1])
    if s.check() == z3.sat:
        m = s.model()
        return m[i].as_long(), m[j].as_long()


def run(filename: str, part_one: bool) -> int:
    res, k = 0, 0 if part_one else 10**13
    getints = lambda s: map(lambda i: int(i), re.findall(r"([+-]?\d+)", s))
    for block in open(filename).read().strip().split("\n\n"):
        a, b, prize = map(lambda s: getints(s), block.split("\n"))
        if sol := solve(a, b, (prize[0] + k, prize[1] + k)):
            res += sol[0] * 3 + sol[1] * 1
    return res


print(run("input", True), run("input", False))
