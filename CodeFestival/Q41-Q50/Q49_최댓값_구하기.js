let number = prompt("숫자 10개를 입력해주세요.").split(' ').map((n) => {
    return parseInt(n, 10);
});

number.sort(function(a, b) { // 오름차순
    return a - b;
});
console.log(number[9]);

// 내림차순 이용해서 구해도 된다.
// numbers.sort((a, b) => {
//     return b-a;
//   });
  
//   console.log(numbers[0]);