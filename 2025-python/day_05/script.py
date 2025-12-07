#!/usr/bin/env python3


def get_input(filename: str) -> ([list], [int]):
    input1, input2 = open(filename).read().split("\n\n")
    intervals = [list(map(int, l.split("-"))) for l in input1.splitlines()]
    ingredients = [int(i) for i in input2.splitlines()]
    return intervals, ingredients


def merge(intervals: [list]) -> [list]:
    intervals.sort(key=lambda x: x[0])
    merged = [intervals.pop(0)]
    for i in range(len(intervals)):
        if intervals[i][0] <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], intervals[i][1])
        else:
            merged.append(intervals[i])
    return merged


def main():
    intervals, ingredients = get_input("input")
    p1 = sum([any([r[0] <= i <= r[1] for r in intervals]) for i in ingredients])
    p2 = sum([r[1] - r[0] + 1 for r in merge(intervals)])
    print(p1, p2)


if __name__ == "__main__":
    main()
