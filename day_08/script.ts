"use strict";
import { readFileSync } from "node:fs";

const getInput = (f: string): number[] =>
  readFileSync(f, "utf-8")
    .split(/\s+/)
    .map((i) => parseInt(i));

const solve = (arr: number[], index: number, P1: boolean): [number, number] => {
  if (arr.length === index) return [index, 0];

  const n = arr[index++];
  const m = arr[index++];
  let s1: number = 0;
  let s2: number = 0;
  let c: number[] = [];
  let t: [number, number];
  let i: number;
  let j: number;

  for (i = 0; i < n; i++) {
    t = solve(arr, index, P1);
    index = t[0];
    c.push(t[1]);
    s1 += t[1];
  }

  for (i = 0; i < m; i++) {
    if (n > 0) {
      j = arr[index] - 1;
      s2 += 0 <= j && j < c.length ? c[j] : 0;
    } else {
      s2 += arr[index];
    }

    s1 += arr[index++];
  }

  return [index, P1 ? s1 : s2];
};

const arr: number[] = getInput("input.txt");
console.log(solve(arr, 0, true)[1]);
console.log(solve(arr, 0, false)[1]);
