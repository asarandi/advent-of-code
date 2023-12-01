#!/usr/bin/env python3

import functools


def search(arr: [int], n: int, s: int) -> [tuple]:
    res = []

    def dfs(tab: [int] = [], i: int = -1) -> None:
        if len(tab) == n:
            if sum(tab) == s:
                res.append(tuple(tab))
        else:
            for j in range(i + 1, len(arr)):
                dfs(tab + [arr[j]], j)

    dfs()
    return res


def min_product(arr: [tuple]) -> int:
    return min(map(lambda t: functools.reduce(lambda x, y: x * y, t), arr))


with open("input.txt") as fp:
    nums = [int(i) for i in fp.read().splitlines()]
    fp.close()

print("part 1:", min_product(search(nums, 6, sum(nums) // 3)))
print("part 2:", min_product(search(nums, 5, sum(nums) // 4)))
