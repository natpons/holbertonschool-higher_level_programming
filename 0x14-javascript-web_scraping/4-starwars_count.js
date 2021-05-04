#!/usr/bin/node
// Script that prints the number of movies where the character Wedge Antilles is present

// must use the module request
const request = require('request');
const url = process.argv[2];

request(url, function (error, response, body) {
  if (response.statusCode === 200) {
    // responseData.results is an object that has a key results
    const films = JSON.parse(body).results;
    let count = 0;
    for (const filmIND in films) {
      // choose all characters for each film
      const filmCHARS = films[filmIND].characters;
      // parse all indexes in every film
      for (const charIND in filmCHARS) {
        // parse every character for very film
        if (filmCHARS[charIND].includes('18')) { count = count + 1; }
      }
    }
    console.log(count);
  } else {
    console.log(error);
  }
});
