#!/usr/bin/node

exports.esrever = function (list) {
  /* creates a new array with the results of calling a provided function on every element in the calling array */
  return (list.map((item, index) => list[list.length - 1 - index]));
};
