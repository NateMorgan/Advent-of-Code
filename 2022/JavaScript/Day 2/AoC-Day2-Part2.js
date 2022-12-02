const { readFileSync } = require('fs')

const handleScoring = (line) => {

  const score = {
    A:1,
    B:2,
    C:3,
    X:0,
    Y:3,
    Z:6
  }

  let picks = line.split(" ")
  let opponentScore = score[picks[0]]
  let result = score[picks[1]]
  if (result === 3){
    return result + opponentScore
  } else if (result === 6){
    return opponentScore !== 3 ? result + opponentScore + 1 : result + 1
  } else {
    return opponentScore !== 1 ? result + opponentScore - 1 : result + 3
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

assert(D2P1('./D2 Test.txt')===12)

console.log(D2P1('./D2 Input.txt'))