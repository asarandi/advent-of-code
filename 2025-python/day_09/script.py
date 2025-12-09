#!/usr/bin/env python3

from shapely.geometry import Polygon


def get_area(a, b):
    h = abs(a[0] - b[0])
    w = abs(a[1] - b[1])
    return (h + 1) * (w + 1)


def get_rectangle(a, b):
    ay, ax = a
    by, bx = b
    ly, hy = min(ay, by), max(ay, by)
    lx, hx = min(ax, bx), max(ax, bx)
    return [(ly, lx), (hy, lx), (hy, hx), (ly, hx)]


lines = open("input").read().splitlines()
coords = [tuple(map(int, l.split(","))) for l in lines]

parent = Polygon(coords)

p1, p2 = 0, 0
for a in coords:
    for b in coords:
        if a > b:
            area = get_area(a, b)
            p1 = max(p1, area)
            ch = Polygon(get_rectangle(a, b))
            if parent.contains(ch):
                p2 = max(p2, area)
print(p1, p2)
