#!/usr/bin/env node

"use strict";
import { readFileSync } from "fs";
const chr = String.fromCharCode;

let s = readFileSync("input.txt", "utf-8").trim();

const reaction = (s) => {
  let done = false;

  while (!done) {
    done = true;
    for (let i = 1; i < s.length; i++) {
      if (s.charCodeAt(i) === (s.charCodeAt(i - 1) ^ 32)) {
        s = s.slice(0, i - 1) + s.slice(i + 1);
        i = Math.max(1, i - 4);
        done = false;
      }
    }
  }
  return s;
};

const search = (input) => {
  let r = Infinity;

  for (let c = 65; c < 91; c++) {
    let s = input;
    s = s.replace(new RegExp(chr(c), "g"), "");
    s = s.replace(new RegExp(chr(c ^ 32), "g"), "");
    s = reaction(s);
    r = s.length < r ? s.length : r;
  }
  return r;
};

const r = reaction(s);
console.log(r.length);
console.log(search(s));
