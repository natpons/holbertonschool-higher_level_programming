#!/usr/bin/node
/* Script that prints the title of a Star Wars movie where the episode number matches a given integer */

/* must use the module request */
const request = require('request');

const url = 'https://swapi-api.hbtn.io/api/films/';
const episode = process.argv[2];

/* https://github.com/request/request */
request(url + episode, function (error, response, body) {
  if (response.statusCode === 200) {
    /* JSON string as a parameter, returns the corresponding JavaScript object */
    const jsonobj = JSON.parse(body);
    console.log(jsonobj.title);
  } else {
    console.log(error);
  }
});
