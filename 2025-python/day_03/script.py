#!/usr/bin/env python3


def get_num(s: str, n: int) -> int:
    digits = []
    for i in range(n):
        end = len(s) - (n - i - 1)
        digits.append(max(s[:end]))
        s = s[s.index(digits[-1]) + 1 :]
    return int("".join(digits))


a, b = 0, 0
for s in open("input").read().splitlines():
    a += get_num(s, 2)
    b += get_num(s, 12)
print(a, b)
