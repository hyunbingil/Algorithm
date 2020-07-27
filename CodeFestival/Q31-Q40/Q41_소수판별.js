function check_prime(n) {
    let i = 2;
    while (i < n) {
        if (n % 1 == 0) {
            break;
        }
        i += 1;
    }
    if (i = n) {
        console.log("YES");
    } else {
        console.log("NO");
    }
}

check_prime(parseInt(prompt("수를 입력하세요."), 10));

// const num = prompt('숫자를 입력하세요.');

// function check_prime(num) {
//   for (let i=2; i<num; i++) {
//     const result = num % i;
//     if (result === 0) {
//       console.log('NO');
//       return false;
//     }
//   }
//   if (num === 1) {
//     console.log('NO');
//     return;
//   }
//   console.log('YES');
// }

// check_prime(num);