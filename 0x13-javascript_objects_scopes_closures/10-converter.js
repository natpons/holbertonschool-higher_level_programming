#!/usr/bin/node

exports.converter = function (base) {
  return function (value) {
    /* convert one base to another for decimal input */
    return value.toString(base);
  };
};
