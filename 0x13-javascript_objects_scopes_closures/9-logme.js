#!/usr/bin/node
let count = 0; // Initialize a counter to keep track of the number of arguments printed

exports.logMe = function (item) {
  // Print the current argument value along with the count
  console.log(`${count}: ${item}`);

  // Increment the count for the next call
  count++;
};
