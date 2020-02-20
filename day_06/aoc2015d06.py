#!/usr/bin/env python3

with open("input.txt", "r") as fp:
    data = fp.read().splitlines()
    fp.close()

g1, g2 = [], []
for i in range(1000):
    g1.append([0] * 1000)
    g2.append([0] * 1000)
for line in data:
    w = line.split(' ')
    if w[1] == "off":
        op, idx = 0, 2
    elif w[1] == "on":
        op, idx = 1, 2
    else:
        op, idx = 2, 1
    src = w[idx].split(',')
    dst = w[idx+2].split(',')
    for i in range(int(src[0]), int(dst[0]) + 1):        
        for j in range(int(src[1]), int(dst[1]) + 1):
            g1[i][j] = g1[i][j] ^ 1 if op == 2 else op
            if op == 0:
                g2[i][j] = 0 if g2[i][j] < 1 else g2[i][j] - 1
            g2[i][j] += op

p1 = p2 = 0
for i in range(1000):
    p1 += sum(g1[i])
    p2 += sum(g2[i])
print("aoc2015d06p1:", p1)
print("aoc2015d06p2:", p2)
