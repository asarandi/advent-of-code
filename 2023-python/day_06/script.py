#!/usr/bin/env python3

import math, re


def get_input(fn: str, w: bool) -> ([int], [int]):
    s = open(fn).read().splitlines()
    p = lambda l: re.findall(r"(\d+)", l)
    f = lambda l: list(map(int, ["".join(p(l))] if w else p(l)))
    return f(s[0]), f(s[1])


def count(t: int, d: int) -> int:
    n = 0
    for i in range(t):
        n += 1 if (t - i) * i > d else 0
    return n


def solve(p2: bool) -> int:
    t, d = get_input("input.txt", p2)
    r = [0] * len(t)
    for i in range(len(t)):
        r[i] = count(t[i], d[i])
    return sum(r) if p2 else math.prod(r)


print(solve(False), solve(True))
