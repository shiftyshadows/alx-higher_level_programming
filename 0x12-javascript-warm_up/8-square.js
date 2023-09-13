#!/usr/bin/node
const arg1 = parseInt(process.argv[2], 10);

for (let i = 0; i < arg1; i++){
    let str = 'X'.repeat(arg1);
    console.log(str);
}
