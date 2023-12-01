#!/usr/bin/env python3

from heapq import heappush, heappop

with open("input.txt", "r") as fp:
    data = fp.read().splitlines()
    fp.close()

reactions, start = [], data[-1]
for line in data[:-2]:
    src, dst = line.split(" => ")[0], line.split(" => ")[1]
    reactions.append((dst, src))

reactions = sorted(reactions, key=lambda x: len(x[1]))
reactions = sorted(reactions, key=lambda x: len(x[0]), reverse=True)


def children(s: str) -> []:
    global reactions

    res = set()
    for i in range(len(s)):
        for k in reactions:
            dst, src = k
            if s[i : i + len(dst)] == dst:
                n = s[:i] + src + s[i + len(dst) :]
                res.add(n)
    return list(res)


seen, queue, goal = set(), [], "e"
heappush(queue, (len(start), 0, start))
while queue:
    k, dist, molecule = heappop(queue)
    seen.add(molecule)
    if molecule == goal:
        print("aoc2015d19p02:", dist)
        break
    for c in children(molecule):
        if c in seen:
            continue
        heappush(queue, (len(c), dist + 1, c))

if goal not in seen:
    print("not found")
