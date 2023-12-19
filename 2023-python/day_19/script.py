#!/usr/bin/env pypy3

import re

workflows, ratings = open("input.txt").read().split("\n\n")
for k, v in ({"=": ":"} | {k: f'"{k}"' for k in "xmas"}).items():
    ratings = ratings.replace(k, v)
workflows, ratings = workflows.splitlines(), ratings.splitlines()
ratings = list(map(lambda s: eval(s), ratings))
flows, pat = {}, r"(\w)([<>])(\d+):(\w+)"
for l in workflows:
    k, v = re.match(r"(\w+){(.*)}", l).groups()
    flows[k] = v


def process(r: dict, w: str) -> int:
    tab = {"A": 1, "R": 0}
    if w in tab:
        return tab[w]
    for s in flows[w].split(","):
        if ":" not in s:
            return process(r, s)
        key, cond, val, res = re.match(pat, s).groups()
        if cond == ">" and r[key] > int(val):
            return process(r, res)
        elif cond == "<" and r[key] < int(val):
            return process(r, res)
    assert False


print(sum(map(lambda r: process(r, "in") * sum(r.values()), ratings)))


def search(r: dict, w: str, depth: int = 0) -> int:
    #    print("enter", r, w, flows[w] if w in flows else "", "depth", depth)

    if w == "R":
        return 0
    elif w == "A":
        v = 1
        for lo, hi in r.values():
            assert lo < hi
            v *= hi - lo + 1
        #        print("return", v, r.values(), "depth", depth)
        return v

    total = 0
    for s in flows[w].split(","):
        #        print("current", s, "depth", depth)
        if ":" not in s:
            total += search(r, s, depth + 1)
            return total

        key, cond, val, res = re.match(pat, s).groups()
        val = int(val)
        lo, hi = r[key]

        if cond == "<":
            if hi < val:
                total += search(r, res, depth + 1)
            elif lo < val:
                total += search(r | {key: (lo, val - 1)}, res, depth + 1)
                r[key] = (val, hi)
        elif cond == ">":
            if lo > val:
                total += search(r, res, depth + 1)
            elif hi > val:
                total += search(r | {key: (val + 1, hi)}, res, depth + 1)
                r[key] = (lo, val)

    #    print("total", total)
    return total


print(search({k: (1, 4000) for k in "xmas"}, "in", 0))
