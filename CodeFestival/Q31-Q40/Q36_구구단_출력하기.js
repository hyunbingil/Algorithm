const n = prompt("숫자를 입력하세요.");
let arr = [];
for (let i=0; i<9; i++) {
    arr[i] = n * (i+1);
}

arr = arr.join(' ');
console.log(arr);

// const num = prompt('1 ~ 9까지의 숫자 중 하나를 입력하세요.')
// let result = '';

// for (let i=1; i<=9; i++){
//   result += i*num + ' ';
// }

// console.log(result);