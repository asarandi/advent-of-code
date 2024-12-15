#!/usr/bin/env pypy3

import re

G = {}
for l in open("input").read().splitlines():
    px,py,vx,vy = tuple(map(lambda i: int(i), re.findall(r"(-?\d+)", l)))
    key, value = (px,py), (vx, vy)
    if key not in G:
        G[key] = []
    G[key] += [value]        


def display(puzzle: dict):
    for k, v in puzzle.items():
        print(k, v)
    print()        

def count(puzzle: dict) -> int:
    res = 0
    for k, v in puzzle.items():
        res += len(v)
    return res

H, W = 7, 11
H, W = 103, 101
def display_v2(puzzle: dict, t: int):
    print("time-index", t)
    for y in range(H):
        for x in range(W):
            key = (x, y)
            c = str(len(puzzle[key])) if key in puzzle else " "
            print(c, end="")
        print()
    print()
            


add = lambda a, b: ((a[0] + b[0]) % W, (a[1] + b[1]) % H)
in_bounds = lambda a: 0 <= a[0] < H and 0 <= a[1] < W

def has_vertical(puzzle: dict) -> bool:
    X, Y = {}, {}
    for y in range(H):
        for x in range(W):
            key = (x, y)
            if key in puzzle:
                X[x] = X[x] + 1 if x in X else 1
                Y[y] = Y[y] + 1 if y in Y else 1

    for k,v in X.items():
        if v > 33:
            return True
    for k,v in Y.items():
        if v > 33:
            return True
    return False        




#def add(a, b) -> tuple:
#    (ax,ay), (bx,by) = a, b
#    ax, ay = ax+bx, ay+by
#    ay = ay - H if ay > H else ay + H if ay < 0 else ay
#    ax = ax - W if ax > W else ax + W if ax < 0 else ax
#    return ax, ay


def transform(puzzle: dict) -> dict:
    res = dict()    
    for k, v in puzzle.items():
        for vv in v:
            kk = add(k, vv)
            if kk not in res:
                res[kk] = []
            res[kk] += [vv]
    for k in puzzle.keys():
        puzzle[k].sort()                
    return res            

def calc_quadrants(puzzle: dict) -> int:
    arr = [0, 0, 0, 0]
    for y in range(H):
        for x in range(W):
            key = (x, y)
            if (key not in puzzle) or (y == H // 2) or (x == W // 2):
                continue
            v1 = 0 if (y < (H // 2)) else 1
            v2 = 0 if (x < (W // 2)) else 1
            index = v1 * 2 + v2
            arr[index] += len(puzzle[key])
    import functools
    return functools.reduce(lambda a,b : a * b, arr)

for t in range(10613):

    if has_vertical(G):
        print("has_vertical", t)
        display_v2(G, t)
    m = count(G.copy())    
    G = transform(G.copy())
    n = count(G.copy())    
    assert m == n
    if t == 99:
        print(calc_quadrants(G))


            
