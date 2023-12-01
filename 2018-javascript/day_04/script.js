#!/usr/bin/env node

"use strict";
import { readFileSync } from "fs";

const arr = readFileSync("input.txt", "utf-8").trim().split("\n").sort();
const N = arr.length;

const what = (s) => s.slice(19, 24);
const when = (s) => parseInt(s.slice(15, 17));
const who = (s) => parseInt(s.match(/#(\d+)/)[1]);
const sumOf = (arr) => arr.reduce((acc, curr) => acc + curr);
const maxOf = (arr) => Math.max.apply(null, arr);

const ct = {};
let i = 0;

while (i < N) {
  while (what(arr[i + 1]) === "Guard") i++;

  const id = who(arr[i++]);
  ct[id] = id in ct ? ct[id] : {};

  while (i < N && what(arr[i]) === "falls") {
    let j = when(arr[i++]);
    let k = when(arr[i++]);
    for (; j < k; j++) ct[id][j] = j in ct[id] ? ct[id][j] + 1 : 1;
  }
}

let bestGuard = undefined;
let bestSum = 0;
for (const id in ct) {
  const v = sumOf(Object.values(ct[id]));
  if (v > bestSum) {
    bestSum = v;
    bestGuard = id;
  }
}

let bestMinute = undefined;
let bestCount = 0;
for (const [k, v] of Object.entries(ct[bestGuard])) {
  if (v > bestCount) {
    bestCount = v;
    bestMinute = k;
  }
}
console.log("part 1:", bestGuard * bestMinute);

bestGuard = undefined;
bestMinute = undefined;
bestCount = 0;

for (const [guard, stats] of Object.entries(ct)) {
  for (const [minute, count] of Object.entries(stats)) {
    if (count > bestCount) {
      bestCount = count;
      bestMinute = minute;
      bestGuard = guard;
    }
  }
}
console.log("part 2:", bestGuard * bestMinute);
