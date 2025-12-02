#!/usr/bin/env python3

a, b = 0, 0
for item in open("input").read().split(","):
    lo, hi = map(int, item.split("-"))
    for i in range(lo, hi + 1):
        s = str(i)
        m, n = len(s), len(s) // 2
        a += i if (m % 2 == 0) and (s[n:] == s[:n]) else 0
        # https://stackoverflow.com/a/67839706
        b += i if (s + s).index(s, 1) < m else 0
print(a, b)
