#!/usr/bin/env pypy3

checksum = lambda arr: "".join(["." if b else str(i) for (b, i) in arr])


def get_input(f: str) -> [tuple]:
    arr = []
    for i, v in enumerate(map(lambda i: int(i), list(open(f).read().strip()))):
        for _ in range(v):
            arr.append((i % 2, i // 2))
    return arr


def get_tail(arr: [tuple], index: int, part_one: bool):
    end, start = None, None
    for i in range(index, -1, -1):
        f, val = arr[i]
        end = i if (end is None) and (not f) else end
        start = i if end and val == arr[end][1] else start
        if start and end and (val != arr[end][1] or part_one):
            return (start, end + 1)
    return (-1, -1)


def get_head(arr: [tuple], size: int):
    end, start = None, None
    for i in range(len(arr)):
        f, _ = arr[i]
        start = i if start is None and f else start
        start = None if start and (not f) and (end is None) else start
        end = i if start and f and (i - start + 1) == size else end
        if start and end:
            return (start, end + 1)
    return (-1, -1)


def run(filename: str, part_one: bool) -> int:
    arr = get_input(filename)
    end = len(arr) - 1
    while True:
        (i, j) = get_tail(arr, end, part_one)
        if i == -1:
            break
        (m, n) = get_head(arr, j - i)
        if (m == -1) or (m > i):
            end = i - 1
            continue
        tail = arr[i:j]
        arr = arr[:i] + [(1, 0)] * (j - i) + arr[j:]
        arr = arr[:m] + tail + arr[n:]
    return sum([i * v for i, (b, v) in enumerate(arr) if not b])


print(run("input", 1), run("input", 0))
