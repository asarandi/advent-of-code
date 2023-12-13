#!/usr/bin/env pypy3


def get_index(rows: [str], is_vertical: bool, skip_config: tuple) -> (int, int):
    _, orientation, _, skip_index = skip_config
    width, index = 0, -1
    for i in range(1, len(rows)):
        if (is_vertical == orientation) and (skip_index == i):
            continue
        if rows[i] == rows[i - 1]:
            for j in range(len(rows)):
                if not (((i + j) < len(rows)) and (0 <= (i - 1 - j))):
                    break
                if not (rows[i + j] == rows[i - 1 - j]):
                    break
                if not (((i + j + 1) == len(rows)) or ((i - 1 - j) == 0)):
                    continue
                if j + 1 > width:
                    width, index = j + 1, i
    return width, index


def check(b: str, skip=(-1, False, -1, -1)) -> int:
    rows = b.splitlines()
    height, width = len(rows), len(rows[0])
    cols = ["".join([rows[y][x] for y in range(height)]) for x in range(width)]
    rw, ri = get_index(rows, False, skip)
    cw, ci = get_index(cols, True, skip)

    if rw > cw:
        return ri * 100, False, rw, ri
    elif cw > rw:
        return ci, True, cw, ci
    else:
        return 0, 0, 0, 0


def search(b: str) -> int:
    best = 0
    config = check(b)
    for k, v in {"#": ".", ".": "#"}.items():
        index = 0
        while (r := b.find(k, index)) != -1:
            s = b[:r] + v + b[r + 1 :]
            cfg = check(s, config)
            if cfg[0] > best:
                best = cfg[0]
            index = r + 1

    assert best != 0
    return best


p1, p2 = 0, 0
for b in open("input.txt").read().split("\n\n"):
    n, *_ = check(b)
    p1 += n
    p2 += search(b)

print(p1, p2)
assert p1 == 37975 and p2 == 32497
