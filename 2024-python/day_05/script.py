#!/usr/bin/env python3

rules, pages = open("input").read().split("\n\n")
dual, multi = {}, {}
for rule in rules.splitlines():
    lo, hi = rule.split("|")
    for key in (lo, hi):
        if key not in multi:
            multi[key] = {}
    multi[lo][hi] = True
    dual[(lo, hi)], dual[(hi, lo)] = True, False


def is_correct(page) -> bool:
    for i in range(1, len(page)):
        key = (page[i - 1], page[i])
        if (key not in dual) or (dual[key] == False):
            return False
    return True


a, b = 0, 0
for page in pages.splitlines():
    page = page.split(",")
    if is_correct(page):
        a += int(page[len(page) // 2])
        continue
    rev = {tuple(set(multi[n]) & set(page)): n for n in page}
    arr = sorted(rev.keys(), key=lambda t: len(t), reverse=True)
    page = [rev[t] for t in arr]
    assert is_correct(page)
    b += int(page[len(page) // 2])

print(a, b)
