const {readFileSync } = require('fs');

const D1P1 = (input)=>{
  const contents = readFileSync(input, 'utf-8');

  let arr = contents.split(/\n\n/)

  arr = arr.map(str => str.split('\n'))

  arr = arr.map(elf => elf.reduce( (acc,curr) => acc + Number(curr),0)).sort( (a,b) =>  b - a)

  return arr.at(0)

}

const assert = (condition) => {
  if (!condition){
    throw Error('Function does not pass example given')
  }
}

assert(D1P1('./D1 Test.txt')===24000)

console.log(D1P1('./D1 Input.txt'))

