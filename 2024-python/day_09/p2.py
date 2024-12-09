#!/usr/bin/env pypy3

import itertools

f = "input"
data = list(map(lambda i: int(i), list(open(f).read().strip())))
arr = []
c = itertools.count()
for i, v in enumerate(data):
    for _ in range(v):
        # id, even/odd, original index, value
        arr.append((next(c), 0 if i % 2 == 0 else 1, i // 2, v))

#print(arr)
n = len(arr)

def get_tail(index: int):
#    print("get_tail", index)
    end, start = None, None
    for i in range(index,-1,-1):
        _, is_odd, val, _ = arr[i]
        end = i if (end is None) and (not is_odd) else end
        start = i if end and val == arr[end][2] else start
        if start and end and val != arr[end][2]:
            return (start, end)
    return None        


def get_head(index: int, k: int):
#    print("get_head", index, k)
    end, start = None, None
    for i in range(len(arr)):
        _, is_odd, _, _ = arr[i]
        start = i if start is None and is_odd else start
        start = None if start and (not is_odd) and (end is None) else start
        end = i if start and is_odd and (i-start+1) == k else end
        if start and end:
#            print("get_head", start, end, i)
            return (start, end)
    return None        

h, t = 0, n - 1

def checksum():
    s = ""
    for v in arr:
        id_, is_odd, index, val = v
        s += "." if is_odd else str(index)
    return s        

#print("arr", checksum())
while True:
    v = get_tail(t)
#    print("tail",v)
    if not v:
        break
    t0, t1 = v
#    print("tail", arr[t0:t1+1])
    k = t1 - t0 + 1    
    v = get_head(0, k)
#    print("head",v)
    if not v:
        t = t0 - 1
        continue
#        break
#    t = len(arr) - 1
    h0, h1 = v
    if h0 > t0:
        t = t0 - 1
        continue
    arr, tail = arr[:t0] + [(0,1,0,0)] * (t1-t0+1) +  arr[t1 + 1:], arr[t0:t1 + 1]
    arr = arr[:h0] + tail + arr[h1 + 1:]
#    t = len(arr) - 1
#    print("arr", arr)
#    print("arr", checksum())


res = 0
for i, v in enumerate(arr):
    _, is_odd, index, _ = v
    if is_odd: continue
    res += i * index
print(res)
