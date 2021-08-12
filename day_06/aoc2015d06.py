#!/usr/bin/env python3

with open("input.txt", "r") as fp:
    data = fp.read().splitlines()
    fp.close()

g1, g2 = [], []
for i in range(1000):
    g1.append([0] * 1000)
    g2.append([0] * 1000)
for line in data:
    w = line.split(" ")
    if w[1] == "off":
        op, idx = 0, 2
    elif w[1] == "on":
        op, idx = 1, 2
    else:
        op, idx = 2, 1
    src = w[idx].split(",")
    dst = w[idx + 2].split(",")
    for i in range(int(src[0]), int(dst[0]) + 1):
        for j in range(int(src[1]), int(dst[1]) + 1):
            g1[i][j] = g1[i][j] ^ 1 if op == 2 else op
            g2[i][j] = 0 if g2[i][j] < 1 else g2[i][j] - 1 if op == 0 else g2[i][j]
            g2[i][j] += op

print("aoc2015d06p01:", sum([sum(x) for x in g1]))
print("aoc2015d06p02:", sum([sum(x) for x in g2]))
