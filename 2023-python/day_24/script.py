#!/usr/bin/env python3

import re, itertools, z3


def point(t: tuple) -> tuple:
    px, py, pz, vx, vy, vz = t
    return px + vx, py + vy, pz + vz


slope = lambda p, q: (q[1] - p[1]) / (q[0] - p[0])
intercept = lambda p, m: p[1] - (m * p[0])


def is_future(t: tuple, x: int) -> bool:
    px, py, pz, vx, vy, vz = t
    assert vx != 0.0
    return (vx > 0 and px < x) or (vx < 0 and px > x)


minarea, maxarea = 7, 27  # sample
minarea, maxarea = 200000000000000, 400000000000000

r, f = r"(-?\d+)", "input.txt"
arr = [tuple(map(int, re.findall(r, l))) for l in open(f).read().splitlines()]

ct = 0
for i, j in itertools.combinations(arr, 2):
    pi = point(i)
    mi = slope(i, pi)
    bi = intercept(i, mi)

    pj = point(j)
    mj = slope(j, pj)
    bj = intercept(j, mj)

    if mi != mj:
        x = (bj - bi) / (mi - mj)
        y = mi * x + bi
        if (minarea <= x <= maxarea) and (minarea <= y <= maxarea):
            if is_future(i, x) and is_future(j, x):
                ct += 1

print(ct)


qx, qy, qz, wx, wy, wz = z3.Ints("qx qy qz wx wy wz")
s = z3.Solver()
for i in range(len(arr)):
    px, py, pz, vx, vy, vz = arr[i]
    t = z3.Int(f"t{i}")
    s.add(qx + wx * t == px + vx * t)
    s.add(qy + wy * t == py + vy * t)
    s.add(qz + wz * t == pz + vz * t)

s.check()
m = s.model()
qx, qy, qz = m[qx].as_long(), m[qy].as_long(), m[qz].as_long()
print(qx + qy + qz)
