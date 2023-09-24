#!/usr/bin/node
const fs = require('fs');

// Check if the correct number of command line arguments is provided
if (process.argv.length !== 5) {
  console.error('Usage: node concat-files.js source1.txt source2.txt destination.txt');
  process.exit(1);
}

const source1FilePath = process.argv[2];
const source2FilePath = process.argv[3];
const destinationFilePath = process.argv[4];

// Read the contents of the first source file
fs.readFile(source1FilePath, 'utf8', (err, data1) => {
  if (err) {
    console.error(`Error reading ${source1FilePath}: ${err}`);
    process.exit(1);
  }

  // Read the contents of the second source file
  fs.readFile(source2FilePath, 'utf8', (err, data2) => {
    if (err) {
      console.error(`Error reading ${source2FilePath}: ${err}`);
      process.exit(1);
    }

    // Concatenate the contents of both source files
    const concatenatedData = data1 + data2;

    // Write the concatenated data to the destination file
    fs.writeFile(destinationFilePath, concatenatedData, 'utf8', (err) => {
      if (err) {
        console.error(`Error writing to ${destinationFilePath}: ${err}`);
        process.exit(1);
      }

      console.log(`Files ${source1FilePath} and ${source2FilePath} concatenated to ${destinationFilePath}`);
    });
  });
});
