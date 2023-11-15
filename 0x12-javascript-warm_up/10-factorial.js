#!/usr/bin/node
function factorial (n) {
  // Base case: factorial of 0 or 1 is 1
  if (n === 0 || n === 1 || isNaN(n)) {
    return 1;
  }
  // Recursive case: compute factorial by multiplying n with factorial(n-1)
  return n * factorial(n - 1);
}

const arg1 = parseInt(process.argv[2], 10);
const result = factorial(arg1);

console.log(result);
