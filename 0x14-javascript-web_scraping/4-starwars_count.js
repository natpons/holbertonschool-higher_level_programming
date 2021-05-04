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
    // parse all films
    for (const index in films) {
      // do the "characters" lines list for each film
      const charsinfilm = films[index].characters;
      // parse characters lines for the film one after another
      for (const onecharline in charsinfilm) {
        // parse every character line for each film
        if (charsinfilm[onecharline].includes('18')) { count = count + 1; }
      }
    }
    console.log(count);
  } else {
    console.log(error);
  }
});
