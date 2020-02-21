#!/usr/bin/env python3

import json

with open("input.txt", "r") as fp:
    data = json.load(fp)
    fp.close()

def trav(data, ignore_red) -> int:
    res = 0
    if isinstance(data, int):
        return data
    elif isinstance(data, list):
        for e in data:
            res += trav(e, ignore_red)
    elif isinstance(data, dict):
        if ignore_red:
            for e in data:
                if isinstance(data[e], str) and data[e] == "red":
                    return 0
        for e in data:
            res += trav(data[e], ignore_red)
    return res

print("aoc2015d12p01:", trav(data, False))
print("aoc2015d12p02:", trav(data, True))
