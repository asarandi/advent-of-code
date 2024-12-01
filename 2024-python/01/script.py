#!/usr/bin/env python3

data = open("input").read().splitlines()

left, right, ct = [], [], {}
for l, r in [[int(i) for i in s.split()] for s in data]:
    left.append(l)
    right.append(r)
    ct[r] = ct[r] + 1 if r in ct else 1

left.sort(), right.sort()

a, b = 0, 0
for i, l in enumerate(left):
    a += abs(l - right[i])
    b += l * (ct[l] if l in ct else 0)

print(a, b)
