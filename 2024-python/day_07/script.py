#!/usr/bin/env pypy3


def calc(arr, n, base) -> int:
    val = arr.pop(0)
    while arr:
        val = {
            0: lambda v, w: v + w,
            1: lambda v, w: v * w,
            2: lambda v, w: int(str(v) + str(w)),
        }[n % base](val, arr.pop(0))
        n //= base
    return val


def run(filename: str, base: int) -> int:
    res = 0
    for l in open(filename).read().splitlines():
        arr = list(map(lambda i: int(i), l.replace(":", "").split()))
        x = arr.pop(0)
        for n in range(base ** (len(arr) - 1)):
            if x == calc(arr.copy(), n, base):
                res += x
                break
    return res

print(run("input", 2), run("input", 3))
