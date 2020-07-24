// replace 같은거 쓰면 안되는건가 ....?

let typing = prompt("q를 e로 바꿔드려요");
result = typing.replace("q", "e");
console.log(result);

//1. 함수 사용
// const word = prompt('입력하세요.');

// function replaceAll(str, searchStr, replaceStr) {
//    return str.split(searchStr).join(replaceStr);
// }

// console.log(replaceAll(word,"q","e"));

//2. 정규식 사용
// const word = prompt('입력하세요.');

// console.log(word.replace(/q/gi, 'e'));