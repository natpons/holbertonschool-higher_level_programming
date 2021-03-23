#!/usr/bin/node

const Square = require('./5-square');

class Square extends Square {
	constructor (size) {
		super(size, size);
		this.size = size;
	}
}

Square.prototype.charPrint = function () {
	for (let i = 0; i < this.size; i++) {
		console.log('C'.repeat(this.size));
	}

	module.exports = Square;
