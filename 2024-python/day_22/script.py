#!/usr/bin/env pypy3


def sequence(i: int) -> int:
    i = (i ^ (i * 64)) % 16777216
    i = (i ^ (i // 32)) % 16777216
    return (i ^ (i * 2048)) % 16777216


arr, cost = [], {}
for v in [int(l) for l in open("input").read().splitlines()]:
    w, delta, seen = 0, [], set()
    for _ in range(2000):
        v = sequence(v)
        w, delta = v % 10, delta + [w - v % 10]
        if len(delta) == 4:
            key, delta = tuple(delta), delta[1:]
            if key not in seen:
                seen.add(key)
                cost[key] = cost[key] + w if key in cost else w
    arr.append(v)

print(sum(arr), max(cost.values()))
