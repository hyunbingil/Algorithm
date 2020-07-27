const limit = prompt("몸무게 제한을 입력해주세요.");
const n = prompt("몇 명인지 입력해주세요.");
let member = [];
let weight = 0;
let count = 0;
for (let i=0; i<n; i++) {
    member.push(parseInt(prompt("몸무게를 입력해주세요."),10));
}

for (i=0; i<n; i++) {
    weight += member[i];
    if (weight <= limit) {
        count += 1;
    }
}

console.log(count);

// let total = 0;
// let count = 0;
// const limit = prompt('제한 무게를 입력하세요.');
// const n = prompt('인원수를 입력하세요.');

// for (let i=1; i<=n; i++){
//   total += parseInt(prompt('무게를 입력해주세요.'), 10);
//   if (total <= limit){
// 		count = i;
//   }
// }

// console.log(count);