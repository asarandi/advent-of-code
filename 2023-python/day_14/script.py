#!/usr/bin/env pypy3
def tilt(dish: tuple, tilt_config: tuple) -> tuple:
    y_start, y_stop, x_start, x_stop, Y, X = tilt_config
    f, g = 0, list(list(l) for l in dish)
    while not f:
        f = 1
        for y in range(y_start, y_stop + len(dish)):
            for x in range(x_start, x_stop + len(dish[0])):
                if (g[y][x] == "O") and (g[y + Y][x + X] == "."):
                    f, g[y][x], g[y + Y][x + X] = 0, g[y + Y][x + X], g[y][x]
    return tuple(tuple(l) for l in g)


getinput = lambda: tuple(tuple(l) for l in open("input.txt").read().splitlines())
calc = lambda g: sum(g[y].count("O") * (len(g) - y) for y in range(len(g)))
Q = ((1, 0, 0, 0, -1, 0), (0, 0, 1, 0, 0, -1), (0, -1, 0, 0, 1, 0), (0, 0, 0, -1, 0, 1))

dish, seen, mark = getinput(), dict(), -1
for i in range(256):
    for tilt_config in Q:
        dish = tilt(dish, tilt_config)
    s = f"{dish}"
    seen[s] = seen[s] + 1 if s in seen else 1
    if s in seen and seen[s] > 2 and mark == -1:
        seq = {k: v for k, v in seen.items() if v > 1}
        mark = (10**9 - i - 1) % len(seq) + i
    elif i == mark:
        break
print(calc(tilt(getinput(), Q[0])), calc(dish))
