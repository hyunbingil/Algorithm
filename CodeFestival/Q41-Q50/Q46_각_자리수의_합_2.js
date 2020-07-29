let number = '';
// let arr = [];
let result = 0;
for (let i=1; i<21; i++) {
    number += i
}

// for (let i=0; i<number.length; i++) {
//     arr.push(number[i])
// }

for (let i=0; i<number.length; i++) {
    result += parseInt(number[i], 10)
}

console.log(result)

// let arr = [];
// let sum = 0;

// for (let i=0; i<20; i++){
//   arr[i] = i+1;
// }

// arr.forEach((n) => {
//   while(n !== 0){
//     sum += (n % 10);
//     n = Math.floor(n/10);
//   }
// })

// console.log(sum);