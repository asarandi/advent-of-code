#!/usr/bin/env python3

with open("input.txt", "r") as fp:
    data = fp.read().strip()
    fp.close()

y, x, y0, x0, y1, x1 = 0, 0, 0, 0, 0, 0
d1, d2 = {(y, x): 1}, {(y, x): 1}
steps = {">": (0, 1), "<": (0, -1), "^": (-1, 0), "v": (1, 0)}
for i in range(len(data)):
    s = data[i]
    y, x = y + steps[s][0], x + steps[s][1]
    d1[(y, x)] = 1 if (y, x) not in d1 else d1[(y, x)] + 1
    if i & 1:
        y1, x1 = y1 + steps[s][0], x1 + steps[s][1]
        d2[(y1, x1)] = 1 if (y1, x1) not in d2 else d2[(y1, x1)] + 1
    else:
        y0, x0 = y0 + steps[s][0], x0 + steps[s][1]
        d2[(y0, x0)] = 1 if (y0, x0) not in d2 else d2[(y0, x0)] + 1

print("aoc2015d03p01:", len(d1))
print("aoc2015d03p02:", len(d2))
