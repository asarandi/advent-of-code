#!/usr/bin/env pypy3

import itertools

f = "sample"
data = list(map(lambda i: int(i), list(open(f).read().strip())))
data_ids = []
c = itertools.count()
for i, v in enumerate(data):
    for _ in range(v):
        # id, even/odd, original index, value
        data_ids.append((next(c), 0 if i % 2 == 0 else 1, i // 2, v))

arr = data_ids
#print(arr)
while arr:
    val = arr.pop(-1)
    id_, is_odd, index, value = val
    if is_odd:
#        print("pop odd", val)
        continue
    found = False
    for j in range(len(arr)):
        if arr[j][1] == 1:
            found = True
#            print("j", j, "arr", arr)
            arr[j] = val
            break
    if not found:
        arr.append(val)
        break

print(arr)
print("".join(map(lambda v: str(v[2]), arr)))
res = 0
for i, v in enumerate(arr):
    id_, is_odd, index, value = v
    if is_odd:
        continue
    res += i * index
print(res)    


    



"""
[(0, 0, 0, 1), (1, 1, 1, 2), (2, 1, 1, 2), (3, 0, 2, 3), (4, 0, 2, 3), (5, 0, 2, 3), (6, 1, 3, 4), (7, 1, 3, 4), (8, 1, 3, 4), (9, 1, 3, 4), (10, 0, 4, 5), (11, 0, 4, 5), (12, 0, 4, 5), (13, 0, 4, 5), (14, 0, 4, 5)]
"""

#print(data)
#print(data_ids)
