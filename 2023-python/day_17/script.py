#!/usr/bin/env pypy3

import functools, heapq

G = open("input.txt").read().splitlines()
H, W = len(G), len(G[0])
U, R, D, L = (-1, 0), (0, 1), (1, 0), (0, -1)


@functools.cache
def history_add(h: tuple, move: tuple, hi: int) -> tuple:
    return tuple([move] + list(h))[:hi]


@functools.cache
def allowed_moves(h: tuple, lo: int, hi: int) -> set:
    reverse = {U: (D,), D: (U,), L: (R,), R: (L,)}
    sides = {U: (L, R), R: (U, D), D: (L, R), L: (U, D)}

    r = set((U, R, D, L))
    r ^= set(reverse[h[0]]) if len(h) > 0 else set()
    r ^= set(sides[h[0]]) if len(set(h[:lo])) > 1 else set()
    r ^= set(h[:1]) if hi <= len(h) and len(set(h[:hi])) == 1 else set()
    return r


def search(lo: int, hi: int) -> int:
    start, stop = (0, 0), (H - 1, W - 1)
    queue, seen = [(0, start, ())], set()
    while queue:
        node = heapq.heappop(queue)
        score, pos, history = node
        if pos == stop:
            if len(set(history[:lo])) != 1:
                continue
            return score

        point = pos, history
        if point in seen:
            continue
        seen.add(point)

        for move in allowed_moves(history, lo, hi):
            dy, dx = move[0] + pos[0], move[1] + pos[1]
            if (dy < 0) or (dx < 0) or (H <= dy) or (W <= dx):
                continue

            new_score = score + int(G[dy][dx])
            new_pos = dy, dx
            new_history = history_add(history, move, hi)

            new_node = new_score, new_pos, new_history
            heapq.heappush(queue, new_node)


# slow: takes 67 seconds on my laptop
print(search(1, 3), search(4, 10))
