#!/usr/bin/node

const request = require('request');

/**
 * Fetches character names from the Star Wars API for a given movie ID.
 *
 * Usage: ./0-starwars_characters.js <Movie ID>
 *
 * @module StarWarsCharacters
 */

// Check if the correct number of arguments is provided
if (process.argv.length !== 3) {
  console.log('Usage: ./0-starwars_characters.js <Movie ID>');
  process.exit(1);
}

// Get the movie ID from the command line arguments
const movieId = process.argv[2];

// Validate that the movie ID is a number
if (isNaN(movieId)) {
  console.log('Movie ID must be a number');
  process.exit(1);
}

// Construct the URL to fetch movie details
const movieUrl = `https://swapi-api.hbtn.io/api/films/${movieId}/`;

/**
 * Retrieves character names for the specified movie ID.
 *
 * @param {string} movieUrl - The URL to fetch movie details including character URLs.
 */
function fetchCharacterNames (movieUrl) {
  request(movieUrl, { json: true }, (err, res, body) => {
    // Handle request errors and non-200 response codes
    if (err || res.statusCode !== 200) {
      console.error(`Failed to fetch data: ${err || `Status code ${res.statusCode}`}`);
      process.exit(1);
    }

    const characters = body.characters;
    const characterNames = new Array(characters.length).fill(null);
    let completedRequests = 0;

    // Fetch each character's name
    characters.forEach((url, index) => {
      request(url, { json: true }, (err, res, body) => {
        if (!err && res.statusCode === 200) {
          characterNames[index] = body.name;
        }
        completedRequests++;

        // Once all requests are completed, log the character names
        if (completedRequests === characters.length) {
          characterNames.forEach(name => console.log(name));
        }
      });
    });
  });
}

// Start fetching character names for the specified movie
fetchCharacterNames(movieUrl);
