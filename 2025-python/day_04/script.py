#!/usr/bin/env python3


def get_input(filename: str) -> set:
    lines = open(filename).read().splitlines()
    h, w = len(lines), len(lines[0])
    return {(y, x) for y in range(h) for x in range(w) if lines[y][x] == "@"}


def get_adjacent(grid: set, yx: tuple) -> set:
    adjacent = {(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)}
    adjacent = set(map(lambda a: tuple(map(sum, zip(a, yx))), adjacent))
    return grid & adjacent


def simulate_updates(grid: set) -> set:
    removed = {t for t in grid if len(get_adjacent(grid, t)) < 4}
    return grid if not removed else simulate_updates(grid - removed)


def main():
    grid = get_input("input")

    part_1 = sum([1 if len(get_adjacent(grid, t)) < 4 else 0 for t in grid])
    part_2 = len(grid - simulate_updates(grid))

    print(part_1, part_2)


if __name__ == "__main__":
    main()
