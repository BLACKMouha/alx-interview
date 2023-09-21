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

  request.get(url, function (e, r, b) {
    if (e) {
      throw (e);
    } else {
      const characters_urls = JSON.parse(b).characters;
      if (characters_urls instanceof Array) {
        characters_urls.map(character_url => {
          request.get(character_url, function (err, res, bod) {
            console.log(JSON.parse(bod).name);
          });
        });
      } else {
        console.log([]);
      }
    }
  });
}