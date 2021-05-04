#!/usr/bin/node
// Script that gets the contents of a webpage and stores it in a file

const request = require('request');
const fs = require('fs');

const url = process.argv[2];
const path = process.argv[3];

// https://github.com/request/request
request
  .get(url)
  .on('error', function (err) {
    console.error(err);
  })
  .pipe(fs.createWriteStream(path));
