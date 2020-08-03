let one = "";
let result = 0;
for (let i = 0; i<1000; i++) {
  one += (i+1)
}

for (let i = 0; i<one.length; i++) {
  if (one[i] === '1') {
    result += 1;
  }
}

console.log(result);


// //1번 답안
// const obj = {};

// for (let i = 0; i <= 1000; i++) {
//     let tmp = i;
//     while (tmp > 0) {
//         let num = tmp % 10;
//         if (obj[num]) {
//             obj[num]++;
//         } else {
//             obj[num] = 1;
//         }
//         tmp = parseInt(tmp/10, 10);
//     }
// }

// console.log(obj[1]);

// //2번 답안
// let s = ''
// for(let i = 0; i<1000; i++){
//   s += i
// }
// console.log(s);
// console.log(s.match(/1/g).length);

// //3번 답안
// let s = ''
// for(let i = 0; i<1000; i++){
//   s += i;
// }
// let count = 0
// for(let j in s){
//   if(s[j] == 1){
//     count++;
//   }
// }
// console.log(count);

// //4번답안
// let s = ''
// for(let i = 0; i<1000; i++){
//   s += i;
// }
// let count = 0
// for(let j of s){
//   if (j == 1){
//     count++;
//   }
// }
// console.log(count);