#!/usr/bin/env python3


def find_num(s: str, rev: bool, p2: bool) -> int:
    nums = {
        "1": "one",
        "2": "two",
        "3": "three",
        "4": "four",
        "5": "five",
        "6": "six",
        "7": "seven",
        "8": "eight",
        "9": "nine",
    }

    if rev:
        s = s[::-1]
        nums = {k: v[::-1] for (k, v) in nums.items()}

    for i in range(len(s)):
        for k, v in nums.items():
            if (s[i:].find(k) == 0) or (p2 and s[i:].find(v) == 0):
                return int(k)


p1, p2 = 0, 0
for l in open("input.txt").read().splitlines():
    p1 += find_num(l, 0, 0) * 10 + find_num(l, 1, 0)
    p2 += find_num(l, 0, 1) * 10 + find_num(l, 1, 1)

print(p1, p2)
