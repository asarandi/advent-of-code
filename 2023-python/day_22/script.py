#!/usr/bin/env pypy3

import re, itertools

bricks, reverse, supported_by = {}, {}, {}

c = itertools.count()
for l in open("input.txt").read().splitlines():
    n = next(c)
    reverse[n], supported_by[n] = [], set()
    x, y, z, X, Y, Z = map(int, re.findall(r"(\d+)", l))
    for i in range(x, X + 1):
        for j in range(y, Y + 1):
            for k in range(z, Z + 1):
                node = i, j, k
                bricks[node] = n
                reverse[n].append(node)
    for num in reverse:
        reverse[num] = tuple(reverse[num])


def reverse2bricks(r: dict) -> dict:
    b = {}
    for num, arr in r.items():
        for node in arr:
            b[node] = num
    return b


done = False
while not done:
    done = True
    new_reverse = {}
    for num, arr in reverse.items():
        new_arr = tuple((x, y, z - 1) for (x, y, z) in arr)
        can_fall = True
        for node in new_arr:
            if ((node in bricks) and (bricks[node] != num)) or (node[2] <= 0):
                can_fall = False
        if can_fall:
            arr = new_arr
            done = False
        new_reverse[num] = arr
    reverse = new_reverse
    bricks = reverse2bricks(reverse)

import copy


def remove_and_count_falling(reverse: dict, index: int) -> int:
    my_reverse = copy.deepcopy(reverse)
    del my_reverse[index]
    my_bricks = reverse2bricks(my_reverse)

    done = False
    while not done:
        done = True
        my_new_reverse = {}
        for num, arr in my_reverse.items():
            new_arr = tuple((x, y, z - 1) for (x, y, z) in arr)
            can_fall = True
            for node in new_arr:
                if ((node in my_bricks) and (my_bricks[node] != num)) or (node[2] <= 0):
                    can_fall = False
            if can_fall:
                arr = new_arr
                done = False
            my_new_reverse[num] = arr
        my_reverse = my_new_reverse
        my_bricks = reverse2bricks(my_reverse)

    res = 0
    for num in reverse:
        if num != index:
            if reverse[num] != my_reverse[num]:
                res += 1
    return res


for (x, y, z), num in bricks.items():
    below = x, y, z - 1
    if (below in bricks) and (bricks[below] != num):
        supported_by[num].add(bricks[below])


# for k, v in supported_by.items():
#    print(k, chr(ord("A") + k), reverse[k], v)


def can_remove(i: int) -> bool:
    for num, supp in supported_by.items():
        if len(supp) == 1 and i in supp:
            return False
    return True


p1, p2 = 0, 0
for i in range(n + 1):
    if can_remove(i):
        p1 += 1
    #        print("can remove", i)
    else:
        n = remove_and_count_falling(reverse, i)
        p2 += n
#        print("can NOT remove", i, "because", n, "would fall")

print(p1, p2)
