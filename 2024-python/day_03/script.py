#!/usr/bin/env python3

import re


def run(f: str, part_one: bool = True, do: bool = True, res: int = 0) -> int:
    for l in open(f).read().splitlines():
        for e in re.compile(r"(mul\(\d+,\d+\)|do\(\)|don't\(\))").findall(l):
            if e.startswith("do"):
                do = {"do()": True, "don't()": False}[e]
            else:
                [a, b] = re.compile(r"(\d+)").findall(e)
                res += int(a) * int(b) if do or part_one else 0
    return res


print(run("input", True), run("input", False))
