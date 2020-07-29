// 내 답이 더 간단하고 깔끔함 ㅎㅎ
const s = prompt("문자열을 입력하세요.");
let result = '';
for (let i in s){
    if ((s[i] == s[i].toUpperCase()) == true) {
        result += s[i].toLowerCase();
    } else {
        result += s[i].toUpperCase();
    }
}
console.log(result)