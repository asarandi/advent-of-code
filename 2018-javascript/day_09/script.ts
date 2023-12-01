"use strict";
import { readFileSync } from "node:fs";

const play = (numPlayers: number, lastMarble: number): number => {
  const scores: number[] = Array(numPlayers).fill(0);
  const arr: number[] = [0];
  let marble: number = 0;
  let player: number = 0;
  let best: number = 0;

  for (let v: number = 1; v <= lastMarble; v++) {
    if (v % 23 === 0) {
      for (let i: number = 0; i < 7; i++) arr.push(arr.shift());
      scores[player] += v + arr.shift();
      arr.unshift(arr.pop());
      best = scores[player] > best ? scores[player] : best;
    } else {
      arr.unshift(arr.pop());
      arr.unshift(v);
    }
    player = (player + 1) % numPlayers;
  }

  return best;
};

console.log(play(9, 25)); // 32
console.log(play(10, 1618)); // 8317
console.log(play(13, 7999)); // 146373
console.log(play(17, 1104)); // 2764
console.log(play(21, 6111)); // 54718
console.log(play(30, 5807)); // 37305
console.log(play(423, 71944)); // 418237
console.log(play(423, 7194400)); // snail
