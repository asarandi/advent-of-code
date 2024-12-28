#!/usr/bin/env python3

combine = lambda a, b: (a[i] + b[i] for i in range(5))
is_match = lambda a: all(map(lambda v: v <= 5, a))

locks, keys = [], []
for b in open("input").read().split("\n\n"):
    b = b.splitlines()
    is_lock = b[0] == "#####"
    b = b[1:] if is_lock else b[:6]
    a = [0] * 5
    for i in range(6 * 5):
        a[i % 5] += 1 if b[i // 5][i % 5] == "#" else 0
    if is_lock:
        locks.append(a)
    else:
        keys.append(a)

print(sum([int(is_match(combine(l, k))) for l in locks for k in keys]))
