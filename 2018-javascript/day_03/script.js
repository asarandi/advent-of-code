#!/usr/bin/env node

"use strict";
import { readFileSync } from "fs";

const arr = readFileSync("input.txt", "utf-8")
  .trim()
  .split("\n")
  .map((s) => s.match(/(\d+)/g))
  .map((a) => a.map((i) => parseInt(i)))
  .map((a) => Object({ id: a[0], x: a[1], y: a[2], w: a[3], h: a[4] }));

const ct = {};

for (const o of arr) {
  for (let y = o.y; y < o.y + o.h; y++) {
    for (let x = o.x; x < o.x + o.w; x++) {
      const key = `${y},${x}`;
      ct[key] = key in ct ? ct[key] + 1 : 1;
    }
  }
}

console.log(
  Object.values(ct)
    .map((v) => v > 1)
    .reduce((a, c) => a + c),
);

myLabel: for (const o of arr) {
  for (let y = o.y; y < o.y + o.h; y++) {
    for (let x = o.x; x < o.x + o.w; x++) {
      const key = `${y},${x}`;
      if (ct[key] > 1) continue myLabel;
    }
  }
  console.log(o.id);
  break;
}
