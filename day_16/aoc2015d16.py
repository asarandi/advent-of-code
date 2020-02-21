#!/usr/bin/env python3

with open("input.txt", "r") as fp:
    data = fp.read().splitlines()
    fp.close()

aunts = []
for line in data:
    line = ': '.join(line.split(': ')[1:])
    words = line.split(', ')
    aunt = {}
    for w in words:
        name, quantity = w.split(': ')[0], int(w.split(': ')[1])
        aunt[name] = quantity
    aunts.append(aunt)

sue = {'children': 3, 'cats': 7, 'samoyeds': 2, 'pomeranians': 3, 'akitas': 0, 'vizslas': 0, 'goldfish': 5, 'trees': 3, 'cars': 2, 'perfumes': 1}
for i in range(len(aunts)):
    f = True
    for k in aunts[i]:
        if aunts[i][k] != sue[k]:
            f = False
            break
    if f:
        print("aoc2015d16p01:", i + 1)

    f = True
    for k in aunts[i]:
        if k in {'cats', 'trees'}:
            if aunts[i][k] <= sue[k]:
                f = False
                break
        elif k in {'pomeranians', 'goldfish'}:
            if aunts[i][k] >= sue[k]:
                f = False
                break
        else:
            if aunts[i][k] != sue[k]:
                f = False
                break
    if f:
        print("aoc2015d16p02:", i + 1)
