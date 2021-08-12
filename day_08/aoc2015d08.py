#!/usr/bin/env python3

with open("input.txt", "r") as fp:
    data = fp.read().splitlines()
    fp.close()

a = b = c = 0
for line in data:
    a += len(line)
    b += len(eval(line))
    c += len(line.encode("unicode_escape").replace(b'"', b'\\"')) + 2

print("aoc2015d08p01:", a - b)
print("aoc2015d08p02:", c - a)
