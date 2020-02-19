#!/usr/bin/env python3

from hashlib import md5

s = 'ckczppom'      # puzzle input
i, f = 1, 0

while True:
    if not f and md5(bytes(s + str(i), 'utf8')).hexdigest()[:5] == "00000":
        print("aoc2015d04p01:", i)
        f = 1
    if f and md5(bytes(s + str(i), 'utf8')).hexdigest()[:6] == "000000":
        print("aoc2015d04p02:", i)
        break
    i += 1        

