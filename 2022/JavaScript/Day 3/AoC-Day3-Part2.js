// const { readFileSync } = require('fs');

// const D3P2 = (input) => {
//   const contents = readFileSync(input, 'utf-8');
//   const inputArr = contents.split(/\n/);

//   const priorityObj = {};
//   'abcdefghijklmnopqrstuvwxyz'.split('').forEach((ele, idx) => {
//     priorityObj[ele] = idx + 1;
//     priorityObj[ele.toUpperCase()] = idx + 27;
//   });

//   const groupArr = inputArr.reduce((acc, cur, idx) => {
//     if (idx % 3 === 0) {
//       acc.push([cur]);
//     } else {
//       acc[Math.floor(idx / 3)].push(cur);
//     }
//     return acc;
//   }, []);

//   const sameArr = groupArr.map((arr) =>
//     arr.reduce((acc, cur) => {
//       if (acc.length === 0) {
//         return acc.push(cur.split(''));
//       } else {
//         cur.split('').forEach((ele, idx) => {
//           if (acc.includes(ele)) {
//             acc.splice(acc.indexOf(ele));
//           }
//         });
//       }
//     }, [])
//   );

  // const sameArr = inputArr.map(line => {
  //   return line.split('').find( (char,idx,array) => array.slice(array.length/2).includes(char))
  // })

  // return groupArr;
  // sameArr.reduce((acc,cur) => priorityObj[cur]+acc,0)
// };

// const assert = (condition) => {
//   if (!condition) {
//     throw Error('Function does not match example given');
//   }
// };

// assert(D3P2('./D3 Test.txt')===70)
// console.log(D3P2('./D3 Test.txt'));
// console.log(D3P2('./D3 Input.txt'))
