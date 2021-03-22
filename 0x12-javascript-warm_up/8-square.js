#!/usr/bin/node
const x = parseInt(process.argv[2], 10);
let i;

if (isNaN(x)) {
  console.log('Missing size');
} else {
  for (i = 0; i < x; i++) {
    console.log('X'.repeat(x));
  }
}
