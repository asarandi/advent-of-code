#!/usr/bin/env python3

import re, copy


def get_input(f: str) -> dict:
    nodes = dict()
    for l in open(f).read().splitlines():
        l, *r = re.findall(r"(\w+)", l)
        nodes[l] = nodes[l] + r if l in nodes else r
        for rr in r:
            nodes[rr] = nodes[rr] + [l] if rr in nodes else [l]
    return nodes


def get_vertices(g: dict) -> set:
    res = []
    for k, v in g.items():
        res = res + [k] + v
    return set(res)


def cut_wire(nodes: dict, ab: tuple) -> dict:
    new_nodes = copy.deepcopy(nodes)
    a, b = ab
    if a in nodes and b in nodes[a]:
        new_nodes[a].remove(b)
    if b in nodes and a in nodes[b]:
        new_nodes[b].remove(a)
    return new_nodes


def find_graph_sizes(g: dict, start: str) -> tuple[int, int]:
    queue, seen = [start], set()
    while queue:
        k = queue.pop(0)
        if k in seen:
            continue
        seen.add(k)
        queue += g[k]
    return len(seen), len(get_vertices(g) ^ seen)


g = get_input("input.txt")

# import graphviz
#
# dot = graphviz.Graph()
# for k, v in g.items():
#     dot.node(k)
#     for vv in v:
#         dot.node(vv)
#         dot.edge(k, vv)
# print(dot.source)
#
# # render: sfdp -x -Goverlap=scale -Tsvg data.dot > data.svg
# # find responsible vertices: jxx-qdp, vsx-zbr, qqq-mlp

g = cut_wire(cut_wire(cut_wire(g, ("jxx", "qdp")), ("vsx", "zbr")), ("qqq", "mlp"))
i, j = find_graph_sizes(g, "qqq")
res = i * j
assert res == 543256
print(res)
