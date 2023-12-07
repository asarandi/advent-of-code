#!/usr/bin/env python3

import collections, functools


def get_type(s: str, p: bool) -> int:
    c, j = collections.Counter(s), "J"
    d, v, cv = dict(c.items()), c.values(), collections.Counter(c.values())
    for b, t in [
        (5 in v, 7),
        (4 in v and p and j in d, 7),
        (3 in v and 2 in v and p and j in d, 7),
        (3 in v and p and j in d, 6),
        (2 in v and cv[2] == 2 and p and j in d and d[j] == 2, 6),
        (2 in v and cv[2] == 2 and p and j in d, 5),
        (2 in v and p and j in d, 4),
        (4 in v, 6),
        (3 in v and 2 in v, 5),
        (3 in v, 4),
        (2 in v and cv[2] == 2, 3),
        (2 in v, 2),
        (p and j in d, 2),
        (True, 1),
    ]:
        if b:
            return t


def get_rank(a: tuple, b: tuple) -> int:
    ah, _, p2 = a
    bh, *_ = b
    order = "AKQT98765432J" if p2 else "AKQJT98765432"
    for i in range(len(ah)):
        ai = order.index(ah[i])
        bi = order.index(bh[i])
        if ai < bi:
            return 1
        elif ai > bi:
            return -1
    return 0


def solve(p2: bool) -> int:
    arr = []
    for _ in range(8):
        arr.append([])
    for s in open("input.txt").read().splitlines():
        hand, bet = s.split()
        type_ = get_type(hand, p2)
        arr[type_] += [(hand, int(bet), p2)]
    arr = [sorted(a, key=functools.cmp_to_key(get_rank)) for a in arr]
    arr = [i for a in arr for i in a]
    return sum([(i + 1) * v[1] for i, v in enumerate(arr)])


print(solve(0), solve(1))
assert (solve(0) == 248105065) and (solve(1) == 249515436)
