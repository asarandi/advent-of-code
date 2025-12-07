#!/usr/bin/env python3

from functools import reduce

lines = open("sample").read().splitlines()

arr = [l.split() for l in lines]
h, w = len(arr), len(arr[0])
arr = [[arr[y][x] for y in range(h)] for x in range(w)]
print("part 1:", sum(map(lambda a: eval(a.pop().join(a)), arr)))

arr = list(map(list, lines))
h, w = len(arr), len(arr[0])
arr = list(map("".join, [[arr[y][x] for y in range(h)] for x in range(w)]))

n, op, store = 0, "", []
for i, v in enumerate(arr):
    v = v.strip()
    if v and v[-1] in ("*", "+"):
        op, store = v[-1], [int(v[:-1])]
    elif v:
        store.append(int(v))
    if (not v) or (i == len(arr) - 1):
        n += sum(store) if op == "+" else reduce(lambda i, j: i * j, store)
print("part 2:", n)
