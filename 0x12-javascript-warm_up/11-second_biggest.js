#!/usr/bin/node
if (process.argv.length <= 3) {
  console.log(0);
} else {
  const a = process.argv.slice(2).sort((a, b) => b - a);
  console.log(a[1]);
}
