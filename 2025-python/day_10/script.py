#!/usr/bin/env python3

import re
from heapq import heappush, heappop


def get_p1(a: int, b: list) -> int:
    k = len(b)
    m = n = 2**k
    for i in range(1, n):
        v = 0
        for j in range(k):
            if i & (1 << j):
                v ^= b[j]
        if v == a:
            j, c = i, 0
            while j:
                j &= j - 1
                c += 1
            m = min(m, c)
    return m


def heuristic(a: tuple, b: tuple) -> int:
    assert len(a) == len(b)
    return max([abs(a[i] - b[i]) for i in range(len(a))])


def search_p2(a: int, b: list, goal: tuple) -> int:
    n = len(goal)
    initial_state = tuple([0] * n)
    depth, score = 0, heuristic(initial_state, goal)
    queue = [(depth + score, depth, score, initial_state)]
    while queue:
        (f, g, h, parent) = heappop(queue)
        if parent == goal:
            return g
        for v in b:
            ch = list(parent)
            for i in range(n):
                if v & (1 << i):
                    ch[i] += 1
            node = tuple(ch)
            node_h = heuristic(node, goal)
            queue.append((g + 1 + node_h, g + 1, node_h, node))
    assert False


make_int = lambda s: sum(map(lambda a: 2 ** int(a), re.findall(r"\d", s)))

p1, p2 = 0, 0
for l in open("input").read().splitlines():
    a, b, c = re.findall(r"^\[(.*)\]\s(.*)\s{(.*)}", l).pop()
    a = int(a.replace(".", "0").replace("#", "1")[::-1], base=2)
    b = [make_int(s) for s in b.split()]
    c = tuple(map(int, c.split(",")))
    p1 += get_p1(a, b)

    # naive: takes 1 minute to solve sample
    # will try z3 approach tomorrow
    p2 += search_p2(a, b, c)
print(p1, p2)
