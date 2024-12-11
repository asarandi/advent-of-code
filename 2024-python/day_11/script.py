#!/usr/bin/env python3

import functools


@functools.cache
def calc(i: int, t: int) -> int:
    s, n = str(i), len(str(i))
    if t == 0:
        return 1
    elif i == 0:
        return calc(1, t - 1)
    elif n % 2 == 0:
        a, b = int(s[: n // 2]), int(s[n // 2 :])
        return calc(a, t - 1) + calc(b, t - 1)
    return calc(i * 2024, t - 1)


run = lambda f, t: sum([calc(int(i), t) for i in open(f).read().split(" ")])
print(run("input", 25), run("input", 75))
