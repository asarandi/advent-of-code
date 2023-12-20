#!/usr/bin/env pypy3

import math

L = open("input.txt").read().splitlines()
types, inputs, outputs = {}, {}, {}
for l in L:
    l, r = l.split(" -> ")
    type_, name = l[:1], l[1:]
    types[name] = type_
    lout = r.split(", ")
    outputs[name] = tuple(lout)
    for n in [name] + lout:
        inputs[n] = []

for k, v in outputs.items():
    for vv in v:
        inputs[vv].append(k)

inputs = {k: tuple(v) for (k, v) in inputs.items()}


def sim(part2: bool) -> int:
    state, counts = {}, {1: 0, 0: 0}
    for k, v in types.items():
        if v == "%":
            state[k] = 0
        elif v == "&":
            state[k] = [0] * len(inputs[k])

    cycles = {k: 0 for k in inputs[inputs["rx"][0]]}

    for i in range(10000 if part2 else 1000):
        queue = [("button", "roadcaster", 0)]
        while queue:
            node = queue.pop(0)
            src, dst, value = node
            counts[value] += 1

            for cy in cycles:
                if i > 0 and cycles[cy] == 0:
                    if not any(state[cy]):
                        cycles[cy] = i + 1
                        if all(cycles.values()):
                            return math.lcm(*cycles.values())

            if dst in ("output", "rx"):
                continue

            if types[dst] == "b":
                for n in outputs[dst]:
                    queue.append((dst, n, value))

            elif types[dst] == "%":
                if value == 1:
                    continue
                state[dst] ^= 1
                for n in outputs[dst]:
                    queue.append((dst, n, state[dst]))

            elif types[dst] == "&":
                state[dst][inputs[dst].index(src)] = value
                out = all(state[dst]) ^ 1
                for n in outputs[dst]:
                    queue.append((dst, n, out))
            else:
                assert 0, dst

    return counts[0] * counts[1]


print(sim(0), sim(1))
