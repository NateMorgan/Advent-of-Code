const { readFileSync } = require('fs')

const handleScoring = (line) => {

  const score = {
    A:1,
    B:2,
    C:3,
    X:1,
    Y:2,
    Z:3
  }

  let picks = line.split(" ")
  let opponentScore = score[picks[0]]
  let myScore = score[picks[1]]
  if (opponentScore === myScore){
    return 3 + myScore
  } else if (opponentScore-myScore === -1 || opponentScore-myScore === 2){
    return 6 + myScore
  } else {
    return myScore
  }
}

const D2P1 = (input) => {
  const contents = readFileSync(input,'utf-8')

  let arr = contents.split(/\n/)

  output = arr.map(line => handleScoring(line)).reduce( (acc,cur) => acc + cur,0)

  return output
}

const assert= (condition) => {
  if (!condition){
    throw Error('Function does match example given')
  }
}

assert(D2P1('./D2 Test.txt')===15)

console.log(D2P1('./D2 Input.txt'))