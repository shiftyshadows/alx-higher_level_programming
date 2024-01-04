#!/usr/bin/node
const fs = require('fs');

// Check if the correct number of arguments are provided
if (process.argv.length !== 4) {
  console.error('Usage: node writefile.js <file-path> <content>');
  process.exit(1);
}

// Get the file path and content from command line arguments
const filePath = process.argv[2];
const content = process.argv[3];

// Write the string to the file in utf-8
fs.writeFile(filePath, content, 'utf-8', (err) => {
  if (err) {
    console.error('Error writing to the file:', err);
  } else {
    console.log('File successfully written.');
  }
});
