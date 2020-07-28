let n = prompt("숫자를 입력하세요.");
const arr = [];
let result = '';
function to_binary(m, a) {
    a.push(m % 2);
    m = parseInt((m/2), 10);

    if (m == 0) {
        a.reverse();
        a.forEach((n) => {
            result += n;
        })
        return console.log(result);
    } else {
        to_binary(m, a);
    }
}

to_binary(n, arr)

// let a = prompt('10진수를 입력해주세요.')
// let b = [];
// let result = '';

// while (a){
// 	b.push(a % 2);
// 	a = parseInt(a / 2, 10);
// }
// b.reverse();

// b.forEach((n) => {
//   result += n;
// })

// console.log(result);