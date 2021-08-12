#!/usr/bin/env python3


def to_list(s: str) -> []:
    return [ord(c) - ord("a") for c in s]


def to_str(lst: []) -> str:
    return "".join([chr(c + ord("a")) for c in lst])


def increment(lst: []) -> []:
    for i in range(len(lst) - 1, -1, -1):
        lst[i] = (lst[i] + 1) % 26
        if lst[i] != 0:
            break
    return lst


def is_valid(lst: []) -> bool:
    f = False
    for i in range(0, len(lst) - 2):
        if lst[i] + 1 == lst[i + 1] and lst[i] + 2 == lst[i + 2]:
            f = True
            break
    if not f:
        return False

    forbidden = {"i", "o", "l"}
    for i in range(len(lst)):
        if chr(lst[i] + ord("a")) in forbidden:
            return False

    f = False
    for i in range(len(lst) - 3):
        if lst[i] == lst[i + 1]:
            for j in range(i + 2, len(lst) - 1):
                if lst[j] == lst[j + 1]:
                    f = True
                    break
    return f


puzzle = "hxbxwxba"

lst = to_list(puzzle)
while not is_valid(lst):
    lst = increment(lst)
print("aoc2015d11p01:", to_str(lst))

lst = increment(lst)
while not is_valid(lst):
    lst = increment(lst)
print("aoc2015d11p02:", to_str(lst))
