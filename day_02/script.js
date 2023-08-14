#!/usr/bin/env node

"use strict";

import { readFileSync } from "fs";

const arr = readFileSync("input.txt", "utf-8").trim().split("\n");

const hasRepeatCount = (s, t) => {
  const o = {};
  for (const c of s) {
    o[c] = c in o ? o[c] + 1 : 1;
  }

  for (const k in o) {
    if (o[k] === t) {
      return true;
    }
  }
  return false;
};

let doubles = 0;
let triples = 0;
for (const s of arr) {
  doubles += hasRepeatCount(s, 2) ? 1 : 0;
  triples += hasRepeatCount(s, 3) ? 1 : 0;
}
console.log(doubles * triples);

const sharedSubstring = (s1, s2) => {
  let s = "";
  for (let i = 0; i < s1.length; i++) {
    s += s1[i] === s2[i] ? s1[i] : "";
  }
  return s;
};

myLabel: for (const s1 of arr) {
  for (const s2 of arr) {
    const s = sharedSubstring(s1, s2);
    if (s.length + 1 === s1.length) {
      console.log(s);
      break myLabel;
    }
  }
}
