#!/usr/bin/env node

"use strict";

import { readFileSync } from "node:fs";

const lines = readFileSync("input.txt", "utf-8").trim().split("\n");

const re =
  /^position=<\s*(-?\d+),\s*(-?\d+)>\s*velocity=<\s*(-?\d+),\s*(-?\d+)>$/;

let Garr = [];
for (const l of lines) {
  const m = l.match(re);
  const key = Array.from({ length: 4 }, (_, i) => parseInt(m[i + 1]));
  Garr.push(key);
}

const update = (currG, add) => {
  const nextG = [];
  for (const key of currG) {
    const [x, y, vx, vy] = key;
    const [newX, newY] = [add ? x + vx : x - vx, add ? y + vy : y - vy];
    const newKey = [newX, newY, vx, vy];
    nextG.push(newKey);
  }
  return nextG;
};

const getRect = (Garr) => {
  let [maxX, minX, maxY, minY] = [-Infinity, Infinity, -Infinity, Infinity];
  for (const key of Garr) {
    const [x, y, vx, vy] = key;
    [maxX, minX] = [Math.max(maxX, x), Math.min(minX, x)];
    [maxY, minY] = [Math.max(maxY, y), Math.min(minY, y)];
  }
  return [maxX, minX, maxY, minY];
};

let [before, after, iter] = [undefined, getRect(Garr), 0];
do {
  before = after;
  Garr = update(Garr, true);
  after = getRect(Garr);
  ++iter;
} while (after[0] < before[0]);
Garr = update(Garr, false);

const [maxX, minX, maxY, minY] = before;
const [cols, rows] = [maxX - minX + 1, maxY - minY + 1];

const image = [];
for (let i = 0; i < rows; ++i) {
  image.push(Array.from({ length: cols }, (_) => " "));
}

for (const key of Garr) {
  const [x, y, vx, vy] = key;
  const [dx, dy] = [x - minX, y - minY];
  image[dy][dx] = "#";
}

console.log(image.map((arr) => arr.join("")).join("\n"));
console.log(iter - 1);
