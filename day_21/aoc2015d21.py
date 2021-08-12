#!/usr/bin/env python3

from copy import deepcopy

with open("input.txt", "r") as fp:
    boss = [int(x.split(": ")[1]) for x in fp.read().splitlines()]
    fp.close()

# hp, damage, armor
def is_winner(player: [], boss: []) -> bool:
    p = True
    while player[0] > 0 and boss[0] > 0:
        if p:
            d = player[1] - boss[2]
            d = 1 if d < 1 else d
            boss[0] -= d
        else:
            d = boss[1] - player[2]
            d = 1 if d < 1 else d
            player[0] -= d
        p = not p
    return player[0] > 0


items = [
    [[8, 4, 0], [10, 5, 0], [25, 6, 0], [40, 7, 0], [74, 8, 0]],
    [[0, 0, 0], [13, 0, 1], [31, 0, 2], [53, 0, 3], [75, 0, 4], [102, 0, 5]],
    [[0, 0, 0], [25, 1, 0], [50, 2, 0], [100, 3, 0]],
    [[0, 0, 0], [20, 0, 1], [40, 0, 2], [80, 0, 3]],
]

p1, p2 = 999, -1
for i in range(len(items[0])):
    for j in range(len(items[1])):
        for k in range(len(items[2])):
            for l in range(len(items[3])):
                lst = [i, j, k, l]
                cost, damage, armor = 0, 0, 0
                for x in range(len(items)):
                    cost += items[x][lst[x]][0]
                    damage += items[x][lst[x]][1]
                    armor += items[x][lst[x]][2]
                if is_winner([100, damage, armor], deepcopy(boss)):
                    p1 = cost if cost < p1 else p1
                else:
                    p2 = cost if cost > p2 else p2

print("aoc2015d21p01:", p1)
print("aoc2015d21p02:", p2)
