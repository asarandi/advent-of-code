#!/usr/bin/env python3

from math import inf

p1, p2 = inf, -inf


def permute(path: [], cities: {}, idx: int):
    global p1, p2
    if idx == len(path):
        dist = 0
        for i in range(1, len(path)):
            dist += cities[path[i - 1]][path[i]]
        p1 = min(p1, dist)
        p2 = max(p2, dist)
    else:
        for i in range(idx, len(path)):
            path[i], path[idx] = path[idx], path[i]
            permute(path, cities, idx + 1)
            path[i], path[idx] = path[idx], path[i]


with open("input.txt", "r") as fp:
    data = fp.read().splitlines()
    fp.close()

cities = {}
for line in data:
    src, dst, d = line.split(" ")[0], line.split(" ")[2], int(line.split(" ")[4])
    if src not in cities:
        cities[src] = {}
    if dst not in cities:
        cities[dst] = {}
    cities[dst][src] = d
    cities[src][dst] = d

permute(list(cities), cities, 0)
print("aoc2015d09p01:", p1)
print("aoc2015d09p01:", p2)
