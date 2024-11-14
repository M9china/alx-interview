#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

request(apiUrl, (error, response, body) => {
  if (error) return console.error(error);

  const characters = JSON.parse(body).characters;
  const characterNames = [];

  const printCharacters = () => {
    characterNames.forEach((name) => console.log(name));
  };

  characters.forEach((character, index) => {
    request(character, (error, response, body) => {
      if (error) return console.error(error);

      characterNames[index] = JSON.parse(body).name;

      if (characterNames.filter(Boolean).length === characters.length) {
        printCharacters();
      }
    });
  });
});
