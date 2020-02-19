#!/usr/bin/env python3

def is_nice_1(s: str) -> bool:
    d = False
    f = {'ab', 'cd', 'pq', 'xy'}
    v = {'a', 'e', 'i', 'o', 'u'}
    vc = 1 if s[0] in v else 0
    for i in range(len(s) - 1):
        vc = vc + 1 if s[i+1] in v else vc
        if s[i] == s[i+1]:
            d = True
        if s[i:i+2] in f:
            return False                
    return True if vc >= 3 and d else False

def is_nice_2(s: str) -> bool:
    f = False
    for i in range(2, len(s)):
        if s[i] == s[i-2]:
            f = True
    if not f:
        return False
    for i in range(len(s)-2):
        for j in range(i+2,len(s)):
            if s[i:i+2] == s[j:j+2]:
                return True
    return False                

with open("input.txt", "r") as fp:
    data = fp.read().splitlines()
    fp.close()

p1, p2 = 0, 0
for line in data:
    p1 = p1 + 1 if is_nice_1(line) else p1 + 0
    p2 = p2 + 1 if is_nice_2(line) else p2 + 0

print("aoc2015d05p01:", p1)
print("aoc2015d05p02:", p2)

