#!/usr/bin/env python3

import functools


def search(arr: [int], n: int, s: int) -> [tuple]:
    res = set()
    used = [False for _ in range(len(arr))]

    def dfs(tab: [int] = []) -> None:
        if len(tab) == n:
            if sum(tab) == s:
                res.add(tuple(sorted(tab)))
        else:
            for i in range(len(arr)):
                if used[i] == False:
                    used[i] = True
                    dfs(tab + [arr[i]])
                    used[i] = False

    dfs()
    return list(res)


def min_product(arr: [int]) -> int:
    res = functools.reduce(lambda x, y: x * y, list(arr[0]))
    for t in arr:
        p = functools.reduce(lambda x, y: x * y, list(t))
        res = p if p < res else res
    return res


N = 2; M = 2; nums = [1, 2, 3, 4, 5, 7, 8, 9, 10, 11]

#N = 6; M = 5; nums = [1,3,5,11,13,17,19,23,29,31,37,41,43,47,53,59,67,71,73,79,83,89,97,101,103,107,109,113]

res = search(nums, N, sum(nums) // 3)
print("part 1:", min_product(res))

res = search(nums, M, sum(nums) // 4)
print("part 2:", min_product(res))
