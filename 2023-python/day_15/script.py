#!/usr/bin/env python3
def hash_algo(s: str) -> int:
    r = 0
    for c in s:
        r = (r + ord(c)) * 17 % 256
    return r


p1, p2, boxes = 0, 0, [{} for _ in range(256)]
for line in open("input.txt").read().splitlines():
    for s in line.split(","):
        p1 += hash_algo(s)
        if s[-1] == "-":
            label = s[:-1]
            index = hash_algo(label)
            if label in boxes[index]:
                del boxes[index][label]
        else:
            l, r = s.split("=")
            boxes[hash_algo(l)][l] = int(r)

for i in range(256):
    for j, k in enumerate(boxes[i].keys()):
        p2 += (i + 1) * (j + 1) * boxes[i][k]

print(p1, p2)
