#!/usr/bin/env python3

puzzle = 29000000

# highly composite numbers: https://oeis.org/A002182
hcn = [
    1,
    2,
    4,
    6,
    12,
    24,
    36,
    48,
    60,
    120,
    180,
    240,
    360,
    720,
    840,
    1260,
    1680,
    2520,
    5040,
    7560,
    10080,
    15120,
    20160,
    25200,
    27720,
    45360,
    50400,
    55440,
    83160,
    110880,
    166320,
    221760,
    277200,
    332640,
    498960,
    554400,
    665280,
    720720,
    1081080,
    1441440,
    2162160,
]

for n in hcn:
    k = 0
    for i in range(n, 0, -1):
        if n % i == 0:
            k += i * 10
    if k >= puzzle:
        print("aoc2015d20p01:", n)
        break

n = 1
while True:
    k = sum(map(lambda i: n // i * 11, filter(lambda j: n % j == 0, range(1, 51))))
    if k >= puzzle:
        print("aoc2015d20p02:", n)
        break
    n += 1
