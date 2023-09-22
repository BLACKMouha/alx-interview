#!/usr/bin/node
/* jshint esversion: 8 */

/**
 * Print all characters of a Star Wars movie
 * There is only one argument passed to the program and is the movie ID
 */
const request = require('request');

const id = process.argv[2] || 1;
const movieUrl = 'https://swapi-api.alx-tools.com/api/films/' + id;

function getMovieCharacters (charactersUrls, index = 0) {
  if (index >= charactersUrls.length) {
    return;
  }
  const characterUrl = charactersUrls[index];
  request(characterUrl, (err, res, body) => {
    if (err) {
      throw (err);
    } else {
      console.log(JSON.parse(body).name);
      getMovieCharacters(charactersUrls, index + 1);
    }
  });
}

request(movieUrl, (err, res, body) => {
  if (err) {
    throw (err);
  } else {
    const charactersUrls = (JSON.parse(body).characters);
    getMovieCharacters(charactersUrls, 0);
  }
});
