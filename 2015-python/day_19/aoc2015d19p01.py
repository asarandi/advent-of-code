#!/usr/bin/env python3

with open("input.txt", "r") as fp:
    data = fp.read().splitlines()
    fp.close()

d, s = {}, data[-1]
for line in data[:-2]:
    src, dst = line.split(" => ")[0], line.split(" => ")[1]
    d[src] = [] if src not in d else d[src]
    d[src].append(dst)

u = set()
for k in d:
    for j in d[k]:
        i = 0
        while i < len(s):
            p = s.find(k, i)
            if p == -1:
                break
            i = p + len(k)
            u.add(s[:p] + j + s[i:])
print("aoc2015d19p01:", len(u))
