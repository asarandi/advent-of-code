#!/usr/bin/env python3

import json

# http://www.njohnston.ca/2010/10/a-derivation-of-conways-degree-71-look-and-say-polynomial/
with open("data.json") as fp:
    j = json.load(fp)
    fp.close()


def calc(current_seq: {}, n: int) -> int:
    for i in range(n):
        new_seq = {}
        for k in current_seq:
            for t in j["evolves_into"][k]:
                if t not in new_seq:
                    new_seq[t] = 0
                new_seq[t] += current_seq[k]
        current_seq = new_seq
    res = 0
    for k in current_seq:
        res += j["length"][k] * current_seq[k]
    return res


puzzle = "1113122113"  # aoc puzzle input
d = {j["subsequence"].index(puzzle): 1}
print("aoc2015d10p01:", calc(d, 40))
print("aoc2015d10p02:", calc(d, 50))
