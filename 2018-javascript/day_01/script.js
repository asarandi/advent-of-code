#!/usr/bin/env node

"use strict";

import { readFileSync } from "node:fs";

const arr = readFileSync("input.txt", "utf-8")
  .trim()
  .split("\n")
  .map((s) => parseInt(s));

let val = 0;
let p1 = undefined;
let p2 = undefined;
const seen = new Set();

while (p2 === undefined) {
  for (let i = 0; i < arr.length; i++) {
    val += arr[i];
    p2 = seen.has(val) && p2 === undefined ? val : p2;
    seen.add(val);
  }
  p1 = p1 === undefined ? val : p1;
}

console.log(p1, p2);
