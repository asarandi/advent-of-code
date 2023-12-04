#!/usr/bin/env python3

data = open("input.txt").read().splitlines()
p1, p2 = 0, [0] * len(data)
for i, s in enumerate(data):
    l, r = map(str.split, s.split(" | "))
    n = len(set(l) & set(r))
    p1 += 2 ** (n - 1) if n else 0
    p2[i] += 1
    for j in range(i + 1, n + i + 1):
        p2[j] += p2[i]
print(p1, sum(p2))
