#!/usr/bin/env python3


def run(part_one):
    ct = 0
    data = open("input").read().splitlines()
    for l in map(lambda l: [int(i) for i in l.split()], data):
        for l in [l] + [l[:i] + l[i + 1 :] for i in range(len(l))]:
            inc, safe = l[0] < l[1], True
            for i in range(1, len(l)):
                safe &= l[i - 1] < l[i] if inc else l[i - 1] > l[i]
                safe &= 1 <= abs(l[i - 1] - l[i]) <= 3
            ct += 1 if safe else 0
            if safe or part_one:
                break
    return ct


print(run(True), run(False))
