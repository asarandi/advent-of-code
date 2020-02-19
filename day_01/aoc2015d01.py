#!/usr/bin/env python3

with open('input.txt', 'r') as fp:
    data = fp.read().strip()
    fp.close()

floor = data.count('(') - data.count(')')
print("aoc2015d01p01:", floor)

floor, i = 0, 0
while floor >= 0 and i < len(data):
    floor = floor + 1 if data[i] == '(' else floor - 1
    i += 1

print("aoc2015d01p02:", i)
