// 내 답안 : 배열과 문자열 활용.
let number = prompt("숫자를 입력하세요.").split('');
let sum = 0;
for (let i=0; i<number.length; i++) {
    sum += parseInt(number[i], 10);
}

console.log(sum);

// 답안 : 숫자 자체에서 연산을 통해 해결.
// let n = prompt('숫자를 입력하세요.');
// let sum = 0;

// while(n !== 0){
//   sum += (n % 10);
//   n = Math.floor(n/10);
// }

// console.log(sum);