#!/usr/bin/node
const OldSquare = require('./5-square');

class Square extends OldSquare {
  constructor (size) {
    super(size, size);
  }

  double () {
    super.double();
  }

  charPrint (c) {
    for (let i = 0; i < this.size; ++i) {
      let j = 0;
      for (; j < this.size; ++j) {
        process.stdout.write(c);
      }
      if (j === this.size) {
        console.log('');
      }
    }
  }
}

module.exports = Square;
