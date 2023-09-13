#!/usr/bin/node
function findSecondLargest (numbers) {
  if (numbers.length < 2) {
    return 0; // Not enough numbers to find the second largest
  }

  const largest = Math.max(...numbers);
  numbers = numbers.filter(num => num !== largest);

  const secondLargest = Math.max(...numbers);
  return secondLargest;
}

// Parse command-line arguments as integers
const args = process.argv.slice(2).map(arg => parseInt(arg)).filter(num => !isNaN(num));

const secondLargest = findSecondLargest(args);

console.log(secondLargest);
