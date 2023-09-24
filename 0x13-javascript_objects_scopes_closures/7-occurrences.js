#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  // Initialize a count variable to keep track of the occurrences
  let count = 0;

  // Loop through the list and check each element
  for (let i = 0; i < list.length; i++) {
    if (list[i] === searchElement) {
      // If the current element matches the search element, increment the count
      count++;
    }
  }

  // Return the final count of occurrences
  return count;
};
