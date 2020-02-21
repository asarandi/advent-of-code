#!/usr/bin/env python3

with open("input.txt", "r") as fp:
    data = [int(x) for x in fp.read().splitlines()]
    fp.close()

k = len(data) + 1
p1, p2 = 0, 0
def perm(work: [], containers: [], unique: {}, idx: int, n: int):
    global k, p1, p2
    if sum(work) == n:
        p1 += 1
        p2 = 0 if len(work) < k else p2
        k = len(work) if len(work) < k else k
        p2 = p2 + 1 if len(work) == k else p2
    else:
        for i in range(idx, len(containers)):
            if i in unique:
                continue
            work.append(containers[i])
            unique.add(i)
            perm(work, containers, unique, i, n)
            unique.remove(i)
            work.pop(-1)

perm([], data, set(), 0, 150)

print("aoc2015d17p01:", p1)
print("aoc2015d17p02:", p2)
