#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  /* executes a reducer function on each element of the array, resulting in single output value */
  return (list.reduce((a, v) => (v === searchElement ? a + 1 : a), 0));
};
