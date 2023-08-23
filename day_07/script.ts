"use strict";
import { readFileSync } from "fs";

const getInput = (f: string): object => {
  const o: object = {};
  const S: string[] = readFileSync(f, "utf-8").trim().split("\n");
  for (let i: number = 0; i < S.length; i++) {
    o[S[i].slice(5, 6)] = {};
    o[S[i].slice(36, 37)] = {};
  }
  for (let i: number = 0; i < S.length; i++) {
    o[S[i].slice(36, 37)][S[i].slice(5, 6)] = true;
  }
  return o;
};

const numObjectKeys = (o: object): number => Object.keys(o).length;
const getReadySteps = (o: object): string[] =>
  Object.keys(o)
    .filter((k) => numObjectKeys(o[k]) === 0)
    .sort();

const evaluate = (o: object, c: string): object => {
  for (const k of Object.keys(o)) delete o[k][c];
  delete o[c];
  return o;
};

const solveP1 = (o: object): string => {
  const arr: string[] = [];
  while (numObjectKeys(o) > 0) {
    const c: string = getReadySteps(o)[0];
    o = evaluate(o, c);
    arr.push(c);
  }
  return arr.join("");
};

const getDuration = (s: string): number => s.charCodeAt(0) - 4;

const solveP2 = (o: object): number => {
  const workers: object[] = [];
  for (let i: number = 0; i < 5; i++) workers.push({ t: 0, c: "" });

  const processing: object = {};
  let time = 0;

  while (numObjectKeys(o) > 0) {
    for (const c of getReadySteps(o)) {
      if (c in processing) continue;
      for (const i in workers) {
        if (workers[i]["t"] === 0) {
          workers[i] = { t: getDuration(c), c: c };
          processing[c] = true;
          break;
        }
      }
    }

    for (const i in workers) {
      if (workers[i]["t"] > 0 && --workers[i]["t"] === 0) {
        o = evaluate(o, workers[i]["c"]);
      }
    }

    time++;
  }
  return time;
};

console.log(solveP1(getInput("input.txt")));
console.log(solveP2(getInput("input.txt")));
