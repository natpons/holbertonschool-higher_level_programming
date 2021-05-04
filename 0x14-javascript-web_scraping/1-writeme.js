#!/usr/bin/node
/* Script that writes a string to a file */

/* to include Node.js(file system module): allows to work with the file system on your computer */
const fs = require('fs');

/* https://nodejs.org/api/process.html#process_process_argv */
const file = process.argv[2];
const content = process.argv[3];

/* https://nodejs.dev/learn/reading-files-with-nodejs */
fs.writeFile(file, content, err => {
  if (err) {
    console.error(err);
  }
});
