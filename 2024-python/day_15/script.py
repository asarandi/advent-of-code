#!/usr/bin/env python3

f = "input"
grid, moves = open(f).read().split("\n\n")
moves = "".join([l.strip() for l in moves.splitlines()])
grid = [l.strip() for l in grid.splitlines()]
start, G, H, W = None, {}, len(grid), len(grid[0] * 2)


def display(puzzle, height, width, title):
    print(title)
    for y in range(height):
        for x in range(width):
            sym = puzzle[(y, x)]
            print(sym, end="")
        print()


for i, l in enumerate(grid):
    for j, c in enumerate(l):
        if c == "#":
            G[(i, j * 2)], G[(i, j * 2 + 1)] = "#", "#"
        elif c == "O":
            G[(i, j * 2)], G[(i, j * 2 + 1)] = "[", "]"
        elif c == ".":
            G[(i, j * 2)], G[(i, j * 2 + 1)] = ".", "."
        elif c == "@":
            G[(i, j * 2)], G[(i, j * 2 + 1)] = "@", "."
            start = (i, j * 2)

distance = lambda a, b: abs(a[0] - b[0]) + abs(a[1] - b[1])
multiply = lambda a, m: (a[0] * m, a[1] * m)
add = lambda a, b: (a[0] + b[0], a[1] + b[1])
URDL = {"^": (-1, 0), ">": (0, 1), "v": (1, 0), "<": (0, -1)}


def get_dependencies(puzzle, start, move_sym) -> (bool, set):
    queue, seen, step = [start], set(), URDL[move_sym]
    while queue:
        node = queue.pop(0)
        seen.add(node)
        new_node = add(node, step)
        if new_node not in puzzle:
            return False, set()
        if puzzle[new_node] not in (".", "[", "]"):
            return False, set()
        if puzzle[new_node] == ".":
            continue

        queue.append(new_node)

        if move_sym == "<" and puzzle[new_node] == "]":
            queue.append(add(new_node, step))
        elif move_sym == ">" and puzzle[new_node] == "[":
            queue.append(add(new_node, step))

        if move_sym in ("^", "v"):
            if puzzle[new_node] == "]":
                queue.append(add(new_node, URDL["<"]))
            if puzzle[new_node] == "[":
                queue.append(add(new_node, URDL[">"]))

    return True, seen


prev = "?"
for index, move in enumerate(moves):
    #    display(G, H, W, prev)
    prev = f"{index}, {move}"
    ok, deps = get_dependencies(G, start, move)
    if not ok:
        continue
    new_puzzle = G.copy()
    step = URDL[move]
    for _, pt in sorted([(distance(pt, start), pt) for pt in deps], reverse=True):
        new_puzzle[add(pt, step)], new_puzzle[pt] = G[pt], "."
    new_puzzle[start] = "."
    start = add(start, step)
    G = new_puzzle


display(G, H, W, "fin")


res = sum([y * 100 + x for y in range(H) for x in range(W) if G[(y, x)] == "["])
print(res)
