#!/usr/bin/env python3

import re
import functools

with open("input.txt") as fp:
    S = fp.read().splitlines()
    fp.close()

ingr = [tuple(map(int, re.compile(r"-?\d+").findall(s))) for s in S]


def quantity():
    for a in range(101):
        for b in range(101 - a):
            for c in range(101 - a - b):
                yield a, b, c, 100 - a - b - c


def search():
    for q in quantity():
        score = [0, 0, 0, 0, 0]
        for i, props in enumerate(ingr):
            for j, val in enumerate(props):
                score[j] += val * q[i]

        if all(map(lambda i: i > 0, score[:4])):
            i = functools.reduce(lambda x, y: x * y, score[:4])
            yield i, score[-1] == 500


p1, p2 = 0, 0
for s, f in search():
    p1 = s if s > p1 else p1
    p2 = s if f and s > p2 else p2

print(p1, p2)
