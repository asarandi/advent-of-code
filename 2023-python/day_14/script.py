#!/usr/bin/env pypy3

G = [list(l) for l in open("input.txt").read().splitlines()]
H, W = len(G), len(G[0])

tab = [
    (1, 0, 0, 0, -1, 0),
    (0, 0, 1, 0, 0, -1),
    (0, -1, 0, 0, 1, 0),
    (0, 0, 0, -1, 0, 1),
]


def roll(G: [list], config: tuple):
    h0, hm, w0, wm, ym, xm = config
    done = False
    while not done:
        done = True
        for y in range(h0, H + hm):
            for x in range(w0, W + wm):
                if (G[y][x] == "O") and (G[y + ym][x + xm] == "."):
                    G[y][x], G[y + ym][x + xm] = G[y + ym][x + xm], G[y][x]
                    done = False
    return G


def calc(G: [list]) -> int:
    r = 0
    for y in range(H):
        for x in range(W):
            if G[y][x] == "O":
                r += H - y
    return r


G = roll(G, tab[0])
print(calc(G))  # part 1

from hashlib import md5

seen = set()
for i in range(512):
    for t in tab:
        G = roll(G, t)
    s = "".join(["".join(l) for l in G])
    h = md5()
    h.update(s.encode())
    d = h.hexdigest()
    print(i, d, calc(G), "---" if d in seen else "")
    seen.add(d)
