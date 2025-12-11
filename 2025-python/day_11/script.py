#!/usr/bin/env python3

import functools

graph = dict()
for l in open("input").read().splitlines():
    k, *v = l.replace(":", "").split()
    graph[k] = tuple(v)


@functools.cache
def search(node, p2=0, dac=0, fft=0) -> int:
    dac |= node == "dac"
    fft |= node == "fft"
    if node == "out":
        return int(dac and fft) if p2 else 1
    return sum([search(key, p2, dac, fft) for key in graph[node]])


print(search("you"), search("svr", True))
