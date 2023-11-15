#!/usr/bin/node
const OldSquare = require('./5-square');

class Square extends OldSquare {
  constructor (size) {
    super(size, size);
  }

  double () {
    super.double();
  }

  charPrint (c = 'X') {
    for (let i = 0; i < this.height; ++i) {
      let j = 0;
      for (; j < this.width; ++j) {
        process.stdout.write(c);
      }
      if (j === this.width) {
        console.log('');
      }
    }
  }
}

module.exports = Square;
