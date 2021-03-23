#!/usr/bin/node

/* class Square that defines a square and inherits from Square of 5-square.js */
class Square extends require('./5-square') {
  charPrint (c) {
    if (c !== undefined) {
      for (let i = 0; i < this.height; i++) {
        console.log('C'.repeat(this.width));
      }
    } else {
      this.print();
    }
  }
}

module.exports = Square;
