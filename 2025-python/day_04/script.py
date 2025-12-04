#!/usr/bin/env python3


def get_input(filename: str) -> dict:
    lines = open(filename).read().splitlines()
    h, w = len(lines), len(lines[0])
    return {(y, x): True for y in range(h) for x in range(w) if lines[y][x] == "@"}


def count_adjacent(grid: dict, yx: tuple) -> int:
    adjacent = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    add_tuples = lambda a, b: tuple(map(sum, zip(a, b)))
    return sum([1 if add_tuples(adj, yx) in grid else 0 for adj in adjacent])


def simulate_updates(grid: dict, ct: int = 0) -> int:
    grid_copy = grid.copy()

    ct_prev = ct
    for key in grid.keys():
        if count_adjacent(grid, key) < 4:
            del grid_copy[key]
            ct += 1

    return ct if ct == ct_prev else simulate_updates(grid_copy, ct)


def main():
    grid = get_input("input")

    part_1 = sum([1 if count_adjacent(grid, key) < 4 else 0 for key in grid.keys()])
    part_2 = simulate_updates(grid)

    print(part_1, part_2)


if __name__ == "__main__":
    main()
