#!/usr/bin/env pypy3


def count_set_bits(n: int) -> int:
    ct = 0
    while n:
        n &= n - 1
        ct += 1
    return ct


def get_config(i: int, n: int) -> int:
    arr = []
    ct = 0
    for b in range(n - 1, -1, -1):
        if i & (1 << b) != 0:
            ct += 1
        else:
            if ct:
                arr.append(ct)
            ct = 0
    if ct:
        arr.append(ct)
    return tuple(arr)


def is_same_config(n: int, s: str) -> bool:
    for i in range(len(s) - 1, -1, -1):
        if s[i] == "#":
            if not (n & 1):
                return False
        elif s[i] == ".":
            if n & 1:
                return False
        n = n >> 1
    return True


p1 = 0
for l in open("input.txt").read().splitlines():
    l, r = l.split()
    r = tuple(list(map(int, r.split(","))))
    rs = sum(r)
    ct = 0
    for n in range(1 << len(l)):
        if count_set_bits(n) == rs:
            c = get_config(n, len(l))
            if (r == c) and (is_same_config(n, l)):
                ct += 1
    p1 += ct
print(p1)
