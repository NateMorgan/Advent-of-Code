const {readFileSync } = require('fs');

const D1P2 = (input)=>{
  const contents = readFileSync(input, 'utf-8');

  let arr = contents.split(/\n\n/)

  arr = arr.map(str => str.split('\n'))

  arr = arr.map(elf => elf.reduce( (acc,curr) => acc + Number(curr),0)).sort( (a,b) =>  b - a)

  return arr.slice(0,3).reduce( (acc,cur) => acc + cur,0)

}

const assert = (condition) => {
  if (!condition){
    throw Error('Function does not pass example given')
  }
}

assert(D1P2('./D1 Test.txt')===45000)

console.log(D1P2('./D1 Input.txt'))

