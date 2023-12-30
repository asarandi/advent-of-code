#!/usr/bin/env pypy3

import itertools, copy

ULRD = [(-1, 0), (0, -1), (0, 1), (1, 0)]
sym = lambda g, t: g[t[0]][t[1]]
tuple_add = lambda a, b: (a[0] + b[0], a[1] + b[1])
is_within = lambda g, a: (0 <= a[0] < len(g)) and (0 <= a[1] < len(g[0]))
distance = lambda a, b: abs(a[0] - b[0]) + abs(a[1] - b[1])
adjacent = lambda a: list(map(lambda b: tuple_add(a, b), ULRD))
grid_order = lambda g: tuple((y, x) for y in range(len(g)) for x in range(len(g[0])))
turn_order = lambda g: tuple(t for t in grid_order(g) if sym(g, t) in "EG")
total_hp = lambda g, m: sum([sym(m, t) for t in turn_order(g)])
is_opponent = lambda g, a, b: sym(g, a) in "GE" and sym(g, b) in "GE" and sym(g, a) != sym(g, b)
get_input = lambda f: [list(l.strip()) for l in open(f).read().splitlines()]
num_elves = lambda g: sum([l.count("E") for l in g])
num_goblins = lambda g: sum([l.count("G") for l in g])
num_alive = lambda g: (num_elves(g), num_goblins(g))


def find_path(g: [[str]], src: tuple, dst: tuple) -> [tuple]:
    ct = itertools.count()
    queue = [(src, next(ct))]
    seen = set()
    parent = {}
    while queue:
        node, num = queue.pop(0)
        if node in seen:
            continue
        seen.add(node)

        if node == dst:
            path = []
            while node != src:
                path += [node]
                node, num = parent[(node, num)]
            return path[::-1]

        for step in adjacent(node):
            if not is_within(g, step):
                continue
            if sym(g, step) != ".":
                continue
            new_node = (step, next(ct))
            parent[new_node] = (node, num)
            queue += [new_node]
    return None


def do_attack(g: [[str]], m: [[str]], unit: tuple, attack: dict) -> bool:
    fewest_hp = 201
    target = None
    for adj in adjacent(unit):
        if is_opponent(g, unit, adj):
            ay, ax = adj
            if m[ay][ax] < fewest_hp:
                fewest_hp = m[ay][ax]
                target = adj
    if target:
        ty, tx = target
        m[ty][tx] -= attack[sym(g, unit)]
        if m[ty][tx] <= 0:
            g[ty][tx] = "."
            m[ty][tx] = "."

    return target != None


def do_round(g: [[str]], m: [[str]], attack: dict) -> tuple:
    order = turn_order(g)
    elves, goblins = num_elves(g), num_goblins(g)
    if not elves or not goblins:
        return elves, goblins

    for unit in order:
        if sym(g, unit) not in "GE":
            continue

        if do_attack(g, m, unit, attack):
            continue

        shortest_len = len(g) * len(g[0])
        shortest_path = None
        opponent = None
        for candidate in turn_order(g):
            if is_opponent(g, unit, candidate):
                for adj in adjacent(candidate):
                    if path := find_path(g, unit, adj):
                        if len(path) < shortest_len:
                            shortest_len = len(path)
                            shortest_path = path
                            opponent = candidate
        if opponent:
            uy, ux = unit
            oy, ox = shortest_path.pop(0)
            g[oy][ox], g[uy][ux] = g[uy][ux], g[oy][ox]
            m[oy][ox], m[uy][ux] = m[uy][ux], m[oy][ox]
            do_attack(g, m, (oy, ox), attack)

    return num_elves(g), num_goblins(g)


def play(attack: dict) -> int:
    G = get_input("input.txt")
    M = copy.deepcopy(G)
    for y, x in turn_order(G):
        M[y][x] = 200

    rounds = -1
    while True:
        rounds += 1
        elves, goblins = do_round(G, M, attack)
        if not elves or not goblins:
            break

    return rounds * total_hp(G, M)

print(play({"G": 3, "E": 3}), play({"G": 3, "E": 20}))
