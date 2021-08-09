#!/usr/bin/env python3

R, C = 2981, 3075
N, calc = 0, 1

while calc < R + C:
    N += calc
    calc += 1

N = N - (R - 1)

calc = 20151125
for i in range(N - 1):
    calc = (calc * 252533) % 33554393

print("part 1:", calc)
