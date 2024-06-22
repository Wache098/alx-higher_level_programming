#!/usr/bin/node
// Script that prints the first argument passed to it

const arg1 = process.argv[2];

if (!arg1) {
  console.log('No argument');
} else {
  console.log(arg1);
}
