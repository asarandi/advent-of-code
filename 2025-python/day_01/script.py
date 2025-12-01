#!/usr/bin/env python3

v, a, b = 50, 0, 0
for l in open("input").read().splitlines():
    c, i = l[0], int(l[1:])
    b, i = b + (i // 100), i % 100
    b = b + 1 if ((c == "R") and (v != 0) and (100 <= (v + i))) else b
    b = b + 1 if ((c == "L") and (v != 0) and ((v - i) <= 0)) else b
    v = (v + i) % 100 if c == "R" else (v + 100 - i) % 100
    a = a + 1 if v == 0 else a

print(a, b)
