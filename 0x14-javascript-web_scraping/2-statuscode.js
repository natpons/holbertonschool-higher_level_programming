#!/usr/bin/node
// Script that display the status code of a GET request

/* must use the module request */
const request = require('request');
const url = process.argv[2];

request.get(url, function (error, response) {
  if (error) {
    console.log(error);
  } else {
  // Print the response status code if a response was received
    console.log('code:', response && response.statusCode);
  }
});
