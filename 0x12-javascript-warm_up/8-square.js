#!/usr/bin/node
const arg1 = parseInt(process.argv[2], 10);

if (Number.isInteger(arg1)) {
  for (let i = 0; i < arg1; i++) {
    const str = 'X'.repeat(arg1);
    console.log(str);
  }
} else {
  console.log('Missing size');
}
