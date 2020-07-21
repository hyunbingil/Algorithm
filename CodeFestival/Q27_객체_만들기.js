const keys = prompt("이름을 입력하세요.").split(' ');
const scores = prompt("점수를 입력하세요.").split(' ');
const obj = {};

for (i=0; i<keys.length; i++) {
    obj[keys[i]] = parseInt(scores[i], 10);
}

console.log(obj);
