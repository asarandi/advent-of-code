"use strict";
import { readFileSync } from "fs";

interface Point {
  x: number;
  y: number;
}

interface Rect {
  L: number;
  R: number;
  U: number;
  D: number;
}

const distance = (a: Point, b: Point) =>
  Math.abs(a.x - b.x) + Math.abs(a.y - b.y);

const getInput = (f: string): Point[] => {
  const lines: string[] = readFileSync(f, "utf-8").trim().split("\n");
  const arr: Point[] = [];
  for (const l of lines) {
    const m: object = l.match(/(\d+), (\d+)/);
    arr.push({ x: parseInt(m[1]), y: parseInt(m[2]) });
  }
  return arr;
};

const getRect = (arr: Point[]): Rect => {
  const rect: Rect = { L: arr[0].x, R: arr[0].x, U: arr[0].y, D: arr[0].y };
  for (let i: number = 0; i < arr.length; i++) {
    rect.L = Math.min(rect.L, arr[i].x);
    rect.R = Math.max(rect.R, arr[i].x);
    rect.U = Math.min(rect.U, arr[i].y);
    rect.D = Math.max(rect.D, arr[i].y);
  }
  return rect;
};

const isFinite = (arr: Point[], rect: Rect): boolean => {
  for (let i: number = 0; i < arr.length; i++) {
    const pt: Point = arr[i];
    if (
      pt.x === rect.L ||
      pt.x === rect.R ||
      pt.y === rect.U ||
      pt.y === rect.D
    )
      return false;
  }
  return true;
};

const iterCoordinates = (arr: Point[], pt: Point): [number[], number] => {
  let minDistance: number = Infinity;
  let candidates: number[] = [];
  let sumDistance = 0;

  for (let i: number = 0; i < arr.length; i++) {
    const d = distance(arr[i], pt);
    if (d < minDistance) {
      minDistance = d;
      candidates = [i];
    } else if (d === minDistance) {
      candidates.push(i);
    }
    sumDistance += d;
  }
  return [candidates, sumDistance];
};

const iterRect = (arr: Point[], rect: Rect): [object, number] => {
  const coordinatePoints: object = {};
  let regionSize: number = 0;

  for (let y: number = rect.U; y <= rect.D; y++) {
    for (let x: number = rect.L; x <= rect.R; x++) {
      const pt: Point = { x: x, y: y };
      const tuple: [number[], number] = iterCoordinates(arr, pt);
      regionSize += tuple[1] < 10000 ? 1 : 0;

      if (tuple[0].length === 1) {
        const index: number = tuple[0].pop();
        if (!(index in coordinatePoints)) coordinatePoints[index] = [];
        coordinatePoints[index].push(pt);
      }
    }
  }
  return [coordinatePoints, regionSize];
};

const solve = (arr: Point[], rect: Rect): [number, number] => {
  const tuple: [object, number] = iterRect(arr, rect);

  let area: number = -Infinity;
  for (const [k, v] of Object.entries(tuple[0])) {
    if (isFinite(v, rect)) {
      area = Math.max(area, v.length);
    }
  }
  return [area, tuple[1]];
};

const arr = getInput("input.txt");
const rect = getRect(arr);
const output = solve(arr, rect);

console.log(output[0], output[1]);
