#!/usr/bin/node
/* Script that reads and prints the content of a file */

/* to include Node.js(file system module): allows to work with the file system on your computer */
const fs = require('fs');

/* https://nodejs.org/api/process.html#process_process_argv */
const file = process.argv[2];

/* https://nodejs.dev/learn/reading-files-with-nodejs */
fs.readFile(file, 'utf-8', function (err, data) {
  if (err) {
    console.log(err);
  } else {
    console.log(data);
  }
});
