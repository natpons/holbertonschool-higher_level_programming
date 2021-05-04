#!/usr/bin/node
// Script that computes the number of tasks completed by user id

const request = require('request');
const url = process.argv[2];

/* https://github.com/request/request */
request(url, function (error, response, body) {
  if (response.statusCode === 200) {
    const result = {};
    // body with all objs: list of dict's
    const objs = JSON.parse(body);
    // to parse objs one after another by id
    for (const id in objs) {
      const obj = objs[id];
      if (obj.completed === true) {
        // if I see this userId for the first time
        if (result[obj.userId] === undefined) {
          result[obj.userId] = 1;
        } else {
          result[obj.userId] = result[obj.userId] + 1;
        }
      }
    }
    console.log(result);
  } else {
    console.log(error);
  }
});
