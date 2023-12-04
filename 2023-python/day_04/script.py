#!/usr/bin/env python3

p1, p2 = 0, 0
data = open("input.txt").read().splitlines()
rep = [0] * len(data)
for i, s in enumerate(data):
    l, r = map(str.split, s.split(" | "))
    n = len(set(l) & set(r))
    for _ in range(rep[i] + 1):
        for j in range(i + 1, n + i + 1):
            rep[j] += 1
    p1 += 2 ** (n - 1) if n else 0
    p2 += rep[i] + 1
print(p1, p2)
