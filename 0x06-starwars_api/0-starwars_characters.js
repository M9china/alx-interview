#!/usr/bin/env node

const axios = require('axios');

// Fetch and display all characters of a Star Wars movie
async function fetchMovieCharacters(movieId) {
    try {
        // Get the film data
        const filmResponse = await axios.get(`https://swapi.dev/api/films/${movieId}/`);
        const characterUrls = filmResponse.data.characters;

        // Retrieve and print each character's name in order
        for (const url of characterUrls) {
            const characterResponse = await axios.get(url);
            console.log(characterResponse.data.name);
        }
    } catch (error) {
        console.error(`Error fetching movie data: ${error.message}`);
    }
}

// Get the Movie ID from the command line argument
const movieId = process.argv[2];
if (!movieId) {
    console.log("Usage: ./0-starwars_characters.js <Movie ID>");
    process.exit(1);
}

fetchMovieCharacters(movieId);
