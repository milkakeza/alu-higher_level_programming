#!/usr/bin/node
export function converter (base) {
  return (num) => num.toString(base);
}