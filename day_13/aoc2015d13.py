#!/usr/bin/env python3

from math import inf

with open("input.txt", "r") as fp:
    data = fp.read().splitlines()
    fp.close()

guests = {}
for line in data:
    words = line[:-1].split(' ')
    name1, name2, value = words[0], words[10], int(words[3])
    value = -value if words[2] == "lose" else value
    guests[name1] = {} if name1 not in guests else guests[name1]
    guests[name1][name2] = value

def calc(lst: [], guests: {}):
    res = 0
    for i in range(len(lst)):
        left = (i + len(lst) - 1) % len(lst)
        right = (i + 1) % len(lst)
        res += guests[lst[i]][lst[left]]
        res += guests[lst[i]][lst[right]]
    return res

res = -inf
def permute(lst: [], guests: {}, idx: int):
    global res

    if idx == len(lst):
        h = calc(lst, guests)
        res = h if h > res else res
    else:
        for i in range(idx, len(lst)):
            lst[i], lst[idx] = lst[idx], lst[i]
            permute(lst, guests, idx + 1)
            lst[i], lst[idx] = lst[idx], lst[i]

permute(list(guests), guests, 0)
print("aoc2015d13p01:", res)

guests['me'] = {}
for g in guests:
    guests[g]['me'] = 0
    guests['me'][g] = 0

res = -inf
permute(list(guests), guests, 0)
print("aoc2015d13p02:", res)
