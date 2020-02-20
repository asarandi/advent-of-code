#!/usr/bin/env python3

with open("input.txt", "r") as fp:
    data = fp.read().splitlines()
    fp.close()

def emulate(lst: [], dbv=None) -> int:
    # dbv = default 'b' value
    d = {}
    while lst:
        new_lst = []
        for i in range(len(lst)):
            line = lst[i]
            src, dst = line.split(' -> ')[0], line.split(' -> ')[1]
            src = src.split(' ')
            if len(src) == 1:
                if src[0].isnumeric():
                    if dst == 'b' and dst not in d and dbv:
                        d[dst] = dbv
                    else:                        
                        d[dst] = int(src[0])
                else:
                    if src[0] in d:
                        d[dst] = d[src[0]]
                    else:
                        new_lst.append(lst[i])
                        continue
            elif len(src) == 2:   # only NOT
                if src[1] in d:
                    d[dst] = ~ d[src[1]]
                else:
                    new_lst.append(lst[i])
                    continue
            else:
                if src[0].isnumeric():
                    a = int(src[0])
                else:
                    if src[0] in d:
                        a = d[src[0]]
                    else:
                        new_lst.append(lst[i])
                        continue
                if src[2].isnumeric():
                    b = int(src[2])
                else:
                    if src[2] in d:
                        b = d[src[2]]
                    else:
                        new_lst.append(lst[i])
                        continue
                if src[1] == 'OR':
                    d[dst] = a | b
                elif src[1] == 'XOR':
                    d[dst] = a ^ b
                elif src[1] == 'LSHIFT':
                    d[dst] = a << b
                elif src[1] == 'RSHIFT':
                    d[dst] = a >> b
                elif src[1] == 'AND':
                    d[dst] = a & b
        lst = new_lst               
    return d['a']

p1 = emulate(data)
p2 = emulate(data, p1)
print("aoc2015d07p01:", p1)
print("aoc2015d07p02:", p2) 
