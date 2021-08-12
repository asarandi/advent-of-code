#!/usr/bin/env python3

with open("input.txt", "r") as fp:
    data = fp.read().splitlines()
    fp.close()

reindeer = {}
for line in data:
    words = line.split(" ")
    name, speed, fly, rest = words[0], int(words[3]), int(words[6]), int(words[13])
    reindeer[name] = {"speed": speed, "fly": fly, "rest": rest}

rl = list(reindeer)

p1 = [0] * len(reindeer)
p2 = [0] * len(reindeer)

for t in range(2503):
    for i in range(len(reindeer)):
        r = rl[i]
        c = reindeer[r]["fly"] + reindeer[r]["rest"]
        k = t % c
        if k < reindeer[r]["fly"]:
            p1[i] += reindeer[r]["speed"]
    m = max(p1)
    for i in range(len(reindeer)):
        if p1[i] == m:
            p2[i] += 1

print("aoc2015d14p01:", max(p1))
print("aoc2015d14p02:", max(p2))
