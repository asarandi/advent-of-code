#!/usr/bin/env python3

from itertools import combinations
from math import prod

euclidean = lambda a, b: (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2 + (a[2] - b[2]) ** 2

input_, max_conn = "sample", 10
input_, max_conn = "input", 1000

arr = open(input_).read().splitlines()
arr = [tuple(map(int, l.split(","))) for l in arr]

distances = list()
for pair in combinations(arr, 2):
    distances.append((euclidean(*pair), *pair))
distances.sort()

circuits = []


def merge(node: set) -> list:
    for c in list(circuits):
        if c & node:
            circuits.remove(c)
            c |= node
            return merge(c)
    circuits.append(node)
    return node


for i, (_, a, b) in enumerate(distances):
    group = merge({a, b})

    if i == max_conn - 1:
        counts = sorted([len(c) for c in circuits], reverse=True)
        print("part 1:", prod(counts[:3]))

    if len(group) == len(arr):
        print("part 2:", a[0] * b[0])
        break
