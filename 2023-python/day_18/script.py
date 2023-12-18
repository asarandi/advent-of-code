#!/usr/bin/env pypy3

U, R, D, L = (-1, 0), (0, 1), (1, 0), (0, -1)
dirs = {"U": U, "R": R, "D": D, "L": L}
G, rgb, pos = {}, [], (0, 0)

for l in open("input.txt").read().splitlines():
    ch, num, code = l.split()
    value, index = int(code[2:7], 16), int(code[7])
    rgb.append((value, index))
    dy, dx = dirs[ch]
    y, x = pos
    for _ in range(int(num)):
        y, x = y + dy, x + dx
        G[y, x] = "#"
    pos = y, x

queue = [(1, 1)]
while queue:
    y, x = queue.pop()
    if (y, x) not in G:
        G[y, x] = "#"
        for dy, dx in dirs.values():
            dy, dx = y + dy, x + dx
            queue.append((dy, dx))


# https://www.geeksforgeeks.org/area-of-a-polygon-with-given-n-ordered-vertices/
def polygonArea(X, Y):
    area = 0.0
    n = len(X)
    j = n - 1
    for i in range(0, n):
        area += (X[j] + X[i]) * (Y[j] - Y[i])
        j = i
    return int(abs(area / 2.0))


y, x, edges, arr = 0, 0, 0, [(0, 0)]
for value, index in rgb:
    dy, dx = [R, D, L, U][index]
    y, x, edges = y + dy * value, x + dx * value, edges + value
    arr.append((y, x))

area = polygonArea(*zip(*arr))
print(len(G), area + edges // 2 + 1)
