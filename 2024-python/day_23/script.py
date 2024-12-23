#!/usr/bin/env pypy3

import itertools, functools

g, items = {}, set()
for l in open("input").read().splitlines():
    l, r = l.split("-")
    g[l] = g[l] + [r] if l in g else [r]
    g[r] = g[r] + [l] if r in g else [l]
    items.add(l)
    items.add(r)

seen = set()
intersect = lambda a, b: set(a) & set(b)
for a, b, c in itertools.permutations(items, 3):
    if any(map(lambda t: t.startswith("t"), (a, b, c))):
        if b in g[a] and c in g[a]:
            if a in g[b] and c in g[b]:
                if a in g[c] and b in g[c]:
                    seen.add(tuple(sorted([a, b, c])))
print(len(seen))

ct = {}
for k, v in g.items():
    l = sorted([k] + v)
    for item in l[1:]:
        n = len(intersect(g[item], v))
        ct[k] = ct[k] + n if k in ct else n

items = []
(kk, vv) = {k: v for k, v in ct.items() if v == max(ct.values())}.popitem()
for k, v in {k: v for k, v in g.items() if kk in v}.items():
    items.append(tuple(sorted([k] + v)))

ct = {}
for a, b in itertools.permutations(items, 2):
    if len(intersect(a, b)) < len(a) // 2:
        ct[a] = ct[a] + 1 if a in ct else 1
        ct[b] = ct[b] + 1 if b in ct else 1

(kk, vv) = {k: v for k, v in ct.items() if v == max(ct.values())}.popitem()
res = functools.reduce(intersect, [i for i in items if i != kk])
print(",".join(sorted(res)))
