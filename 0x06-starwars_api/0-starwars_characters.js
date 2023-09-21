#!/usr/bin/node
/* jshint esversion: 8 */

/**
 * Print all characters of a Star Wars movie
 * There is only one argument passed to the program and is the movie ID
 */

if (process.argv.length === 3) {
  const request = require('request');
  const id = process.argv[2];
  const url = 'https://swapi-api.alx-tools.com/api/films/' + id;

  const characters_urls = request.get(url, (err, res, body) => {
    if (err) {
      console.error(err);
    } else {
      const characters_urls = JSON.parse(body).characters;
      characters_urls.forEach((Character_url) => {
        request.get(Character_url, (e, r, b) => {
          if (e) {
            console.log(e);
          } else {
            console.log(JSON.parse(b).name);
          }
        });
      });
    }
  });
}
