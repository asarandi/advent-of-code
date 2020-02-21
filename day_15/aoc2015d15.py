#!/usr/bin/env python3

from math import inf

with open("input.txt", "r") as fp:
    data = fp.read().splitlines()
    fp.close()

ingredients = []
for line in data:
    commas = line.split(',')
    ingredients.append([int(x.split(' ')[-1]) for x in commas])

def calc(quantities: [], ingredients: []) -> (int, bool):
    res = [0] * len(ingredients[0])
    for j in range(len(res)):
        for k in range(len(quantities)):
            res[j] += quantities[k] * ingredients[k][j]
    for j in range(len(res)):
        res[j] = res[j] if res[j] > 0 else 0
    ans = res[0]
    for j in range(1,len(res) - 1): # -1 to exclude calories
        ans *= res[j]
    return ans, res[-1] == 500

p1, p2 = -inf, -inf
def permute(lst: [], idx: int, ingredients: []):
    global p1, p2
    if idx == len(lst):
        k, c = calc(lst, ingredients)
        p1 = k if k > p1 else p1
        p2 = k if c and k > p2 else p2
    else:
        for i in range(idx, len(lst)):
            lst[i], lst[idx] = lst[idx], lst[i]
            permute(lst, idx + 1, ingredients)
            lst[i], lst[idx] = lst[idx], lst[i]

n = 100
for i in range(n):
    for j in range(i, n):
        for k in range(j, n):
            for l in range(k, n + 1):
                if i + j + k + l == n:
                    lst = [i,j,k,l]
                    permute(lst, 0, ingredients)

print("aoc2015d15p01:", p1)
print("aoc2015d15p02:", p2)
