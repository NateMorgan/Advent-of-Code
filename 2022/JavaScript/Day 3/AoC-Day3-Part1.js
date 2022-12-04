const { readFileSync } = require('fs')


const D3P1 = (input) =>{
  const contents = readFileSync(input,'utf-8')
  const inputArr = contents.split(/\n/)

  const priorityObj = {}
  'abcdefghijklmnopqrstuvwxyz'.split('').forEach((ele,idx) => {
    priorityObj[ele] = idx + 1
    priorityObj[ele.toUpperCase()] = idx + 27
  })

  const sameArr = inputArr.map(line => {
    return line.split('').find( (char,idx,array) => array.slice(array.length/2).includes(char))
  })

  return sameArr.reduce((acc,cur) => priorityObj[cur]+acc,0)
}

const assert = (condition) => {
  if (!condition){
    throw Error("Function does not match example given")
  }
}

assert(D3P1('./D3 Test.txt')===157)
console.log(D3P1('./D3 Input.txt'))

