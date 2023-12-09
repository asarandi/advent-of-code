#!/usr/bin/env python3


def process(arr: [int], part2: bool) -> int:
    history = [arr]
    while not all(list(map(lambda i: i == 0, arr))):
        arr = [arr[i] - arr[i - 1] for i in range(1, len(arr))]
        history.append(arr)

    ret = 0
    for i in range(len(history) - 1, -1, -1):
        ret = history[i][0] - ret if part2 else history[i][-1] + ret
    return ret


l = [[int(i) for i in s.split()] for s in open("input.txt").read().splitlines()]
print(sum(map(lambda a: process(a, 0), l)), sum(map(lambda a: process(a, 1), l)))
